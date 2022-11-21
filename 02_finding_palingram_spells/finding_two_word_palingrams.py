"""TBA."""
import sys

FILE_PATH: str = "inventwithpython_dictionary.txt"
PALINGRAM_PATH: str = "palingrams.txt"


def main():
    """TBA."""
    # Read dictionary file
    word_list: list = open_file(FILE_PATH)

    # Init palingram dict of lists of str
    # Key is core word. Value is list containing found palingram strings
    palingrams = {}
    for word in word_list:
        found_palingram = pal_gram_algo(word, word_list)
        if found_palingram:
            palingrams[word] = found_palingram

    # Write palingram dict to file
    write_file(PALINGRAM_PATH, palingrams)


def pal_gram_algo(word: str, word_list: list) -> list:
    """TBA."""
    pals = []
    # mirror = [word, word[::-1]]  # To test word forward and reversed
    if is_pal(word):  # Single word palindrome
        pals.append(word)
    # Search word forward
    for _i in range(1, len(word)):
        segment1 = word[:_i]
        segment2 = word[_i:]
        # print(segment1, segment2)
        if segment1[::-1] in word_list and is_pal(segment2):
            pals.append(f"{word} {segment1[::-1]}")
    # Search word reversed
    for _i in range(len(word)-1):
        segment1 = word[:_i:-1]
        segment2 = word[_i::-1]
        # print(segment1, segment2)
        if segment1 in word_list and is_pal(segment2):
            pals.append(f"{segment1} {word}")

    return pals


def write_file(file: str, palingrams: dict) -> None:
    """TBA."""
    with open(file, 'w', encoding="utf-8") as _f:
        for key, value in palingrams.items():
            _f.write(f"{key:<15} {', '.join(value)}\n")


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
