##
# @see https://github.com/neozhaoliang/gifmaze
##
import gifmaze as gm

surface = gm.GIFSurface(width=400, height=400, color_depth=2, bg_color=0)
surface.set_palette([0, 0, 0, 255, 255, 255, 255, 0, 255, 140, 140, 140])

anim = gm.Animation(surface)
anim.set_control(speed=20, delay=5, trans_index=3)

maze = anim.create_maze_in_region(cell_size=20, region=0, mask=None)


from gifmaze.algorithms import prim

anim.pad_delay_frame(200)
prim(maze, start=(0, 0))
anim.pad_delay_frame(500)

surface.save('gifmaze.gif')
surface.close()

