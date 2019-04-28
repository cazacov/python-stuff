import pygame as pg
import sys

cx = 500
cy = 500

position = [0, 0]
pg.init()
opts = 0
opts = pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF
screen = pg.display.set_mode([1000, 1000], opts)
screen.fill([0, 0, 0])
font = pg.font.Font(None, 30)

info = pg.display.Info()


FPS = 300
clock = pg.time.Clock()  # Create a clock object


def render():
    screen.fill([0, 0, 0])

    x = position[0]
    y = position[1]

    pg.draw.circle(screen, [255, 0, 0], [cx + x, cy - y], 30, 0)
    fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
    screen.blit(fps, (50, 50))

    pg.display.flip()
    clock.tick(FPS)


changed = True
done = False


while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True

    position[0] = position[0] + 5
    changed = True

    if changed:
        changed = False
        render()

pg.quit()
sys.exit()
