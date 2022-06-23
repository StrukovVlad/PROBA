import itertools

with open(r'C:\Users\Влад\Desktop\re.txt') as f:
    header = itertools.islice(f, 5)

    for line in header:
        print(line, end='')

