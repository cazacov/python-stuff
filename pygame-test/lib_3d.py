import pygame as pg

from vector_ops import *

class Render3D:

    def init(self):
        pass

    def render(self, screen, vertices, faces, position, zoom, origin):
        screen.fill([0, 0, 0])

        cx = origin[0]
        cy = origin[1]

        px = position[0]
        py = position[1]

        for face in faces:
            pointlist = []

            for n in face:
                point = vertices[n]
                x = px + point[0] * zoom
                y = py + point[1] * zoom
                pointlist.append([cx + x, cy - y])

            p0 = vertices[face[1]]
            p1 = vertices[face[0]]
            p2 = vertices[face[2]]

            v1 = vect(p0, p1)
            v2 = vect(p0, p2)
            normal = cross_product(v1, v2)

            if normal[2] > 0:

                lightVector = [-1, -1, 1]
                cosA = cosAngle(lightVector, normal)

                light = 25
                if cosA > 0:
                    light = light + cosA * 230

                pg.draw.polygon(screen, [light, light, light], pointlist, 0)
                pg.draw.polygon(screen, [255, 255, 255], pointlist, 1)

        pg.display.flip()
