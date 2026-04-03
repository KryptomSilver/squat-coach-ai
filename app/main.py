# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from pathlib import Path
import argparse
import json

import cv2

from app.config import OUTPUT_JSON_PATH, OUTPUT_VIDEO_PATH, ensure_output_dirs
from app.pipeline.pose_estimator import create_pose_estimator, estimate_pose
from app.pipeline.video_reader import iter_frames, open_video
from app.utils.drawing import draw_pose_overlay


def run_analysis(input_video: str | Path) -> dict[str, Path]:
    input_path = Path(input_video)
    if not input_path.exists():
        raise FileNotFoundError(f"No existe el video de entrada: {input_path}")

    ensure_output_dirs()
    capture, fps, width, height = open_video(input_path)
    pose = create_pose_estimator()
    writer = cv2.VideoWriter(str(OUTPUT_VIDEO_PATH), cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
    if not writer.isOpened():
        capture.release()
        pose.close()
        raise RuntimeError(f"No se pudo crear el video de salida: {OUTPUT_VIDEO_PATH}")

    landmarks_by_frame = []
    processed_frames = 0
    try:
        for frame_index, timestamp_s, frame in iter_frames(capture):
            landmarks, pose_landmarks = estimate_pose(pose, frame)
            landmarks_by_frame.append(
                {
                    "frame_index": frame_index,
                    "timestamp_s": timestamp_s,
                    "pose_detected": bool(landmarks),
                    "landmarks": landmarks,
                }
            )

            annotated = draw_pose_overlay(frame, pose_landmarks, frame_index)
            writer.write(annotated)
            processed_frames += 1
    finally:
        writer.release()
        capture.release()
        pose.close()

    if processed_frames == 0:
        raise RuntimeError("El video no contiene frames procesables")

    with OUTPUT_JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(landmarks_by_frame, f, indent=2)

    return {
        "json_landmarks": OUTPUT_JSON_PATH,
        "annotated_video": OUTPUT_VIDEO_PATH,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Squat Coach AI - Pipeline minimo")
    parser.add_argument("--input", required=True, help="Ruta del video de entrada")
    args = parser.parse_args()

    try:
        outputs = run_analysis(args.input)
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)

    print("Pipeline completado.")
    print(f"JSON: {outputs['json_landmarks']}")
    print(f"Video anotado: {outputs['annotated_video']}")


if __name__ == "__main__":
    main()
