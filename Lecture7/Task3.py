class Cell:
    def __init__(self, quantity):
        self.total_cells = quantity

    def __add__(self, other):
        return self.total_cells + other.total_cells

    def __sub__(self, other):
        if self.total_cells - other.total_cells > 0:
            return self.total_cells - other.total_cells
        else:
            print('Error')

    def __mul__(self, other):
        return self.total_cells * other.total_cells

    def __truediv__(self, other):
        return int(self.total_cells / other.total_cells)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.total_cells // rows)]) + '\n' + '*' * (self.total_cells % rows)


cell1 = Cell(200)
cell2 = Cell(12)
cell3 = cell1 / cell2
print(cell3)
print(cell2.make_order(3))