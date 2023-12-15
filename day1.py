#
f = open("day1-input.txt", "r")
lines = f.readlines()
sum = 0
for line in lines:
    first = 0
    last = 0
    for ch in line:
        if ch.isdigit():
            last = int(ch)
            if first == 0:
                first = int(ch)
    sum = sum + first * 10 + last

print(sum)
