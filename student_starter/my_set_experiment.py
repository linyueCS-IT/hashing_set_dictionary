from binary_search import binary_search
from time import time_ns
from my_hashing_experiment import my_hash


class WordList_NoOptimization:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        fh = open(filename, "r")
        self._list = [line for line in map(str.strip, fh)]
        fh.close()

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_NoOptimization("wordlist.txt")
        if word in all_words:
        """

        # Since list is not a hash structure,
        # in needs to be traversed from beginning to end, and the time complexity is O(n).
        return value in self._list


class WordList_BinarySearch:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        # Way1
        # fh = open (filename,"r")
        # self._list = []
        # for line in fh:
        #     line = line.strip()
        #     self._list.append(line)
        # fh.close()

        # Way2
        with open(filename,"r") as fh:
            self._list = [line for line in map(str.strip,fh)]

        # Way3
        # with open(filename,"r") as fh:
        #     self._list = [line.strip() for line in fh]

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_BinarySearch("wordlist.txt")
        if word in all_words:
        """


class WordList_WithHash:
    def __init__(self, filename):
        """Reads words from filename and stores them"""

    def _hash(self, key: str) -> int:
        """convert key into an integer"""

    def __contains__(self, value: str):
        """
        function that allows this class to use:

        all_words = WordList_WithHash("wordlist.txt")
        if word in all_words:
        """


# =============================================================================
# time it
# =============================================================================
if __name__ == "__main__":
    print(f"{"init":>10}   "
          f"{"search":>10}   "
          f"{"total":>10}   "
          "class")

    for search_class in (
            WordList_NoOptimization,
            WordList_BinarySearch,
            WordList_WithHash,
    ):
        fh_words_to_find = open("words_to_find.txt", "r")

        now_all = time_ns()
        all_words = search_class("wordlist.txt")
        contained = 0
        setup_time = (time_ns() - now_all) / 1_000_000_000

        now_search_only = time_ns()
        for word in map(str.strip, fh_words_to_find):
            if word in all_words:
                contained += 1
        total_time = (time_ns() - now_all) / 1_000_000_000
        search_time = (time_ns() - now_search_only) / 1_000_000_000
        print(f"{setup_time:10.5f}   "
              f"{search_time:10.5f}   "
              f"{total_time:10.5f}   "
              f"{search_class.__name__}")
