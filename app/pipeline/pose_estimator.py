# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from typing import Any

import cv2

from app.config import POSE_PARAMS
from app.utils.mp_compat import load_mediapipe_modules


MP_POSE, _, _ = load_mediapipe_modules()


def create_pose_estimator() -> Any:
    return MP_POSE.Pose(
        static_image_mode=False,
        model_complexity=POSE_PARAMS["model_complexity"],
        min_detection_confidence=POSE_PARAMS["min_detection_confidence"],
        min_tracking_confidence=POSE_PARAMS["min_tracking_confidence"],
    )


def estimate_pose(pose: Any, frame_bgr: Any) -> tuple[dict[str, dict[str, float]], Any | None]:
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    result = pose.process(frame_rgb)

    landmarks: dict[str, dict[str, float]] = {}
    if result.pose_landmarks:
        for idx, lm in enumerate(result.pose_landmarks.landmark):
            landmark_name = MP_POSE.PoseLandmark(idx).name
            landmarks[landmark_name] = {
                "x": float(lm.x),
                "y": float(lm.y),
                "z": float(lm.z),
                "visibility": float(lm.visibility),
            }

    return landmarks, result.pose_landmarks
