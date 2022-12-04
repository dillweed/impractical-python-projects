"""TBA."""

from collections import Counter
import sys
import logger

FILE_PATH: str = "words_2of4brif.txt"


def main():
    """Find anagram phrases with user interaction."""

    # Read dictionary file.
    word_list: list[str] = open_file(FILE_PATH)

    # Get name input
    name = input("\nType your full name or 'Q' to quit: ").lower()

    # Find anagram phrase from name
    result = find_phrase(name, word_list)
    print("\n", result, "\n")

    # List unused letters from name
    name_dict = Counter(name)
    name_dict.subtract(Counter(result))
    print(name_dict)


def find_phrase(name: str, word_list: list) -> str:
    """TBA."""
    logger.log.info("Name: %s", name)
    logger.log.info("Name dict: %s", Counter(name))
    phrase = ""
    name_dict = Counter(name)  # Dict of letter quantities
    while True:
        options: list = find_options(name_dict, word_list)
        while options:
            # offer first item from options list
            print(f"\nName: {name}, \nPhrase: {phrase}\n")
            response = input(f"Use \"{options[0]}\"? y n or q: ").lower()
            if response == 'y':  # Add this word to the phrase
                phrase = f"{phrase} {options[0]}".strip()
                # Reduce name_dict by new word values
                name_dict.subtract(Counter(options[0]))
                break
            if response == 'n':  # Remove the option
                options.pop(0)
            if response == 'q':  # Quit
                sys.exit("bye")
            logger.log.info("Phrase: %s", phrase)
        if not options:  # return phrase when no options remain
            return phrase


def find_options(name_dict: dict, word_list: list) -> list:
    """Return a list of words that fit inside name_dict."""
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
    # Sort word list with longest first
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
