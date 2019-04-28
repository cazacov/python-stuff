import pygame as pg
import sys
from vector_ops import *
from lib_3d import Render3D

origin = [500, 500]
# vertices = [[100, 100, -100],
#             [-100, 100, -100],
#             [-100, -100, -100],
#             [100, -100, -100],
#             [100, 100, 100],
#             [-100, 100, 100],
#             [-100, -100, 100],
#             [100, -100, 100]
#             ]
#
# faces = [[0, 1, 2, 3],
#          [0, 4, 5, 1],
#          [1, 5, 6, 2],
#          [2, 6, 7, 3],
#          [3, 7, 4, 0],
#          [7, 6, 5, 4]]


vertices = [[0, 0, 111.8],
            [80.9, -58.78, 50.0],
            [80.9, 58.78, 50.0],
            [-30.9, 95.11, 50.0],
            [-100.0, 0.0, 50.0],
            [-30.9, -95.11, 50.0],
            [100.0, 0.0, -50.0],
            [30.9, 95.11, -50.0],
            [-80.9, 58.78, -50.0],
            [-80.9, -58.78, -50.0],
            [30.9, -95.11, -50.0],
            [0, 0, -111.8]]

faces = [[0,2,1],
         [0,3,2],
         [0,4,3],
         [0,5,4],
         [0,1,5],
         [1,2,6],
         [2,3,7],
         [3,4,8],
         [4,5,9],
         [5,1,10],
         [6,2,7],
         [7,3,8],
         [8,4,9],
         [9,5,10],
         [10,1,6],
         [11,6,7],
         [11,7,8],
         [11,8,9],
         [11,9,10],
         [11,10,6]]

position = [0, 0, 0]
zoom = 1
pg.init()
opts = pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF
screen = pg.display.set_mode([1000, 1000], opts)
screen.fill([0, 0, 0])
info = pg.display.Info()
FPS = 300
clock = pg.time.Clock()  # Create a clock object

renderer = Render3D()
renderer.init()

changed = True
done = False


while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        position = add(position, [-5, 0, 0])
        changed = True
    if keys[pg.K_RIGHT]:
        position = add(position, [5, 0, 0])
        changed = True
    if keys[pg.K_UP]:
        position = add(position, [0, 5, 0])
        changed = True
    if keys[pg.K_DOWN]:
        position = add(position, [0, -5, 0])
        changed = True

    if keys[pg.K_q]:
        rotateZ(vertices, 0.02)
        changed = True
    if keys[pg.K_e]:
        rotateZ(vertices, -0.02)
        changed = True
    if keys[pg.K_a]:
        rotateY(vertices, 0.02)
        changed = True
    if keys[pg.K_d]:
        rotateY(vertices, -0.02)
        changed = True
    if keys[pg.K_w]:
        rotateX(vertices, -0.02)
        changed = True
    if keys[pg.K_s]:
        rotateX(vertices, 0.02)
        changed = True

    if keys[pg.K_KP_PLUS]:
        zoom = zoom * 1.01
        changed = True
    if keys[pg.K_KP_MINUS]:
        zoom = zoom / 1.01
        changed = True

    if changed:
        changed = False
        renderer.render(screen, vertices, faces, position, zoom, origin)

pg.quit()
sys.exit()
