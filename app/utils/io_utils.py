# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
import csv
import json
from dataclasses import asdict
from pathlib import Path

from app.domain.models import FramePose


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def export_landmarks_json(frame_poses: list[FramePose], output_path: Path) -> None:
    ensure_parent(output_path)
    payload = [asdict(frame_pose) for frame_pose in frame_poses]
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def export_landmarks_csv(frame_poses: list[FramePose], output_path: Path) -> None:
    ensure_parent(output_path)
    columns = ["frame_index", "timestamp_s", "landmark", "x", "y", "z", "visibility", "pose_detected"]
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

        for frame_pose in frame_poses:
            if not frame_pose.landmarks:
                writer.writerow(
                    {
                        "frame_index": frame_pose.frame_index,
                        "timestamp_s": frame_pose.timestamp_s,
                        "landmark": "NO_POSE",
                        "x": "",
                        "y": "",
                        "z": "",
                        "visibility": "",
                        "pose_detected": False,
                    }
                )
                continue

            for name, point in frame_pose.landmarks.items():
                writer.writerow(
                    {
                        "frame_index": frame_pose.frame_index,
                        "timestamp_s": frame_pose.timestamp_s,
                        "landmark": name,
                        "x": point.x,
                        "y": point.y,
                        "z": point.z,
                        "visibility": point.visibility,
                        "pose_detected": True,
                    }
                )
