import pandas as pd

import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

def count_nodes_and_edges(multi_digraph):
    """
    Count the number of nodes and edges in a directed multigraph by visiting it manually.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        tuple: A tuple containing the number of nodes and the number of edges.
    """
    # Create a set to store visited nodes
    visited_nodes = set()
    edge_count = 0

    # Iterate through all nodes in the graph
    for node in multi_digraph.nodes:
        visited_nodes.add(node)  # Add the node to the set of visited nodes

        # Iterate through outgoing neighbors (edges) from the current node
        for neighbor in multi_digraph[node]:
            # Count all parallel edges (multi-edges) between the current node and its neighbor
            edge_count += len(multi_digraph[node][neighbor])

    # The number of nodes is the size of the visited_nodes set
    node_count = len(visited_nodes)

    return node_count, edge_count

def in_degree_count(multi_digraph):
    """
    Count the in-degree of each node in a directed multigraph.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        dict: A dictionary where keys are nodes and values are the in-degree of each node.
    """
    
    in_degree = dict()

    for node in multi_digraph.nodes:
        in_degree[node] = 0

    for node in multi_digraph.nodes:
        for neighbor in multi_digraph[node]:
            in_degree[neighbor] += len(multi_digraph[node][neighbor])
    
    return in_degree

def out_degree_count(multi_digraph):
    """
    Count the out-degree of each node in a directed multigraph.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        dict: A dictionary where keys are nodes and values are the out-degree of each node.
    """
    
    out_degree = dict()

    for node in multi_digraph.nodes:
        out_degree[node] = 0

    for node in multi_digraph.nodes:
        for neighbor in multi_digraph[node]:
            out_degree[node] += len(multi_digraph[node][neighbor])
    
    return out_degree


def density(multi_digraph):
    """
    Calculate the density of a directed multigraph.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        float: The density of the directed multigraph.
    """
    # Get the number of nodes and edges in the graph
    node_count, edge_count = count_nodes_and_edges(multi_digraph)

    # Calculate the maximum number of edges in a directed graph with the same number of nodes
    max_edges = node_count * (node_count - 1)

    # Calculate the density of the graph
    graph_density = edge_count / max_edges

    return graph_density

def show_distribution(multi_digraph):
    """
    Display the distribution of in-degrees and out-degrees of a directed multigraph.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.
    """

    # For each node: Compute the in-degree and out-degree
    in_degree = in_degree_count(multi_digraph)
    out_degree = out_degree_count(multi_digraph)
    
    # Plot two separate histograms for the in-degree and the out-degree, respectively
    plt.hist(list(in_degree.values()), bins=20, alpha=0.5, label='In-degree')
    plt.xlabel('In-degree')
    plt.ylabel('Frequency')
    plt.show()

    plt.hist(list(out_degree.values()), bins=20, alpha=0.5, label='Out-degree')
    plt.xlabel('Out-degree')
    plt.ylabel('Frequency')
    plt.show()

def hubs(multi_digraph):
    """
    Identify airports with degrees higher than the 90th percentile and list them as "hubs."

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        list: A list of airport codes that are considered "hubs."
    """
    # Get the in-degree and out-degree of each node
    in_degrees = in_degree_count(multi_digraph)
    out_degrees = out_degree_count(multi_digraph)

    # Compute the 90th percentile for in-degree and out-degree
    in_degree_threshold = np.percentile(list(in_degrees.values()), 90)
    out_degree_threshold = np.percentile(list(out_degrees.values()), 90)

    # Identify airports with in-degree and out-degree higher than the 90th percentile
    hub_airports = [node for node in multi_digraph.nodes if in_degrees[node] > in_degree_threshold and out_degrees[node] > out_degree_threshold]

    return hub_airports

def density_type(multi_digraph):
    """
    Identify the type of network based on its density.

    Parameters:
        multi_digraph (nx.MultiDiGraph): A directed multigraph created using NetworkX.

    Returns:
        str: A string representing the type of network.
    """
    # Get the density of the graph
    graph_density = density(multi_digraph)

    # Determine the type of network based on its density
    if graph_density < 1:
        network_type = "Sparse"
    else:
        network_type = "Dense"

    return network_type