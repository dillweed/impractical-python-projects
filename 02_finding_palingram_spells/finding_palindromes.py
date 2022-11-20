"""TBA."""
import sys

FILE_PATH: str = "inventwithpython_dictionary.txt"


def main():
    """TBA."""
    # Read dictionary file
    word_list: list = open_file(FILE_PATH)

    # Make a list of palindromes
    palindromes: list = []
    for word in word_list:
        if is_pal(word):
            palindromes.append(word)

    # Print palindrome list
    print(f"\n{len(palindromes)} palindromes found.\n\n", palindromes)


def open_file(file: str) -> list:
    """Open file and return list of lines in lowercase.

    Args:
        FILE_PATH (str): The spelling dictionary file

    Returns:
        words (list): Word list in lowercase
    """
    # Read dictionary file with try block
    try:
        with open(file, "r", encoding="utf-8") as word_file:
            word_list: list = word_file.read().lower().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)
    return word_list


def is_pal(word: str) -> bool:
    """Return bool if word is a palindrome.

    Args:
        word (str): Word to test

    Returns:
        bool: True if word is a palindrome
    """
    return word == word[::-1]


if __name__ == "__main__":
    main()
