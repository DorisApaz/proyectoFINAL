import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from data import getData


def getDataNode(coords, nameNode):
    nodeData = None
    for i in coords:
        if i['name'] == nameNode:
            nodeData = i
    return nodeData

def dibujar_punto_en_imagen(ruta_imagen, coords):
    # Carga la imagen
    img = mpimg.imread(ruta_imagen)

    # Crea la figura y el gráfico
    fig, ax = plt.subplots()

    # Muestra la imagen
    ax.imshow(img)
    plt.axis('off')   

    # Dibuja el punto rojo en las coordenadas dadas y agrega el número
    for i, coord in enumerate(coords):    
        x, y, connections = coord['x'], coord['y'], coord['connections']
        color = 'ro'
        if i == 0: color = 'go'
        if i == len(coords) - 1: color = 'go'
        
        ax.plot(x, y, color, markersize=15)
        
        ax.text(x, y, str(coord['name']), color='white', fontsize=8, ha='center', va='center')


        #Draw line connection
        if(len(connections) > 0):
            for c in connections:
                connectedNode = getDataNode(coords, c[0])
                if connectedNode == None : continue
                cx, cy = connectedNode['x'], connectedNode['y']
                
                ax.annotate('', xy=(cx, cy), xytext=(x,y),
                    arrowprops=dict(arrowstyle='->', color='blue', linewidth=2),
                    annotation_clip=False)
                
                # Calcula el punto medio entre las coordenadas inicial y final
                punto_medio = ((x + cx) / 2,
                            (y + cy) / 2)

                # # Agrega el texto en el punto medio de la línea
            
                ax.text(punto_medio[0], punto_medio[1], str(c[1]), color='black', fontsize=10,
                            ha='center', va='center', fontweight='bold')
                
    # Muestra el gráfico con los puntos y números dibujados
    plt.show()

# Ejemplo de uso
ruta_imagen = 'ciudad.jpeg'
 
#dibujar_punto_en_imagen(ruta_imagen, getData())
