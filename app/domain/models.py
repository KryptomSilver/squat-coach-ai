# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
from dataclasses import dataclass


@dataclass(frozen=True)
class VideoMetadata:
    fps: float
    width: int
    height: int
    frame_count: int


@dataclass(frozen=True)
class LandmarkPoint:
    x: float
    y: float
    z: float
    visibility: float


@dataclass(frozen=True)
class FramePose:
    frame_index: int
    timestamp_s: float
    landmarks: dict[str, LandmarkPoint]

    @property
    def pose_detected(self) -> bool:
        return bool(self.landmarks)
