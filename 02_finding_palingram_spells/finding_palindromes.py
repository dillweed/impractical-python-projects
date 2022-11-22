"""Find palindromes within a given list of words."""
import sys

FILE_PATH: str = "words_2of4brif.txt"


def main():
    """Find palindromes within a given list of words."""
    # Read word file
    word_list: list = open_file(FILE_PATH)

    # Make a list of palindromes
    palindromes: list = []
    for word in word_list:
        if is_pal(word):
            palindromes.append(word)

    # Print palindrome list
    print(f"\n{len(palindromes)} palindromes found.\n")
    print(*palindromes, sep=", ")


def open_file(file: str) -> list:
    """Open text file and return a list of words."""
    try:
        with open(file, "r", encoding="utf-8") as word_file:
            word_list: list = word_file.read().lower().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)
    return word_list


def is_pal(word: str) -> bool:
    """Return bool if word str is a palindrome."""
    return word == word[::-1]


if __name__ == "__main__":
    main()
