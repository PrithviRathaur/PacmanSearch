# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    startState = problem.getStartState()
    # Create a stack for where the states will enter
    openList = util.Stack()
    # Create a set to add places you have been
    closedList = set()
    # use a hash table to keep track of parents
    metaData = {problem.getStartState(): None}
    # Create current state
    current = startState
    # Loop through search
    while problem.isGoalState(current) is False:
        if current not in closedList:
            closedList.add(current)
            successors = problem.getSuccessors(current);
            for s,d,c in successors:
                if s not in closedList:
                    metaData[s] = [current, d]
                    openList.push(s)
        closedList.add(current)
        if openList.isEmpty() is not True:
            current = openList.pop()
    path = []
    while current != problem.getStartState():
        info = metaData[current]
        path.append(info[1])
        current = info[0];
    path.reverse()
    return path

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    startState = problem.getStartState()
    # Create a stack for where the states will enter
    openList = util.Queue()
    # Create a set to add places you have been
    closedList = set()
    # use a hash table to keep track of parents
    metaData = {problem.getStartState(): None}
    # Create current state
    current = startState
    # Loop through search
    while problem.isGoalState(current) is False:
        if current not in closedList:
            closedList.add(current)
            successors = problem.getSuccessors(current);
            for s,d,c in successors:
                if s not in list(metaData.keys()):
                    metaData[s] = [current, d]
                    openList.push(s)
        closedList.add(current)
        current = openList.pop()
    path = []
    while current != problem.getStartState():
        info = metaData[current]
        path.append(info[1])
        current = info[0];
    path.reverse()
    return path

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    startState = problem.getStartState()
    # Create a stack for where the states will enter
    openList = util.PriorityQueue()
    # Create a set to add places you have been
    closedList = set()
    # use a hash table to keep track of parents
    metaData = {problem.getStartState(): [None, None, 0]}
    # Create current state
    current = startState
    # Loop through search
    while problem.isGoalState(current) is False:
        if current not in closedList:
            closedList.add(current)
            successors = problem.getSuccessors(current);
            for s,d,c in successors:
                info = metaData[current]
                totalCost = c + info[2]
                if s not in list(metaData.keys()):
                    metaData[s] = (current, d, totalCost)
                    openList.push(s,totalCost)
                else:
                    infoS = metaData[s]
                    if totalCost < infoS[2]:
                        metaData[s] = (current, d, totalCost)
        closedList.add(current)
        current = openList.pop()
    path = []
    while current != problem.getStartState():
        info = metaData[current]
        path.append(info[1])
        current = info[0];
    path.reverse()
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    startState = problem.getStartState()
    # Create a stack for where the states will enter
    openList = util.PriorityQueue()
    # Create a set to add places you have been
    closedList = set()
    # use a hash table to keep track of parents
    metaData = {problem.getStartState(): [None, None, 0]}
    # Create current state
    current = startState
    # Loop through search
    while problem.isGoalState(current) is False:
        if current not in closedList:
            closedList.add(current)
            successors = problem.getSuccessors(current);
            for s,d,c in successors:
                info = metaData[current]
                totalCost = c + info[2]
                heuristicScore = heuristic(s, problem)
                overallCost = totalCost + heuristicScore
                if s not in list(metaData.keys()):
                    metaData[s] = (current, d, totalCost)
                    openList.push(s,overallCost)
                else:
                    infoS = metaData[s]
                    totalCostS = infoS[2];
                    overallCostS = totalCostS + heuristic(s, problem)
                    if overallCost < overallCostS:
                        metaData[s] = (current, d, totalCost)
                        openList.push(s, overallCost)
        closedList.add(current)
        current = openList.pop()
    path = []
    while current != problem.getStartState():
        info = metaData[current]
        path.append(info[1])
        current = info[0];
    path.reverse()
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
