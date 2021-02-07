import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
import pandas as pd

#read file with nodes
with open('stations_csv.csv') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader] [1:]

#create list of node names
node_names = [n[0] for n in nodes]

#read file with edges
with open('trips.csv') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader] [1:]
edge_names = [e[2:4] for e in edges]

#print number of nodes and edges (for control)
print(len(node_names))
print(len(edge_names))

G=nx.Graph() #Initialize Graph
G.add_nodes_from(node_names) #Add nodes to the Graph
G.add_edges_from(edge_names) #Add edges to the Graph
print(nx.info(G))

#create dictionary for attributes
name_dict = {}
lat_dict = {}
lon_dict = {}

for node in nodes:
    name_dict[node[0]] = node[1]
    lat_dict[node[0]] = node[2]
    lon_dict[node[0]] = node[3]

nx.set_node_attributes(G, name_dict, 'Stop') #Add dictionary as node attribute
nx.set_node_attributes(G, lat_dict, 'lat')
nx.set_node_attributes(G, lon_dict, 'lon')

for n in G.nodes():
    print(n, G.nodes[n]["Stop"])

density = nx.density(G)
print("Network Density:", density)

nx.draw(G)
plt.show

