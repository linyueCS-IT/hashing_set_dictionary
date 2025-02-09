from typing import Any

KEY_VALUE = tuple[str, Any]


class MyDictionary:
    def __init__(self, filename):
        """read in a list of words, set translation of word to "None" """

    def _hash(self, key: str) -> int:
        """convert key into an integer"""

    def get_value(self, word: str) -> Any:
        """
        gets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """

    def set_value(self, word: str, description: Any):
        """
        sets the description for 'word'
        raises 'KeyError' if word is not found in your dictionary
        """

    def __contains__(self, key: str):
        """
        function that allows this class to use:
        'if word in my_dictionary:'
        """


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
