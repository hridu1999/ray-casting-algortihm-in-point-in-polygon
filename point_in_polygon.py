from polygenerator import random_polygon
import matplotlib.pyplot as plt


def ray_casting(edges, xp, yp):
    counter = 0
    for edge in edges:
        (x1, y1), (x2, y2) = edge
        if (yp < y1) != (yp < y2) and xp < x1 + ((yp-y1)/(y2-y1))*(x2-x1):
            counter += 1
    return counter%2 == 1


def onclick(event):
    xp, yp = event.xdata, event.ydata
    if ray_casting(edges, xp, yp):
        print("The given point is inside of the polygon")
        plt.plot(xp, yp, "go", markersize=5)
    else:
        print("The given point outside of the polygon")
        plt.plot(xp, yp, "ro", markersize=5)
    plt.gcf().canvas.draw()


polygon = random_polygon(num_points=100)
polygon.append(polygon[0])
edges = list(zip(polygon, polygon[1:] + polygon[:1]))
plt.figure(figsize=(10, 10))
plt.gca().set_aspect("equal")
xs, ys = zip(*polygon)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.plot(xs, ys, "b-", linewidth=0.8)
plt.show()

