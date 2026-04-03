# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from pathlib import Path
from typing import Any
from typing import Generator

import cv2


def open_video(video_path: str | Path) -> tuple[cv2.VideoCapture, float, int, int]:
    path = Path(video_path)
    capture = cv2.VideoCapture(str(path))
    if not capture.isOpened():
        raise ValueError(f"No se pudo abrir el video: {path}")

    fps = capture.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return capture, float(fps), width, height


def iter_frames(capture: cv2.VideoCapture) -> Generator[tuple[int, float, Any], None, None]:
    fps = capture.get(cv2.CAP_PROP_FPS) or 30.0
    frame_index = 0
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        timestamp_s = frame_index / max(float(fps), 1e-6)
        yield frame_index, timestamp_s, frame
        frame_index += 1
