class Matrix:
    def __init__(self, list):
        self.matrix_list = list


    def __str__(self):
        matrix_lines = []
        for i in self.matrix_list:
            line = ' '.join([str(number) for number in i])
            matrix_lines.append(line)

        matrix_print = '\n'.join([str(line) for line in matrix_lines])
        return matrix_print


    def __add__(self, other):
        for num_line, line in enumerate(self.matrix_list, start=0):
            zippped_lists = zip(line, other.matrix_list[num_line])
            sum = [x + y for (x, y) in zippped_lists]
            self.matrix_list[num_line] = sum


matrix1 = Matrix([[1, 2, 3],[2, 4, 1], [1, 3 ,2]])
matrix2 = Matrix([[1, 2, 3],[2, 4, 1], [1, 3 ,2]])
matrix1 + matrix2
print(matrix1)