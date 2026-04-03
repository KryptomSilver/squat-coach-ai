# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from typing import Any

import cv2

from app.utils.mp_compat import load_mediapipe_modules


MP_POSE, MP_DRAWING_UTILS, MP_DRAWING_STYLES = load_mediapipe_modules()


def draw_pose_overlay(frame_bgr: Any, pose_landmarks: Any | None, frame_index: int) -> Any:
    output = frame_bgr.copy()
    if pose_landmarks is not None:
        MP_DRAWING_UTILS.draw_landmarks(
            image=output,
            landmark_list=pose_landmarks,
            connections=MP_POSE.POSE_CONNECTIONS,
            landmark_drawing_spec=MP_DRAWING_STYLES.get_default_pose_landmarks_style(),
        )

    cv2.putText(
        output,
        f"frame={frame_index}",
        (16, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return output
