import pygame as pg
import sys
from vector_ops import *
from lib_3d import Render3D
from bodies_3d import *


screen_width = 1600
screen_height = 1000

origin = [screen_width/2, screen_height/2]
vertices = rhombicuboctahedron.vertices
faces = rhombicuboctahedron.faces
position = [0, 0, 0]
zoom = 1


pg.init()
opts = pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF
screen = pg.display.set_mode([screen_width, screen_height], opts)
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
        rotate_z(vertices, 0.02)
        changed = True
    if keys[pg.K_e]:
        rotate_z(vertices, -0.02)
        changed = True
    if keys[pg.K_a]:
        rotate_y(vertices, 0.02)
        changed = True
    if keys[pg.K_d]:
        rotate_y(vertices, -0.02)
        changed = True
    if keys[pg.K_w]:
        rotate_x(vertices, -0.02)
        changed = True
    if keys[pg.K_s]:
        rotate_x(vertices, 0.02)
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
