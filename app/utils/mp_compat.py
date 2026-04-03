# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
"""Compat layer for MediaPipe imports across versions."""


def load_mediapipe_modules():
    try:
        import mediapipe as mp
    except Exception as exc:
        raise RuntimeError(
            "MediaPipe no esta instalado. Ejecuta: pip install -r requirements.txt"
        ) from exc

    if hasattr(mp, "solutions"):
        return mp.solutions.pose, mp.solutions.drawing_utils, mp.solutions.drawing_styles

    try:
        from mediapipe.python.solutions import drawing_styles
        from mediapipe.python.solutions import drawing_utils
        from mediapipe.python.solutions import pose
    except Exception as exc:
        raise RuntimeError(
            "No se pudo cargar MediaPipe Pose. Reinstala con: pip install mediapipe==0.10.14"
        ) from exc

    return pose, drawing_utils, drawing_styles
