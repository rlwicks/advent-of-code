import sys
from typing import Optional


TEXT_DIGITS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def process_line(line: str, include_text_digits: bool) -> int:
    i = 0
    first = None
    last = None
    dig = None
    while i < len(line):
        start_i = i
        if line[i].isdigit():
            dig = int(line[i])
        if include_text_digits:
            for d, text_d in TEXT_DIGITS.items():
                if i + len(text_d) > len(line):
                    continue
                if line[i : i + len(text_d)] == text_d:
                    dig = d
                    break
        i = i + 1
        last = dig
        if first is None:
            first = dig
        # print("{}: {} | {}, {} | {}".format(start_i, dig, first, last, line[start_i:]))
    return (first if first is not None else 0) * 10 + (last if last is not None else 0)


f = open(sys.argv[1], "r")
lines = f.readlines()
sum_p1 = 0
sum_p2 = 0
for line in lines:
    standardized_line = line.strip().lower()
    # print(line.strip())
    val1 = process_line(standardized_line, False)
    val2 = process_line(standardized_line, True)
    sum_p1 = sum_p1 + val1
    sum_p2 = sum_p2 + val2
    # print("{} gives {}, new sum {}\n".format(line.strip(), val, sum))

print("Part 1, calibrations sum: " + str(sum_p1))
print("Part 2, calibrations sum: " + str(sum_p2))
