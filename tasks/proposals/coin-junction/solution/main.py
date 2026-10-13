"""Reference scaffold for the coin-junction task."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_workspace', required=False, default='.')
    args = parser.parse_args()
    print('solution placeholder for coin-junction')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
