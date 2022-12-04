"""TBA."""

from collections import Counter
import sys
import logger

FILE_PATH: str = "words_2of4brif.txt"


def main():
    """Find anagram phrases with user interaction."""

    # Read dictionary file.
    word_list: list[str] = open_file(FILE_PATH)

    name = input("\nType your full name or 'Q' to quit: ").lower()
    result = find_phrase(name, word_list)
    print("\n", result, "\n")
    name_dict = Counter(name)
    name_dict.subtract(Counter(result))
    print(name_dict)


def find_phrase(name: str, word_list: list) -> str:
    """TBA."""
    logger.log.info("Name: %s", name)
    logger.log.info("Name dict: %s", Counter(name))
    phrase = ""
    name_dict = Counter(name)
    while True:
        options: list = find_options(name_dict, word_list)
        while options:
            # offer first item from options list
            print(f"\nName: {name}, \nPhrase: {phrase}\n")
            response = input(f"Use \"{options[0]}\"? y n or q: ").lower()
            if response == 'y':
                phrase = f"{phrase} {options[0]}".strip()
                name_dict.subtract(Counter(options[0]))
                break
            if response == 'n':
                options.pop(0)
            if response == 'q':
                sys.exit("bye")
            logger.log.info("Phrase: %s", phrase)
        if not options:  # return phrase when no options remain
            return phrase


def find_options(name_dict: dict, word_list: list) -> list:
    """TBA."""
    word_options = []
    for word in word_list:
        flag = False
        word_dict = Counter(word)
        for k, _v in word_dict.items():
            if _v > name_dict[k]:
                flag = True
                break
        if not flag:
            word_options.append(word)
    word_options = sorted(word_options, key=len, reverse=True)
    return word_options


def open_file(file: str) -> list:
    """Open text file and return a list of words."""
    try:
        with open(file, "r", encoding="utf-8") as word_file:
            word_list: list = word_file.read().lower().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)
    return word_list


if __name__ == "__main__":
    main()
