# Airline Network Analysis Project

## Project Overview
This project analyzes a dataset of over 3.5 million US domestic flights from 1990 to 2009. The goal is to apply data mining and network analysis techniques to gain insights into air traffic patterns and evaluate the efficiency of the airline network. Additionally, we explore partitioning strategies to divide the network between two hypothetical airlines.

## Key Tasks and Features

### 1. Graph Creation and Analysis
- **Objective**: Represent the airline network as a graph where nodes are airports and edges are flight routes.
- **Graph Metrics**:
  - Total number of nodes (airports) and edges (routes).
  - Network density, defined as the ratio of actual edges to possible edges.
  - Degree distribution to identify hub airports with the highest connectivity.
- **Insights**:
  - Busiest routes by passenger volume.
  - Under-utilized routes where flight capacity exceeds passenger demand.

### 2. Centrality Measures
- **Objective**: Evaluate the importance of each airport using network centrality measures:
  - **Betweenness Centrality**: Frequency of an airport appearing on the shortest paths between other airports.
  - **Closeness Centrality**: Accessibility of an airport to all others in the network.
  - **Degree Centrality**: Direct connectivity of an airport.
  - **PageRank**: Importance of an airport based on connections from other highly connected airports.
- **Insights**: Identification of critical hubs and their roles in the network.

### 3. Route Optimization
- **Objective**: Identify optimal flight paths and evaluate over-utilized and under-utilized routes.
- **Techniques**:
  - Analyze passenger-to-flight ratios to detect inefficiencies.
  - Highlight overburdened or redundant connections.

### 4. Airline Network Partitioning
- **Objective**: Simulate the division of the network between two airlines.
- **Methods**:
  - **Minimum Cut**: Divide the network into two subgraphs by removing the smallest number of edges.
  - **Balanced Partitioning**: Use the Kernighan-Lin algorithm to create two subgraphs of similar size while minimizing edges between partitions.
- **Visualizations**: Graphs highlight the partitions and edges removed during the division.

### 5. Community Detection
- **Objective**: Discover natural groupings or clusters of airports within the network.
- **Methods**: Apply modularity-based algorithms to detect communities of strongly connected nodes.

### 6. Bonus: Connected Components
- **Objective**: Identify isolated groups of airports and analyze their significance in the network.
- **Application**: Implement algorithms in a distributed computing environment using MapReduce for scalability.

### 7. Algorithmic Challenges
- **Objective**: Solve a theoretical problem of finding the cheapest route with at most `k` stops.
- **Implementation**:
  - A priority queue-based approach inspired by Dijkstra's algorithm.
  - Optimization to minimize memory usage and redundant calculations.
- **Complexity Analysis**:
  - Time complexity: `O(k * E * log(N * k))`
  - Space complexity: `O(E + N * k)`

## Visualizations
- Graphs and histograms provide insights into degree distributions, centrality measures, and partitioning outcomes.
- Interactive maps display the geographic spread of air traffic and highlight busiest routes.

## Conclusion
This project demonstrates the power of network analysis and data mining techniques in uncovering insights from a large dataset. By leveraging advanced algorithms and visualizations, we explored the structure, efficiency, and potential restructuring of the US airline network.

## Project files
- [`HW5.ipynb`](HW5.ipynb): contains questions 1, 4, 5, Bonus, and the AQ.
- [`Questions2-3.ipynb`](Questions2-3.ipynb): contains questions 2–3.

