"""Run palingram search against multiple word lists."""
import finding_two_word_palingrams

word_lists = ["words_2of4brif.txt", "words_inventwithpython.txt",
              "words_jlawler.txt", "words_thinkpython2.txt"]

for word_list in word_lists:
    finding_two_word_palingrams.FILE_PATH = word_list
    finding_two_word_palingrams.PALINGRAM_PATH = "palingrams_" + word_list
    finding_two_word_palingrams.main()
