import pygame
import numpy as np
import random
class Grid:
    def __init__(self,width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = random.randint(0,1)

    def Conway(self, off_color, on_color, surface):
        for i in range(self.rows):
            for j in range(self.columns):
                j_pos = j * self.scale
                i_pos = i * self.scale

                if self.grid_array[i][j] == 1:
                    pygame.draw.rect(surface, on_color, [i_pos,j_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [i_pos, j_pos, self.scale - self.offset, self.scale - self.offset])
        next = np.ndarray(shape=(self.size))

        for i in range(self.rows):
            for j in range(self.columns):
                cellstate = self.grid_array[i][j]
                neighbourstate = self.get_neighbour(i,j)
                # 1.Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # 2.Any live cell with two or three live neighbours lives on to the next generation.
                # 3.Any live cell with more than three live neighbours dies, as if by overpopulation.
                # 4.Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


                if cellstate == 0 and neighbourstate == 3: #condition 4
                    next[i][j] = 1
                elif cellstate == 1 and (neighbourstate < 2 or neighbourstate > 3): #condition 1 and 3
                    next[i][j] = 0
                else: #condition 2
                    next[i][j] = cellstate
        self.grid_array = next

    def get_neighbour(self,x,y):
        total = 0
        for i in range(-1,2):
            for j in range(-1,2):
                x_edge = (x+i+self.rows) % self.rows
                y_edge = (y+j+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
