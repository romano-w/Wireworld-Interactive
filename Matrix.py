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

    def _num_neighbors(self):
        """
        Finds the number of neighbors for a given cell.
        :return: Returns an int
        """
        






