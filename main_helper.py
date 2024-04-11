import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def plot_threshold(corr_df):
    G = nx.Graph()
    nodes = set(corr_df['FILENAME1'].unique()) | set(corr_df['FILENAME2'].unique())
    G.add_nodes_from(nodes)
    for _, row in corr_df.iterrows():
        weight = row['CORRELATION']
        if row['FILENAME1'] != row['FILENAME2']:
            G.add_edge(row['FILENAME1'], row['FILENAME2'], weight=weight)

    thresholds = np.arange(-1, 1, 0.05)  # Stops before 0.95 to avoid exceeding 0.9
    edge_densities = []

    for thresh in thresholds:
        filtered_edges = [(u, v) for u, v, d in G.edges(data=True) if d['weight'] > thresh]
        edge_density = len(filtered_edges) / (len(nodes) * (len(nodes) - 1) / 2)  # Formula for edge density
        edge_densities.append(edge_density)

    plt.plot(thresholds, edge_densities, marker='o', color='black', markerfacecolor='lightblue', markeredgecolor='black', mouseover=True)
    plt.xlabel('Threshold')
    plt.ylabel('Edge Density')
    plt.title('Edge Density vs. Threshold')
    plt.grid(True)
    plt.show()

def create_network(corr_df, threshold):
    G = nx.Graph()
    nodes = set(corr_df['FILENAME1'].unique()) | set(corr_df['FILENAME2'].unique())
    G.add_nodes_from(nodes)
    for _, row in corr_df.iterrows():
        weight=row['CORRELATION']
        if weight > threshold and row['FILENAME1'] != row['FILENAME2']:
            G.add_edge(row['FILENAME1'], row['FILENAME2'], weight=weight)
    edge_density = (2 * len(G.edges())) / (len(G.nodes()) * (len(G.nodes()) - 1)) # 2E / V(V-1)
    print(f"Edge density of graph at threshold {threshold} is {edge_density}")
    return G

def sort_and_print_top_x(df, num, centrality):
    sorted_df = sorted(df.items(), key=lambda x: x[1], reverse=True)

    print(f"\nTop 10 central nodes based on {centrality} centrality\n")
    for node, centrality in sorted_df[:num]:
        print(f"Node {node}: {centrality} Centrality = {centrality:.4f}")

def calculate_centrality_measures(network):

    degree_centrality = nx.degree_centrality(network)
    sort_and_print_top_x(degree_centrality, 10, 'degree')

    betweenness_centrality = nx.betweenness_centrality(network)
    sort_and_print_top_x(betweenness_centrality, 10, 'betweenness')

    pagerank = nx.pagerank(network, max_iter=2000)
    sort_and_print_top_x(pagerank, 10, 'pagerank')

    eigenvector_centrality = nx.eigenvector_centrality(network)
    sort_and_print_top_x(eigenvector_centrality, 10, 'eigenvector')