import cairo
# use pillow dependency as PIL for fixing spread of pixel ()
from PIL import Image
import os

FILE_NAME = os.path.basename(__file__)
WIDTH = 2 
HEIGHT = 2

# create Surface 
ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)

# - Create context
cr = cairo.Context(ims)

cr.set_source_rgb(1,0,0)
cr.rectangle(1,1,1,1)
cr.fill()

# before using PILLOW
# print(ims.get_data().tobytes())
# ims.write_to_png(f"./exports/{FILE_NAME[:-3]}.png")

img = Image.frombuffer(
    'RGBA',
    (WIDTH, HEIGHT ),
    ims.get_data(),
    'raw',
    'RGBA',
    0,1
)
img.resize((WIDTH, HEIGHT), resample=Image.Resampling.NEAREST)
img.save("raw.png")