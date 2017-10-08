import time
from random import randint
import logging
from sys import maxsize
from BaseAI_3 import BaseAI

DEPTH = 3

# working minimax backup

class PlayerAI(BaseAI):
    def __init__(self):
        """create and configure logger for file writing"""
        logging.basicConfig(filename="./PlayerAI.log",level=logging.DEBUG)
        self._logger = logging.getLogger()
        self._logger.info("="*90+"\n"+"="*100)
        self._logger.info("Heuristic is: return len(grid.getAvailableCells())")

        """stats that will be used to assess heuristic"""
        self._no_of_moves = 0
        self._no_of_leaves = 0
        self._avg_move_time = 0
        self._move_time = 0
        self._depth_limit = DEPTH
        self._max_move_depth = 0

        self._time = 0 #will be used to cut off the search


    def getMove(self, grid):
        self._max_move_depth = 0
        self._move_time = self._time = time.clock()
        self._no_of_moves+=1
        best_value = maxsize*-1
        for move in grid.getAvailableMoves():
            temp_grid = grid.clone()
            temp_grid.move(move)
            if best_value < self.min(Node(move=move,grid=temp_grid,depth=DEPTH-1)):
                best_move = move

        """ keep track of info in order to assess the heuristic"""
        self._move_time = time.clock() - self._move_time
        self._avg_move_time += self._move_time
        self._logger.info("Move number={}, number of leaves={},max depth{}, time to find={}".format(self._no_of_moves,self._no_of_leaves,self._max_move_depth,self._move_time))

        #Safety net. Will help to identify bugs
        if move is None:
            raise ValueError("MOVE CANNOT BE NONE")
        return move

    def max(self,node):
        """i dont use a seperate is_leaf(node) function to evaluate if the node is a leaf
        because that would require to call the get_children functions twice in a
        min or max node, which is expensive"""
        """checking if the node is a leaf node"""
        if node._depth > self._max_move_depth:
            self._max_move_depth = node._depth
        if (node._depth <= 0):
            return evaluate(node._grid)
        children = node.get_max_children()
        if len(children) == 0: # if node is a leaf then STOP
            self._no_of_leaves+=1
            return evaluate(node._grid)

        """if it not a leaf node procced"""
        max_value = maxsize*-1
        for child in children:
            value = self.min(child)
            if value > max_value:
                max_value = value
        return max_value

    def min(self,node):
        """i dont use a seperate is_leaf(node) function to evaluate if the node is a leaf
        because that would require to call the get_children functions twice in a
        min or max node, which is expensive"""
        """checking if the node is a leaf node"""
        if node._depth > self._max_move_depth:
            self._max_move_depth = node._depth
        if (node._depth <= 0):
            return evaluate(node._grid)
        children = node.get_min_children()
        if len(children) == 0: # if node is a leaf then STOP
            self._no_of_leaves+=1
            return evaluate(node._grid)

        """if it not a leaf node procced"""
        min_value = maxsize
        for child in children:
            value = self.max(child)
            if value < min_value:
                min_value = value
        return min_value

def evaluate(grid):
    # returns number of blank tiles
    return len(grid.getAvailableCells())

"""Describes a tree node for both min and max"""
class Node:
    def __init__(self,move=None,grid=None,depth=None):
        self._move = move
        if grid is None:
            raise ValueError("GRID CANNOT BE NONE")
        self._grid = grid
        self._depth = depth

    def get_max_children(self):
        children = []
        for move in self._grid.getAvailableMoves():
            grid=self._grid.clone()
            grid.move(move)
            children.append(Node(move=move,grid=grid,depth=self._depth-1))
        return children

    def get_min_children(self):
        children = []
        for cell in self._grid.getAvailableCells():
            grid=self._grid.clone()
            grid.setCellValue(cell,2)
            children.append(Node(move=None,grid=grid,depth=self._depth-1))
            grid.setCellValue(cell,4)
            children.append(Node(move=None,grid=grid,depth=self._depth-1))
        return children

