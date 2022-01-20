from typing import Tuple

import numpy as np # type: ignore

#Tile graphics structured type compatable with Console.tiles_rgb.
graphic_dt = np.dtype(
	[
		("ch", np.int32), #unicode codepoint.
		("fg", "3B"), # 3 unsigned bites, for RGB colors.
		("bg", "3B"),
	]
)
	
# Tile struct used for statisticall defiend tile data.
tile_dt = np.dtype(
	[
		("walkable", np.bool), # True if this tile can be walked over.
		("transparent", np.bool), # True of this tile dosen't block FOV.
		("dark",graphic_dt), #graphics for when this tile is not in FOV.
		("light", graphic_dt), #Graphics for when the tile is in FOV
	]
)

def new_tile(
	*, # Enforcing the use of keywords, so that paramiter order dosen't matter.
	wakable: int,
	transparent: int,
	dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
	light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
	"""helper function for defining individual tile types """
	return np.array((wakable, transparent, dark, light), dtype =tile_dt)

# SHROUD represents unexplored unseen tiles
SHROUD = np.array((ord(" "),(255,255,255),(0,0,0)),dtype=graphic_dt)

floor = new_tile(
	wakable=True,
	transparent=True,
	dark=(ord(" "),(255,255,255),(50,50,150)),
	light=(ord(" "),(255,255,255),(200,180,50)),
)
wall = new_tile(
	wakable=False,
	transparent=False, 
	dark=(ord(" "),(255,255,255),(0,0,100)),
	light=(ord(" "),(255,255,255),(130,110,50)),
)
