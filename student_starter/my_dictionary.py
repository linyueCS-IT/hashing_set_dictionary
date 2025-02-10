from typing import Any
from my_hashing_experiment import my_hash
KEY_VALUE = tuple[str, Any]

class MyDictionary:
    def __init__(self, filename):
        """read in a list of words, set translation of word to "None" """

        self._bucket_number = 2**10
        self._hash_table : list[list] = [[] for _ in range(self._bucket_number)]

        with open(filename, "r") as fh:
            for word in map (str.strip,fh):
                dictionary_item = (word, "")
                bucket_index = self._hash(word)
                self._hash_table[bucket_index].append(dictionary_item)

    def _hash(self, key: str) -> int:
        """convert key into an integer"""
        return my_hash(key, self._bucket_number)

    def get_value(self, word: str) -> Any:
        """
        gets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """
        bucket_index = self._hash(word)
        for key, translation  in self._hash_table[bucket_index]:
            if key == word:
                return translation
        raise KeyError(f"{word} not found")

    def set_value(self, word: str, description: Any):
        """
        sets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """
        bucket_index = self._hash(word)
        for i, key_value in enumerate(self._hash_table[bucket_index]):
            if key_value[0] == word:
                # key_value is tuple, it is immutable, so doesn't change value
                # key_value[1] = description
                # create new tuple assign
                self._hash_table[bucket_index][i] = (word, description)
                return
        raise KeyError(f"{word} not found")

    def __contains__(self, key: str):
        """
        function that allows this class to use:
        'if word in my_dictionary:'
        """
        bucket_index = self._hash(key)
        for word, description in self._hash_table[bucket_index]:
            if word == key:
                return True
        return False

# =============================================================================
# validation
# =============================================================================
if __name__ == "__main__":

    my_dict = MyDictionary("wordlist.txt")

    print("Test Getting Values:")
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        print(f"Current description of {this_word} is '{my_dict.get_value(this_word)}'")

    print()
    print("Test Setting Values:")
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        value = input(f"Enter description for {this_word}: ")
        my_dict.set_value(this_word, value)

    print()
    for this_word in ("tennessee", "exploit", "sagitta", "printer"):
        print(f"Updated description of {this_word} is '{my_dict.get_value(this_word)}'")
