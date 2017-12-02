######################################################################
# Author: Will Romano
# username: romanow

# Assignment: Final Project
# Purpose: Class for a matrix in cellular automation

######################################################################


class Matrix:
    def __init__(self, width, height):

        # 0 empty (black),
        # 1 electron head (blue),
        # 2 electron tail (red),
        # 3 conductor (yellow).

        self.matrix = []
        self.width = width
        self.height = height

        for i in range(self.height):
            temp_rowlist = []
            for j in range(self.width):
                temp_rowlist.append(0)
            self.matrix.append(temp_rowlist)

    def term_display(self):
        """
        Displays the current matrix to the terminal for debugging purposes
        :return: None
        """
        print("")
        for row in self.matrix:
            for col in row:
                if col == 0:
                    print(col, end="")
                elif col == 1:
                    print("\033[34m" + "\033[1m" + str(col) + "\033[0m", end="")
                elif col == 2:
                    print("\033[31m" + "\033[1m" + str(col) + "\033[0m", end="")
                elif col == 3:
                    print("\033[92m" + "\033[1m" + str(col) + "\033[0m", end="")
            print("")

    def _is_electron(self, location):
        """
        Finds the number of neighboring electrons and returns True if there are one or two
        :param location: The location in the matrix to check (represented as a list)
        :return: Returns True or False
        """
        neighbor_count = 0
        try:
            if self.matrix[location[0]][location[1] - 1] == 1:
                neighbor_count += 1
            if self.matrix[location[0] - 1][location[1] - 1] == 1:
                neighbor_count += 1
            if self.matrix[location[0] - 1][location[1]] == 1:
                neighbor_count += 1
            if self.matrix[location[0] - 1][location[1] + 1] == 1:
                neighbor_count += 1
            if self.matrix[location[0]][location[1] + 1] == 1:
                neighbor_count += 1
            if self.matrix[location[0] + 1][location[1] + 1] == 1:
                neighbor_count += 1
            if self.matrix[location[0] + 1][location[1]] == 1:
                neighbor_count += 1
            if self.matrix[location[0] + 1][location[1] - 1] == 1:
                neighbor_count += 1
        except IndexError:
            pass

        if neighbor_count == 1 or neighbor_count == 2:
            return True
        else:
            return False

    def generation_progress(self):
        """
        Progress to the next generation of the matrix
        :return: None
        """
        next_matrix = []
        for row in range(len(self.matrix)):
            temp_rowlist = []
            for col in range(len(self.matrix[0])):
                if self.matrix[row][col] == 0:
                    temp_rowlist.append(0)
                if self.matrix[row][col] == 1:
                    temp_rowlist.append(2)
                elif self.matrix[row][col] == 2:
                    temp_rowlist.append(3)
                elif self.matrix[row][col] == 3 and self._is_electron([row, col]):
                    temp_rowlist.append(1)
                elif self.matrix[row][col] == 3 and not self._is_electron([row, col]):
                    temp_rowlist.append(3)
            next_matrix.append(temp_rowlist)
        self.matrix = next_matrix



