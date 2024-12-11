import random
from typing import List

class Crossword:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.words = []

    def add_word(self, word: str, row: int, col: int, direction: str) -> bool:
        """
        Add a word to the grid in the specified direction if it fits.
        direction: 'H' for horizontal, 'V' for vertical.
        """
        if direction == 'H':
            if col + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] not in (' ', word[i]):
                    return False
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]

        elif direction == 'V':
            if row + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] not in (' ', word[i]):
                    return False
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]
        else:
            return False

        self.words.append(word)
        return True

    def display(self):
        """Display the crossword grid."""
        for row in self.grid:
            print(' '.join(row))

    def is_valid_position(self, word: str, row: int, col: int, direction: str) -> bool:
        """Check if a word can be placed at the given position."""
        if direction == 'H':
            if col + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] not in (' ', word[i]):
                    return False
        elif direction == 'V':
            if row + len(word) > self.size:
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] not in (' ', word[i]):
                    return False
        else:
            return False
        return True

    def solve(self, words: List[str]) -> bool:
        """Attempt to solve the crossword by placing all words."""
        if not words:
            return True

        word = words[0]
        for row in range(self.size):
            for col in range(self.size):
                for direction in ('H', 'V'):
                    if self.is_valid_position(word, row, col, direction):
                        self.add_word(word, row, col, direction)
                        if self.solve(words[1:]):
                            return True
                        self.remove_word(word, row, col, direction)
        return False

    def remove_word(self, word: str, row: int, col: int, direction: str):
        """Remove a word from the grid."""
        if direction == 'H':
            for i in range(len(word)):
                self.grid[row][col + i] = ' '
        elif direction == 'V':
            for i in range(len(word)):
                self.grid[row + i][col] = ' '

def main():
    size = 10
    words = ["apple", "banana", "grape", "orange", "peach"]
    random.shuffle(words)

    crossword = Crossword(size)
    success = crossword.solve(words)

    if success:
        print("Crossword Puzzle Generated Successfully:")
        crossword.display()
    else:
        print("Failed to generate a crossword puzzle.")

if __name__ == "__main__":
    main()
