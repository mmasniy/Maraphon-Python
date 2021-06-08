from re import sub


def clear_words(line):
    return list(map(lambda word: sub(r"[?!.,;:-]", "", word), line.split()))

#
# if __name__ == "__main__":
#
#     text_example_1 = 'WOMAN: Yes?, ENCYCLOPEDIA SALESMAN: Burglar, madam. WOMAN: ' \
#                      'Are you an encyclopaedia salesman?'
#
#     text_example_2 = 'ENCYCLOPEDIA SALESMAN: No madam, I\'m a burglar, ' \
#                      'I burgle people. WOMAN: I think you\'re an encyclopaedia' \
#                      'salesman.'
#
#     text_example_3 = 'ENCYCLOPEDIA SALESMAN: Oh I\'m not, open the door, ' \
#                      'let me in please. WOMAN: If I let you in, you\'ll sell' \
#                      'me encyclopedias.'
#
#     print(clear_words(text_example_1))
#     print(clear_words(text_example_2))
#     print(clear_words(text_example_3))
#
#
#
