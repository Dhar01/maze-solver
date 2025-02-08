from cell import Cell
from time import sleep
from graphics import Window

class Maze:
    def __init__(
        self,
        x1: int, # starting point of the maze - horizontal
        y1: int, # starting point of the maze - vertical
        num_rows: int, # max number of rows
        num_cols: int, # max number of cols
        cell_size_x: int, # size of cell - horizontal
        cell_size_y: int, # size of cell - vertical
        win: Window | None = None
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = None
        self.__cells = []
        self._create_cells()

    def _create_cells(self) -> None:
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) -> None:
        """
        i is the cell position to x
        j is the cell position to y
        """
        if self.__win is None:
            return

        x1 = self.__x1 + (i * self.__cell_size_x)
        y1 = self.__y1 + (j * self.__cell_size_y)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        self.__cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self.__win is None:
            return

        self.__win.redraw()
        sleep(0.05)

    def get_cells(self):
        return self.__cells
