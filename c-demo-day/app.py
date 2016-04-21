readSplitted = lambda: [int(x) for x in raw_input().split(' ')]
ensureValue = lambda fn, *arg: fn(*arg) if hasattr(fn, '__call__') else fn

def getPack2d(N, M, fillers):
  pack = [[0] * M for _ in xrange(N)]
  pack[0][0] = ensureValue(fillers[0], pack)
  for j in xrange(1, M):
    pack[0][j] = ensureValue(fillers[1], pack, j)
  for i in xrange(1, N):
    pack[i][0] = ensureValue(fillers[2], pack, i)
  fn = fillers[3]
  for i in xrange(1, N):
    for j in xrange(1, M):
      pack[i][j] = fn(pack, i, j)
  return pack[N - 1][M - 1]

def getMinToChange(N, M, maze):
  COME_FROM_TOP = 0
  COME_FROM_LEFT = 1
  infinity = N * M
  emptyVi = lambda i, j: (1 - maze[i][j]) if i < N else 0
  emptyVj = lambda i, j: (1 - maze[i][j]) if j < M else 0
  initializer = [1, 1] if maze[0][0] else [0, 0]
  columnInitializer = emptyVj(0, 1)
  return min(getPack2d(N, M, [
    initializer,
    lambda pack, j: [
      infinity,
      pack[0][j - 1][COME_FROM_LEFT] + maze[0][j]
    ],
    lambda pack, i: [columnInitializer, infinity] if i == 1 else [
      pack[i - 1][0][COME_FROM_TOP] + maze[i][0],
      infinity
    ],
    lambda pack, i, j: [
      min(
        pack[i - 1][j][COME_FROM_TOP],
        pack[i - 1][j][COME_FROM_LEFT] + emptyVj(i - 1, j + 1)
      ) + maze[i][j],
      min(
        pack[i][j - 1][COME_FROM_LEFT],
        pack[i][j - 1][COME_FROM_TOP] + emptyVi(i + 1, j - 1)
      ) + maze[i][j]
    ]
  ]))

def main():
  N, M = readSplitted()
  print getMinToChange(N, M, [[int(x == 'b') for x in raw_input()] for _ in xrange(N)])

main()
