"""Simple tool to add numbers."""

def add_numbers(*numbers: float) -> float:
    """Return the sum of the provided numbers.

    Args:
        *numbers: Numeric values to be added.

    Returns:
        The arithmetic sum of all provided numbers.
    """
    return sum(numbers)


def main() -> None:
    """Command line interface for adding numbers."""
    import argparse

    parser = argparse.ArgumentParser(description="Add numbers together.")
    parser.add_argument("numbers", metavar="N", type=float, nargs="+", help="Numbers to add")
    args = parser.parse_args()

    result = add_numbers(*args.numbers)
    print(result)


if __name__ == "__main__":
    main()
