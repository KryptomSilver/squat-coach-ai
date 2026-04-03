# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from pathlib import Path

OUTPUT_JSON_PATH = Path("outputs/json/landmarks.json")
OUTPUT_VIDEO_PATH = Path("outputs/videos/annotated.mp4")

POSE_PARAMS = {
    "model_complexity": 1,
    "min_detection_confidence": 0.5,
    "min_tracking_confidence": 0.5,
}


def ensure_output_dirs() -> None:
    OUTPUT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_VIDEO_PATH.parent.mkdir(parents=True, exist_ok=True)
