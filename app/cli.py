# Copyright (c) 2026 Abel Romero Ruiz - Developed with assistance from Codex
import argparse

from app.main import run_analysis


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Squat Coach AI - MVP CLI")
    parser.add_argument("--input", required=True, help="Path to input video")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    outputs = run_analysis(args.input)

    print("Analysis completed.")
    print(f"Annotated video: {outputs['annotated_video']}")
    print(f"Landmarks JSON: {outputs['json_landmarks']}")


if __name__ == "__main__":
    main()
