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
        self._list.sort()

        # Way3
        # with open(filename,"r") as fh:
        #     self._list = [line.strip() for line in fh]

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_BinarySearch("wordlist.txt")
        if word in all_words:
        """
        index = binary_search(self._list, 0, len(self._list) - 1, value)
        return index is not None


class WordList_WithHash:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        self._bucket_number = 1000
        self._hash_table = [[] for _ in range(self._bucket_number)]

        with open(filename,"r") as fh:
            for line in map(str.strip,fh):
                if line:
                    bucket_index = my_hash(line,self._bucket_number)
                    self._hash_table[bucket_index].append(line)

    def _hash(self, key: str) -> int:
        """convert key into an integer"""
        return my_hash(key, self._bucket_number)

    def __contains__(self, value: str):
        """
        function that allows this class to use:

        all_words = WordList_WithHash("wordlist.txt")
        if word in all_words:
        """
        bucket_index = self._hash(value)
        # self._hash_table[bucket_index] is not a single value, but a list of multiple values!
        return  value in self._hash_table[bucket_index]


# =============================================================================
# time it
# =============================================================================
# if __name__ == "__main__":
#     print(f"{"init":>10}   "
#           f"{"search":>10}   "
#           f"{"total":>10}   "
#           "class")
#
#     for search_class in (
#             WordList_NoOptimization,
#             WordList_BinarySearch,
#             WordList_WithHash,
#     ):
#         fh_words_to_find = open("words_to_find.txt", "r")
#
#         now_all = time_ns()
#         all_words = search_class("wordlist.txt")
#         contained = 0
#         setup_time = (time_ns() - now_all) / 1_000_000_000
#
#         now_search_only = time_ns()
#         for word in map(str.strip, fh_words_to_find):
#             if word in all_words:
#                 contained += 1
#         total_time = (time_ns() - now_all) / 1_000_000_000
#         search_time = (time_ns() - now_search_only) / 1_000_000_000
#         fh_words_to_find.close()
#         print(f"{setup_time:10.5f}   "
#               f"{search_time:10.5f}   "
#               f"{total_time:10.5f}   "
#               f"{search_class.__name__}")

if __name__ == "__main__":
    # 先测试文件内容
    print("Testing file contents:")
    with open("wordlist.txt", 'r') as f:
        word_count = sum(1 for _ in f)
    print(f"wordlist.txt contains {word_count} words")

    with open("words_to_find.txt", 'r') as f:
        find_count = sum(1 for _ in f)
    print(f"words_to_find.txt contains {find_count} words")

    print("\nStarting performance tests:")
    print(f"{'init':>10}   "
          f"{'search':>10}   "
          f"{'total':>10}   "
          "class")

    for search_class in (
            WordList_NoOptimization,
            WordList_BinarySearch,
            WordList_WithHash,
    ):
        print(f"\nTesting {search_class.__name__}")
        fh_words_to_find = open("words_to_find.txt", "r")

        now_all = time_ns()
        all_words = search_class("wordlist.txt")
        contained = 0
        setup_time = (time_ns() - now_all) / 1_000_000_000

        now_search_only = time_ns()
        words_tested = 0
        for word in map(str.strip, fh_words_to_find):
            words_tested += 1
            if words_tested % 1000 == 0:  # 每测试1000个词打印一次进度
                print(f"Tested {words_tested} words...")
            if word in all_words:
                contained += 1

        total_time = (time_ns() - now_all) / 1_000_000_000
        search_time = (time_ns() - now_search_only) / 1_000_000_000
        fh_words_to_find.close()

        print(f"Found {contained} words out of {words_tested} tested")
        print(f"{setup_time:10.5f}   "
              f"{search_time:10.5f}   "
              f"{total_time:10.5f}   "
              f"{search_class.__name__}")