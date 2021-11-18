# ![](./worldmap.png)
# # LEGO World Map in Markley’s Projection

# noreorder
from io import StringIO
import numpy as np
import pandas as pd
import plotly.express as px

# ## Load Data Files

elevation = np.load("data/elevation.npy")
land = np.load("data/land.npy")

# ## The Color Palette of LEGO World Map

color_table = """
  R,   G,   B,  name
 33,  33,  33,  Black
255, 255, 255,  White
 20,  48,  68,  Dark Blue
255,  99,  71,  Coral
255, 126,  20,  Orange
247, 186,  48,  Bright Light Orange
222, 198, 156,  Tan
166, 202,  85,  Lime
 16, 203,  49,  Bright Green
 66, 192, 251,  Medium Azure
  0, 138, 128,  Dark Turquoise
"""

color_table = pd.read_csv(
    StringIO(color_table),
    skipinitialspace=True,
    index_col="name",
)

colors = list(color_table.index)
pallete = np.array(color_table, dtype=np.uint8)

px.imshow(pallete[np.newaxis], width=800)

# ## The Land Map with Shadow

worldmap = np.full_like(land, colors.index("Dark Turquoise"))
worldmap[land == 1] = colors.index("Dark Blue")
worldmap = np.roll(worldmap, 1, axis=1)
worldmap[land == 1] = colors.index("White")

px.imshow(pallete[worldmap], width=800)

# ## The Full World Map with Ocean Topography

block_counts = [
    ("Coral", 600),
    ("Orange", 600),
    ("Bright Light Orange", 600),
    ("Tan", 725),
    ("Lime", 1000),
    ("Bright Green", 600),
    ("Medium Azure", 1600),
    ("Dark Turquoise", 2000),
    ("Black", 10000),  # We may not have enough tiles to cover the ocean.
]
blocks = np.concatenate([np.full(count, colors.index(x)) for x, count in block_counts])

ocean = worldmap == colors.index("Dark Turquoise")
rank_by_depth = np.argsort(elevation[ocean])[::-1].argsort()
worldmap[ocean] = blocks[rank_by_depth]

px.imshow(pallete[worldmap], width=800)

# ## Tiled Maps

tiled_map = np.concatenate(
    [
        np.roll(worldmap, worldmap.shape[1] // 2, axis=1),
        np.rot90(worldmap, 2),
        worldmap,
    ]
)
tiled_map = np.tile(tiled_map, 2)

px.imshow(pallete[tiled_map], width=800)
