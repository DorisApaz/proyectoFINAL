import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pyperclip

def dibujar_punto_en_imagen(ruta_imagen):
    # Carga la imagen
    img = mpimg.imread(ruta_imagen)

    # Crea la figura y el gráfico
    fig, ax = plt.subplots()

    # Muestra la imagen
    ax.imshow(img)
    plt.axis('off')

    # Función para capturar las coordenadas del clic
    def onclick(event):
        if event.xdata is not None and event.ydata is not None:   
            coordenada_x = round(event.xdata, 2)
            coordenada_y = round(event.ydata, 2)
            
            coordenadas = {'x': coordenada_x, 'y': coordenada_y}
            print(coordenadas)
            pyperclip.copy(str(coordenadas) + ",")  # Copia las coordenadas al portapapeles

    # Conecta el evento 'button_press_event' a la función 'onclick'
    fig.canvas.mpl_connect('button_press_event', onclick)

    # Muestra el gráfico interactivo
    plt.show()

# Ejemplo de uso
ruta_imagen = 'ciudad.jpeg'
dibujar_punto_en_imagen(ruta_imagen)