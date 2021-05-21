import matplotlib.pyplot as plt 
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y, name):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3,6))
    #plt.title(name)
    plt.bar(x,y)
    plt.xticks(rotation=45)
    #plt.xlabel('Time')
    #plt.ylabel('Current Occupancy')
    plt.tight_layout()
    graph = get_graph()
    return graph