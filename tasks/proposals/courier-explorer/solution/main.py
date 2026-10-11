"""Reference scaffold for the courier-explorer task."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_workspace', required=False, default='.')
    args = parser.parse_args()
    print('solution placeholder for courier-explorer')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
