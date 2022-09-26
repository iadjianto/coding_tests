# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:17:16 2022

@author: isaia

Finding the dominant cell, where the center integer is higher in value than all its direct neighbours, including its neighbours.
For a given grid of integers, print off how many dominant cells are in the grid.
"""

def vectors_for_neighbours(): # Helper function to get all possible vectors for neighbours
    vectors = []
    steps = [-1,0,1]
    for i in steps:
        for j in steps:
            if i == 0 and j == 0:
                continue
            else:
                vectors.append((i,j))
    return vectors

"""
INPUT: grid of numbers
Find all neighbours for all elements in the grid

OUTPUT: For each element, attach a list of neighbouring cells
"""
def grid_neighbour_finder(grid):
    n = len(grid)
    try:
        m = len(grid[0])
    except TypeError:
        grid = grid.append(grid)
        m = len(grid[0])
    faux_graph = []
    vectors = vectors_for_neighbours()
    for i in range(n):
        for j in range(m):
            neighbours = []
            for k in vectors:
                if i + k[0]>=0 and j+k[1]>=0 and i + k[0] < n and j+k[1] < m: #deals with border of grids
                    neighbours.append(grid[i+k[0]][j+k[1]])
            faux_graph.append((grid[i][j], neighbours))
    return faux_graph

def finding_dominant_cells(grid): # function that counts all dominant cells
    neighbourly = grid_neighbour_finder(grid)
    counter = 0
    for i in range(len(neighbourly)):
        if neighbourly[i][0] > max(neighbourly[i][1]): # condition: if the center of the evaluated cell within the grid is greater than all its neighbours
            # print(neighbourly[i][0])
            counter +=1
    
    print(counter)

# grid = [[1,2,7],\
#         [4,5,6],\
#         [8,8,9]]

# grid = [[1,2,2,1]]

grid = [[9,1,1],\
        [1,1,9],\
        [9,1,1],\
        [1,1,9]]

finding_dominant_cells(grid)
