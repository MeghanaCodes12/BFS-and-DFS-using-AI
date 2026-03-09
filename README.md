# Graph Traversal Algorithms in Python (BFS & DFS)

## Description
This repository contains Python implementations of two fundamental graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

Graph traversal algorithms are used to systematically visit all nodes (vertices) in a graph. BFS explores nodes **level by level using a queue**, while DFS explores nodes **as deep as possible along a branch before backtracking**, usually using a stack or recursion. These algorithms are widely used in computer science for searching, pathfinding, and graph analysis. 

---

## Features
- Implementation of **Breadth-First Search (BFS)**
- Implementation of **Depth-First Search (DFS)**
- Graph creation using **user input**
- Displays **node traversal order**
- Checks whether a **destination node is reachable**
- Simple and beginner-friendly Python code
- Uses **Adjacency List** graph representation

---

## Technologies / Tools Used
- **Python 3**
- Basic Data Structures
  - List
  - Stack
  - Queue
- Command Line Interface (CLI)

---

## Project Structure
```
graph-traversal-bfs-dfs
│
├── bfs.py
├── dfs.py
└── README.md
```

---

## How to Run the Programs

### 1. Clone the Repository
```
git clone https://github.com/your-username/graph-traversal-bfs-dfs.git
```

### 2. Navigate to the Folder
```
cd graph-traversal-bfs-dfs
```

### 3. Run BFS
```
python bfs.py
```

### 4. Run DFS
```
python dfs.py
```

---

## Program Workflow
1. Enter the **number of nodes**
2. Enter the **names of nodes**
3. Enter **neighbors for each node**
4. Enter:
   - **Start node**
   - **Destination node**
5. The program will display:
   - Whether the destination is **reachable**
   - The **traversal path**

---

## Real World Applications

### Breadth-First Search (BFS)
- Finding the **shortest path in unweighted graphs**
- **Navigation and routing systems**
- **Social network analysis**
- **Web crawling**
- **Level-order traversal in trees**

### Depth-First Search (DFS)
- **Cycle detection in graphs**
- **Topological sorting**
- **Maze and puzzle solving**
- **Connected component detection**
- **Artificial intelligence search algorithms**

---

## Learning Outcomes
This project helps understand:
- Graph representation using adjacency lists
- Difference between **BFS and DFS**
- Use of **Queue vs Stack** in algorithms
- Graph reachability problems
- Basic graph traversal techniques
