import pandas as pd
from pprint import pprint
from algoritm.graph import Node
from algoritm.dijkstra import Dijkstra

pd.set_option('display.max_columns', None)


node5 = Node(5)
node6 = Node(6)
node4 = Node(4)
node3 = Node(3)
node2 = Node(2)
node1 = Node(1)
node0 = Node(0)

# Connects
node0.connect([
    {'node' : node1, 'distance' : 2},
    {'node' : node3, 'distance' : 1}
])

node1.connect([
    {'node' : node4, 'distance' : 10},
    {'node' : node3, 'distance' : 3}
])

node2.connect([
    {'node' : node0, 'distance' : 4},
    {'node' : node5, 'distance' : 5}
])

node3.connect([
    {'node' : node4, 'distance' : 2},
    {'node' : node6, 'distance' : 4},
    {'node' : node5, 'distance' : 8},
    {'node' : node2, 'distance' : 2},
])

node4.connect([
    {'node' : node6, 'distance' : 6}
])
node5.connect([])

node6.connect([
    {'node' : node5, 'distance' : 1}
])



initialNode = node0
destinationNode = node5

dijkstra = Dijkstra([node0, node1, node2, node3, node4, node5, node6])
dijkstra.workGraph(initialNode)
route = dijkstra.getBestRoute(destinationNode)

#Show table
tb = dijkstra.tb          
for item in tb:
    item['node'] = item['node'].value
    item['father'] = item['father'].value
df = pd.DataFrame(tb)
print(df)

#Show route

routeString = ""
for item in route:
    node = item['node']
    routeString = routeString + str(node) + "->"

routeString = routeString.strip("->")
print(routeString)







"""

v1->v2 75.69 m
v2->v3 64.12 m
v3->v4 33.32 m
v4->v5 75.74 m
v5->v6 43.26 m
v6->v7 106.04 m
v7->v8 65.72 m
v8->v9 78.42 m
v9->v10 79.27 m
v10->v11 33.58 m
v11->v12 66.82 m
v12->v13 71.84 m



"""


"""

v1->v2 74.56 m
v1->v14 93.99 m

v2->v3 63.66 m
v2->v1 74.56 m
v3->v4 36.51 m
v4->v5 75.48 m

v6->v5 75.48 m

v6->v7 107.40 m
v7->v9 64.70 m

v9<->v8 77.04 m
v9<->10 79.30 m
v9->20 80.41 m

v10<->v11 80.01 m
v11<->v12 33.78 m
v12->v13 67.04 m
v13->v14 71.37 m

"""