import pandas as pd
from pprint import pprint
from algoritm.graph import Node
from algoritm.dijkstra import Dijkstra
from data import getData
from dev_image import dibujar_punto_en_imagen

pd.set_option('display.max_columns', None)


def logica(initialNode, destinationNode):
        
    data =  getData()
    app_nodes = []
    def searchData(name):
        dat = None
        for i in data:
            if i['name'] == name:
                dat = i

        return dat

    def searchNode(name):
        nod = None
        for i in app_nodes:
            if i.value == name:
                nod = i

        return nod


    for i in data:
        node = Node(i['name'])
        app_nodes.append(node)

    for i in app_nodes:
        d = searchData(i.value)
        conn = []
        for k in d['connections']:
            nod = searchNode(k[0])
            co = {'node' : nod, 'distance' : k[1]}
            conn.append(co)     

        i.connect(conn)


    initialNode = searchNode(initialNode)
    destinationNode = searchNode(destinationNode)

    dijkstra = Dijkstra(app_nodes)
    dijkstra.workGraph(initialNode)
    route = dijkstra.getBestRoute(destinationNode)

    #Show table
    tb = dijkstra.tb          

    for item in tb:
        item['node'] = item['node'].value
        #item['father'] = item['father'].value
    df = pd.DataFrame(tb)
    print(df)


    #Show route
    routeString = ""
    for item in route:
        node = item['node']
        routeString = routeString + str(node) + "->"

    routeString = routeString.strip("->")




    dataRoute = []
    for i in route:
        d = searchData(i['node'])
        dataRoute.append(d)

    ruta_imagen = 'ciudad.jpeg'
    dibujar_punto_en_imagen(ruta_imagen, dataRoute)


    return routeString
#Draw route on image
