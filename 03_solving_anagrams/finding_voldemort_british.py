"""TBA."""

from collections import Counter
from itertools import permutations
import sys
import time


def main():
    """TBA."""
    start = time.time()
    name = "tmvoordle"
    # name = input("Input letters to make up a proper noun: ").lower()
    dict_file = "words_2of4brif.txt"
    word_list = open_file(dict_file)
    trigram_file = "least-likely_trigrams.txt"
    trigram_list = open_file(trigram_file)
    # Filter words to match name length
    word_list_filt_len = list(
        filter(lambda word: len(word) == len(name), [word.lower() for word in word_list]))
    word_list_cv = map_cv(word_list_filt_len)
    reduction_percentage = .05
    word_list_cv = reduce_cv_maps(word_list_cv, reduction_percentage)
    name_permutations = [''.join(perm) for perm in permutations(name)]
    name_permutations = list(set(name_permutations))  # Remove duplicates
    # Find permutations of name that match cv pattern of word list
    names_filt_cv = [perm for perm in name_permutations if map_cv([perm])[
        0] in word_list_cv]  # Hacky way to send individual strings to function that expects list
    names_filt_trigram = filter_trigrams(names_filt_cv, trigram_list)
    names_filt_digram = filter_digrams(names_filt_trigram)
    print(len(names_filt_digram))
    first_letters = set([word[0] for word in names_filt_digram])
    while True:
        choice = input(f"{first_letters} Choose a first letter: ")
        print([word for word in names_filt_digram if word.startswith(choice)])


def filter_trigrams(word_list, trigram_list):
    unlikely_names = set()
    word_list = set(word_list)
    for trigram in trigram_list:
        for name in word_list - unlikely_names:
            if trigram in name:
                unlikely_names.add(name)
    return list(word_list - unlikely_names)


def filter_digrams(word_list):
    rejected_words = set()
    word_list = set(word_list)
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt',
               'mv', 'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv',
                          'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for reject in rejects:
        for name in word_list - rejected_words:
            if reject in name:
                rejected_words.add(name)
    for reject in first_pair_rejects:
        for name in word_list - rejected_words:
            if name.startswith(reject):
                rejected_words.add(name)
    return list(word_list - rejected_words)


def map_cv(word_list) -> list[str]:
    vowels = "aeiouy"
    cv_maps = []
    for word in word_list:
        map = ""
        for char in word:
            if char in vowels:
                map += "v"
            else:
                map += "c"
        cv_maps.append(map)
    return cv_maps


def reduce_cv_maps(cv_maps, reduction_percentage) -> list[str]:
    cv_set = set(cv_maps)
    retain_int = len(cv_set) - int(len(cv_set)*reduction_percentage)
    cv_maps_retained = [cv_map[0]
                        for cv_map in Counter(cv_maps).most_common(retain_int)]
    return cv_maps_retained


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
