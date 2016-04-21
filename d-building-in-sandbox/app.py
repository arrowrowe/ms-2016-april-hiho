readSplitted = lambda: [int(x) for x in raw_input().split(' ')]

BLOCK_DEAD = 0
BLOCK_ALIVE = 1
BLOCK_WITH_CUBE = 2

def getWorldWithCubes(xBound, yBound, zBound, cubes):
  world = [[[BLOCK_DEAD] * zBound for __ in xrange(yBound)] for _ in xrange(xBound)]
  for cube in cubes:
    world[cube[0]][cube[1]][cube[2]] = BLOCK_WITH_CUBE
  return world

def getNeighbors(x, y, z):
  yield x - 1, y, z
  yield x + 1, y, z
  yield x, y - 1, z
  yield x, y + 1, z
  yield x, y, z - 1
  yield x, y, z + 1

# See also https://www.zhihu.com/question/42406890/answer/94388263
class Sand:
  def __init__(self, cubeCount):
    self.xBound = self.yBound = self.zBound = 1
    self.cubeIndex = 0
    self.cubes = [None] * cubeCount

  def build(self, x, y, z):
    self.xBound = max(self.xBound, x)
    self.yBound = max(self.yBound, y)
    self.zBound = max(self.zBound, z)
    self.cubes[self.cubeIndex] = (x - 1, y - 1, z - 1)
    self.cubeIndex += 1

  def valid(self):
    self.world = getWorldWithCubes(self.xBound, self.yBound, self.zBound, self.cubes)
    zMax = self.zBound - 1
    self.floodfill([(x, y, zMax) for x in xrange(self.xBound) for y in xrange(self.yBound)])
    for cubeIndex in xrange(len(self.cubes) - 1, -1, -1):
      x, y, z = self.cubes[cubeIndex]
      if (
        z and self.hasNoSuchNeighbor(x, y, z, BLOCK_WITH_CUBE)
      ) or (
        z < zMax and self.hasNoSuchNeighbor(x, y, z, BLOCK_ALIVE)
      ):
        return False
      self.world[x][y][z] = BLOCK_DEAD
      self.floodfill([(x, y, z)])
    return True

  def hasNoSuchNeighbor(self, x, y, z, neighbor):
    for x, y, z in getNeighbors(x, y, z):
      if self.isIn(x, y, z) and self.world[x][y][z] == neighbor:
        return False
    return True

  def isIn(self, x, y, z):
    return 0 <= x < self.xBound and 0 <= y < self.yBound and 0 <= z < self.zBound

  def floodfill(self, q):
    while q:
      x, y, z = q.pop()
      if self.isIn(x, y, z) and self.world[x][y][z] == BLOCK_DEAD:
        self.world[x][y][z] = BLOCK_ALIVE
        q.extend(list(getNeighbors(x, y, z)))

def main():
  for _ in xrange(input()):
    cubeCount = input()
    sand = Sand(cubeCount)
    for __ in xrange(cubeCount):
      sand.build(*readSplitted())
    print 'Yes' if sand.valid() else 'No'

main()
