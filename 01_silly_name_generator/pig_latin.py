"""
Convert input to pig-latin.

To form Pig Latin, you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the word.
"""
# TODO preserve punctuation.
# TODO add edge rule for words with no vowel but 'y' like 'my'.


def main() -> None:
    """Convert input to pig-latin."""
    print("\n" + convert_to_pig_latin(get_input()) + "\n")


def get_input() -> str:
    """Ask for input.

    Returns:
        str: User input text
    """
    input_text: str = input("Type a sentence: ")
    return input_text


def convert_to_pig_latin(input_text: str) -> str:
    """Convert text to pig-latin.

    Args:
        input_text (str): User input text

    Returns:
        str: Converted text to pig-latin
    """
    vowels: str = "aeiouAEIOU"
    pig_latin: list[str] = []

    # Convert non-alpha characters to spaces
    cleaned_text: str = "".join(
        [c if c.isalpha() else " " for c in input_text])
    # Split words to list
    words: list = cleaned_text.split()
    # For each word, split on index of first vowel char
    for word in words:
        swap_index: int = 0  # Position of first vowel char
        for i, c in enumerate(word):
            if c in vowels:
                swap_index = i
                break
        if swap_index:  # If word begins with a consonant
            translated_word: str = f"{word[swap_index:]}{word[:swap_index]}ay"
            pig_latin.append(translated_word)
        else:  # Word begins with a vowel
            pig_latin.append(f"{word}way")

    return " ".join(pig_latin)


if __name__ == "__main__":
    main()
