######################################################################
# Author: Will Romano
# username: romanow

# Assignment: Final Project
# Purpose: Class for a matrix in cellular automation

######################################################################


class Matrix:
    def __init__(self, width, height):
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
        print("\033[92m")
        print(self.height, self.width)
        print(self.matrix)
        for col in range(self.height):
            tmp_str = ""
            for row in range(self.width):
                tmp_str += str(self.matrix[row][col]) + " "
            print(tmp_str)
        print("\033[0m")
