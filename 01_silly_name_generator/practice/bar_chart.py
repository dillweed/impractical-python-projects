"""Create a bar chart of character frequency from text input"""

from collections import defaultdict

WIDTH: int = 75  # Chart max char width


def main() -> None:
    """Process text from interactive input"""
    # Ask for text input
    input_text: str = input("Enter text: ")
    # Get dict of char sums
    sums: dict[str, int] = get_char_sums(input_text)
    # Print char sums as bar chart
    print_sum_chart(sums)


def get_char_sums(input_text: str) -> dict[str, int]:
    """Create a dictionary of character sums

    Args:
        input_text (str): 

    Returns:
        dict: 'a'-'z' keys with sum values
    """
    # Strip text of non-alpha chars
    cleaned_text: str = "".join(
        [c.lower() if c.isalpha() else "" for c in input_text])

    # Sum chars count as values in a-z dictionary
    sums: dict[str, int] = defaultdict(
        lambda: 0)  # a-z dict values default to 0
    for i in range(ord('a'), ord('z') + 1):
        sums[chr(i)] = cleaned_text.count(chr(i))

    return sums


def print_sum_chart(sums: dict[str, int]) -> None:
    """Print sums dict as bar chart

    Args:
        sums (dict): 'a'-'z' keys with char count values
    """
    # Get max count to normalize chart to WIDTH
    max_count: int = max(sums.values())
    multiplier: float = WIDTH / max_count

    # Print dict as bar chart fitted to WIDTH
    print("   "+"-" * WIDTH)
    for k, v in sums.items():
        print(f"{k}: {k*int(v*multiplier):<{WIDTH}}|")
    print("   "+"-" * WIDTH)


if __name__ == "__main__":
    main()
