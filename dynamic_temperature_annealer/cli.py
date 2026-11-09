"""CLI for dynamic-temperature-annealer."""
import sys
import argparse
from .annealer import TemperatureAnnealer


def main():
    parser = argparse.ArgumentParser(description="Dynamic Temperature Annealer CLI")
    parser.add_argument("--demo", action="store_true", help="Run dynamic sampling parameter recommendation demo")
    args = parser.parse_args()

    if args.demo:
        annealer = TemperatureAnnealer()
        p1 = annealer.recommend_params("Write a Python function with json schema validation")
        p2 = annealer.recommend_params("Brainstorm 10 creative marketing slogans for AI tool")

        print("Code Prompt Parameters:", p1.to_dict())
        print("Creative Prompt Parameters:", p2.to_dict())
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
