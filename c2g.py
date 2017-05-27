import networkx
import matplotlib.pyplot as plt
import random

import thirdparty.osmparser as darksorcery
import vehicle

G = darksorcery.read_osm(darksorcery.download_osm(-40.4347, -3.7356, -40.2603, -3.6359))

"""
for n in G:
    print(G.node[n]);

for n in G.edges():
    print(G[n[0]][n[1]]);
"""

traffic_signals = []
"""
for n in G:
    if 'highway' in G.node[n]['tags']:
        if G.node[n]['tags']['highway'] == 'traffic_signals':
            traffic_signals.append(n)
"""

vehicle_0 = vehicle.Vehicle(G, G.node[random.choice(G.nodes())], G.node[random.choice(G.nodes())])
vehicle_0.set_path(networkx.shortest_path(G, source=vehicle_0.get_initial()['id'], target=vehicle_0.get_terminal()['id']))
vehicle_0_path_indices = []

positions = { n : (G.node[n]['lat'], G.node[n]['lon']) for n in G}

colors = []
for i, n in enumerate(G):
    if n in traffic_signals:
        colors.append('green')
    elif n in vehicle_0.get_path():
        colors.append('red');
        vehicle_0_path_indices.append(i);
    else: colors.append('blue')

while vehicle_0.get_current() != vehicle_0.get_terminal():
    print("[vehicle_0] current node: %10s, latitude %.7f, longitude %.7f" % \
                        (vehicle_0.get_current()['id'], \
                        vehicle_0.get_current()['lat'], \
                        vehicle_0.get_current()['lon']))
    vehicle_0.update_state()

networkx.draw(G, positions, node_size=50, node_color=colors, linewidths= 0.8, width=1.5)
plt.show()
