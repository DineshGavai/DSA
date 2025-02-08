class NumberContainers:

    def __init__(self):
        self.index_map = {} 
        self.number_map = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            if old_number in self.number_map:
                self.number_map[old_number].discard(index)  # Remove index from old number's set
                if not self.number_map[old_number]:  # Remove key if set is empty
                    del self.number_map[old_number]

        # Update index mapping
        self.index_map[index] = number

        # Add index to new number's set
        if number not in self.number_map:
            self.number_map[number] = SortedSet()
        self.number_map[number].add(index)
        

    def find(self, number: int) -> int:
        if number in self.number_map and self.number_map[number]:
            return self.number_map[number][0]  # Return the smallest index
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)