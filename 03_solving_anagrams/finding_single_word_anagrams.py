"""Find single-word anagrams within a word list."""
from collections import defaultdict
import sys
import time
import logger

FILE_PATH: str = "words_2of4brif.txt"
ANAGRAM_PATH: str = "anagrams.txt"


def main():
    """Find single-word anagrams within a word list."""
    # Read dictionary file.
    word_list: list[str] = open_file(FILE_PATH)

    # Make anagram dict from list
    start_time = time.time()
    anagrams: dict[str, list] = catalog_anagrams(word_list)
    logger.log.info("Runtime for catalog_anagrams was %s seconds.",
                    str(time.time() - start_time))

    # Write anagram dict to file.
    write_file(ANAGRAM_PATH, anagrams)


def catalog_anagrams(word_list: list) -> dict:
    """TBA."""
    # Init anagram dict of list of str.
    anagrams: dict[str, list[str]] = defaultdict(
        lambda: [])  # Empty list as value
    # Key is sorted(word). Value is list of matching anagrams.
    for word in word_list:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams


def open_file(file: str) -> list:
    """Open text file and return a list of words."""
    try:
        with open(file, "r", encoding="utf-8") as word_file:
            word_list: list = word_file.read().lower().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)
    return word_list


def write_file(file: str, anagrams: dict) -> None:
    """Write dictionary of lists of found anagrams."""
    with open(file, 'w', encoding="utf-8") as _f:
        for key, value in anagrams.items():
            _f.write(f"{key:<15} {', '.join(value)}\n")


if __name__ == "__main__":
    main()
