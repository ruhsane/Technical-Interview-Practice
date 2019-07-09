class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.row_dict = self.row_dict()

    def row_dict(self):
        curr_index = 0
        row_dict = {}
        row_num = 1
        digit = ''

        for char in self.matrix_string:
            curr_index += 1

            # if current character is a number, concatinate the number to the string
            if char.isdigit():
                
                digit += char

                # create an array for current row
                if row_num not in row_dict:
                    row_dict[row_num] = []

            # append the number to the row number array if we reached the end of a number
            # (if we see a space, line, or we are at the end of the matrix)
            if char.isdigit() is False or curr_index == len(self.matrix_string):
                if digit != '':
                    row_dict[row_num].append(int(digit))

                # after appending the number, change back the variable to empty for next number to concatinate
                digit = ''

            # if we reached a line break
            if char == "\n" :
                # add one to our current row number
                row_num += 1 
        
        return row_dict

    def row(self, index):
        
        return self.row_dict[index]

    def column(self, index):
        column = []
        for row in self.row_dict:
            column.append(self.row_dict[row][index-1])

        return column
