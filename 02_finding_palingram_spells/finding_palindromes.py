"""TBA"""
import sys


def main():
    """TBA"""
    # Read dictionary file with try block
    try:
        with open("inventwithpython_dictionary.txt", "r", encoding="utf-8") as dict_file:
            spell_dict = dict_file.read().splitlines()

    except IOError as _e:
        print(_e)
        sys.exit(1)

    print(spell_dict)


if __name__ == "__main__":
    main()
