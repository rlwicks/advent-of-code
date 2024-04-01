import sys
import numpy as np
from typing import Optional

"""
We view the problem transposed so that we have the ease 
of working within the same array when sliding north.
"""


def print_field(field):
    for i, row in enumerate(field):
        print(f"{i}: " + "".join(row))
    print()


def propagate_slide(last_j_stop, round_rock_cnt, row, j) -> int:
    load_of_slide = 0
    for k in range(last_j_stop, last_j_stop + round_rock_cnt):
        row[k] = "0"
        load_of_slide = load_of_slide + len(row) - k
    for k in range(last_j_stop + round_rock_cnt, j):
        row[k] = "."
    return load_of_slide


def slide_west(field) -> int:
    load_sum = 0
    for i, row in enumerate(field_t):
        j = 0
        round_rock_cnt = 0
        last_j_stop = 0
        while j < len(row):
            if row[j] == "O":
                round_rock_cnt = round_rock_cnt + 1
            elif row[j] == "#":
                load_of_slide = propagate_slide(last_j_stop, round_rock_cnt, row, j)
                load_sum = load_sum + load_of_slide
                last_j_stop = j + 1
                round_rock_cnt = 0
                # print_field(field_t.transpose())

            # noop on "."
            j = j + 1
        load_of_slide = propagate_slide(last_j_stop, round_rock_cnt, row, j)
        load_sum = load_sum + load_of_slide
        # print_field(field_t.transpose())
    return load_sum


f = open(sys.argv[1], "r")
lines = [list(l.strip()) for l in f.readlines()]
field_t = np.array(lines)
field_t = field_t.transpose()
print("Untransposed:")
print_field(field_t.transpose())
load = slide_west(field_t)  # Sliding north is equivalent to sliding the transpose west.
print("Untransposed:")
print_field(field_t.transpose())
print(load)
