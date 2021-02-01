import csv
import networkx as nx
from networkx.algorithms import community

with open('stations_csv.csv') as nodecsv:
    nodereader = csv.reader(nodecsv)
    nodes = [n for n in nodereader] [1:]

node_names = [n[0] for n in nodes]

with open('trips.csv') as edgecsv:
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader] [1:]
edge_names = [e[2:4] for e in edges]
print(len(node_names))
print(len(edge_names))

G=nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edge_names)
print(nx.info(G))

name_dict = {}
lat_dict = {}
lon_dict = {}

for node in nodes:
    name_dict[node[0]] = node[1]
    lat_dict[node[0]] = node[2]
    lon_dict[node[0]] = node[3]

nx.set_node_attributes(G, name_dict, 'Stop_name')
nx.set_node_attributes(G, lat_dict, 'lat')
nx.set_node_attributes(G, lon_dict, 'lon')

for n in G.nodes():
    print(n, G.nodes[n]['Stop_name'])

density = nx.density(G)
print("Network Density:", density)
