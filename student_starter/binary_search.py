from __future__ import annotations

from typing import TypeVar, Generic, Protocol, Optional


class Comparable(Protocol):

    def __lt__(self, other) -> bool:
        pass

    def __eq__(self, other) -> bool:
        pass


def binary_search(arr: list[Comparable], low: int, high: int, value: Comparable) -> Optional[int]:
    """
    does a binary search for value in arr.
    :param arr: a sorted! array of type OurArray
    :param low: the lowest index to search from
    :param high: the highest index to search to
    :param value: the value that you are looking for
    :return: the index of the value in the array, if it exists,
            otherwise, None
    """
    left: int = low
    right: int = high
    mid: int = 0
    while left <= right:
        mid = (left + right) // 2
        if value == arr[mid]:
            return mid
        elif value < arr[mid]:
            right = mid - 1
        else:
            mid += 1
            left = mid

    # couldn't find it
    return None