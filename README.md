# Pacman Search Algorithms

This project involves developing a Pacman agent to that will find paths through various maze layouts. These paths are optimized to reach a location of the map or collect various pellets in the maze. 

![PacmanMazeImage](maze.png)

## Project Description 

I have built the general search algorithms, such as a Depth First Search, Breadth First Search, Uniform Cost Search, and A* Search. These algorithms are found in **search.py**. Various heuristics were also developed in order to optimize food or different locations in the maze. This project is aimed at exploring the use of search functions as an introduction to artificial intelligence. By implementing the search algorithms, one can see the tradeoffs between accuracy and computation that are involved in solving search problems. The overall Pacman AI project was developed at UC Berkeley primarily by John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).

## Running the Project

### Testing out the Code

First, one will need to clone this repo. To start off, I recommend just running the following command: 

```bash
python3 pacman.py
```
This will pull up the Pacman Gui. From here you can play a game of pacman using the arrow keys. There are many different options that **pacman.py** supports which can be shown by running the following command: 

```bash
python3 pacman.py -h
```

### DFS

The following commands will run DFS on three different maze layouts (tinyMaze, mediumMaze, and bigMaze). All of the maze layouts can be found in the layouts folder in the repo. 

```bash
python3 pacman.py -l tinyMaze -p SearchAgent
python3 pacman.py -l mediumMaze -p SearchAgent
python3 pacman.py -l bigMaze -z .5 -p SearchAgent
```

### BFS

The following commands will run BFS on the mediumMaze and bigMaze layouts. 

```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

### UCS

The following commands will run UCS on the mediumMaze and compare it to different cost functions on mediumDottedMaze and mediumScaryMaze. The difference between these functions is only in their cost functions. 

```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

### A*
The following commands will run A* and test the algorithm using the manhattan heuristic which is implemented in **searchAgents.py**. 

```bash
python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### Developing a Heuristic

The advantages to A* search become more apparent when the search problem becomes more difficult, such as finding the shortest path between all 4 corners in the maze.  In order to run A* on this problem though, a heuristic for the algorithm needs to be developed. The heuristic can be shown in the **searchAgents.py** file. The performance of BFS and A* in solving this problem are shown by running the following commands.

```bash
python3 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python3 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

An even more difficult problem is finding the shortest path in eating all the food in the maze. A heuristic for this problem can be found in **searchAgents.py**. To test the heuristic, run the following commands: 

```bash
python3 pacman.py -l testSearch -p AStarFoodSearchAgent
python3 pacman.py -l trickySearch -p AStarFoodSearchAgent
```
