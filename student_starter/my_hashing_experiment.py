import sys
from io import StringIO
from report import print_table

OUTPUT_TO_FILE = False

def my_hash(key: str, number_of_buckets: int) -> int:
    # return 0
    # return len(key) % number_of_buckets
    h = 0
    for c in key:
        h = h * 10 + (ord(c) - ord("a"))
    return h % number_of_buckets

def main():
    names: list[str]
    with open("names.txt", "r") as names_file:
        names = list(map(str.strip, names_file))

    if OUTPUT_TO_FILE:
        sys.stdout = StringIO()

    for number_of_buckets in [7, 19, 53, 101]:
        # create buckets
        buckets: list[list[str]] = []
        for i in range(number_of_buckets):
            buckets.append([])

        # hash names into buckets
        for name in names:
            bucket: int = my_hash(name, number_of_buckets)
            buckets[bucket].append(name)

        print_table(f"Buckets = {number_of_buckets}", list(map(len, buckets)))

    if OUTPUT_TO_FILE:
        sys.stdout.seek(0)
        with open("report.md", "w") as fh:
            for line in sys.stdout:
                print(line.strip(), file=fh)
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    main()
    # print(my_hash("rat", 100))
