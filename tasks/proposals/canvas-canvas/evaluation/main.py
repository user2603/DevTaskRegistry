"""Evaluation scaffold for the canvas-canvas task."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_workspace', required=False, default='.')
    args = parser.parse_args()
    print('evaluation placeholder for canvas-canvas')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
