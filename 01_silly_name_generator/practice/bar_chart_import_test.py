from bar_chart import get_char_sums, print_sum_chart

with open('text.txt') as f:
    text = f.read()
    print_sum_chart(get_char_sums(text))
