"""Find palindromes and palingrams within a word list."""
import sys
import time
import logger

FILE_PATH: str = "words_2of4brif.txt"
PALINGRAM_PATH: str = "palingrams.txt"


def main():
    """Find palindromes and palingrams within a word list."""
    start_time = time.time()

    # Read dictionary file.
    word_list: list = open_file(FILE_PATH)
    word_set: set = set(word_list)

    # Init palingram dict of list of str.
    # Key is core word. Value is list containing found palingrams.
    palingrams: dict = {}

    # Send each word through palingram algorithm and append if found.
    for word in word_list:
        found_palingram: list = pal_gram_algo(word, word_set)
        if found_palingram:
            palingrams[word] = found_palingram

    # Write palingram dict to file.
    write_file(PALINGRAM_PATH, palingrams)
    logger.log.info("Runtime for pal_gram_algo rev 4 was %s seconds.",
                    str(time.time() - start_time))
    logger.log.info("Found %s words with palindromes or palingrams from %s",
                    str(len(palingrams)), FILE_PATH)


def pal_gram_algo(word: str, word_set: set) -> list:
    """Find palindromes and two-word palingrams.

    Args:
        word (str): word to process
        word_set (set): words for validation test

    Returns:
        list: found palindromes and two-word palingrams
    """
    pals = []

    # Check for single word palindrome.
    if is_pal(word):
        pals.append(word)

    # Search word forward.
    for _i in range(1, len(word)):
        segment1 = word[:_i]
        segment2 = word[_i:]
        if segment1[::-1] in word_set and is_pal(segment2):
            pals.append(f"{word} {segment1[::-1]}")

    # Search word reversed.
    for _i in range(len(word)-1):
        segment1 = word[:_i:-1]  # Word is reversed.
        segment2 = word[_i::-1]  # Word is reversed.
        if segment1 in word_set and is_pal(segment2):
            pals.append(f"{segment1} {word}")

    return pals


def is_pal(word: str) -> bool:
    """Return bool if word str is a palindrome."""
    return word == word[::-1]


def open_file(file: str) -> list:
    """Open text file and return a list of words."""
    try:
        with open(file, "r", encoding="utf-8") as word_file:
            word_list: list = word_file.read().lower().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)
    return word_list


def write_file(file: str, palingrams: dict) -> None:
    """Write dictionary of lists of found palingrams."""
    with open(file, 'w', encoding="utf-8") as _f:
        for key, value in palingrams.items():
            _f.write(f"{key:<15} {', '.join(value)}\n")


if __name__ == "__main__":
    main()
