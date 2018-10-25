"""
I like parentheticals (a lot).

“Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.”

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of
the first parenthesis), the output should be 79 (position of the last parenthesis).

"""
from itertools import islice


def find_match_close(string, open_position):
    nested_count = 0

    for pos, char in enumerate(
            islice(string, open_position + 1, None), start=open_position + 1):
        if char == '(':
            # start of a new parenthetical block
            nested_count += 1
        elif nested_count and char == ')':
            # end of a parenthetical block
            nested_count -= 1
        elif not nested_count and char == ')':
            # matching end parenthesis
            return pos
    else:
        raise RuntimeError('Didn\'t find closing parenthesis!')


test_string = (
    'Sometimes (when I nest them (my parentheticals) '
    'too much (like this (and this))) they get confusing.'
)

print(find_match_close(test_string, 10), 'expected', 79)
print(find_match_close(test_string, 28), 'expected', 46)
print(find_match_close(test_string, 57), 'expected', 78)
