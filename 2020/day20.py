#!/usr/bin/env python3

def to_bin(word):
  return "".join(["0" if c == "." else "1" for c in word])

def enumerate_edges(image):
  edge1 = image[0]
  edge2 = image[-1]
  edge3 = "".join([line[0] for line in image])
  edge4 = "".join([line[-1] for line in image])
  edges = (edge1, edge2, edge3, edge4)

  edges = list(map(to_bin, edges))
  edges_forward = map(lambda x: int(x, 2), edges)
  edges_backward = map(lambda x: int(x[::-1], 2), edges) 

  return (tuple(sorted([x, y])) for x, y in zip(edges_forward, edges_backward))

with open("day20.txt") as f:
  tiles = {}

  tile_id = -1
  tile = []

  for line in f:
    line = line.strip()
    if tile_id == -1:
      tile_id = int(line.split(" ")[1][:-1])
      continue

    if line != "":
      tile.append(line)
      continue

    tiles[tile_id] = list(enumerate_edges(tile))
    tile_id = -1
    tile = []

  edge_count = {}
  for tile_id, edges in tiles.items():
    for edge in edges:
      edge_count[edge] = edge_count.get(edge, 0) + 1

  for edge, count in edge_count.items():
    if count == 1:
      continue

    for tile_id, edges in tiles.items():
      if edge in edges:
        del edges[edges.index(edge)]

  ans = 1
  for tile_id, edges in tiles.items():
    if len(edges) == 2:
      ans *= tile_id
  print(ans)

