from typing import Any, List


# Things to do:
# - append
# - delete
# - _resize
# - _create an arary
# - if the array is complete, double the capacity
# - have a capacity, length, and the data holded


class Array:
    def __init__(self) -> None:
        self.capacity: int = 1  # total slots
        self.length: int = 0  # used slots
        self.data: List[Any] = self._make_array(self.capacity)  # data in slots

    def _make_array(self, size) -> List[Any]:
        """Create an empty array of fixed size initialise to None"""
        return [None] * size

    def _resize(self, new_size) -> None:
        new_array = self._make_array(new_size)
        for i in range(self.length):
            new_array[i] = self.data[i]
        self.capacity = new_size
        self.data = new_array

    def append(self, item: Any) -> None:
        if self.length >= self.capacity:
            self._resize(self.capacity * 2)  # double capacity
        self.data[self.length] = item
        self.length += 1

    def delete(self, index: int) -> None:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.length - 1] = None
        self.length -= 1

    def get(self, index) -> Any:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.data[index]

    # rewritting the len method
    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return f"Test Array({self.data[: self.length]})"
