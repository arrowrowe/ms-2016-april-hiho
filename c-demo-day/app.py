readSplitted = lambda: [int(x) for x in raw_input().split(' ')]
ensureValue = lambda fn, *arg: fn(*arg) if hasattr(fn, '__call__') else fn

def getPack2d(N, M, fillers):
  pack = [[0] * M for _ in xrange(N)]
  pack[0][0] = ensureValue(fillers[0], pack)
  for i in xrange(1, M):
    pack[0][i] = ensureValue(fillers[1], pack, i)
  for i in xrange(1, N):
    pack[i][0] = ensureValue(fillers[2], pack, i)
  fn = fillers[3]
  for i in xrange(1, N):
    for j in xrange(1, M):
      pack[i][j] = fn(pack, i, j)
  return pack[N - 1][M - 1]

def getMinToChange(N, M, maze):
  total = N * M
  return min(getPack2d(N, M, [
    [0, 0],
    lambda pack, i: [total, pack[0][i - 1][1] + int(maze[0][i])],
    [total, total],
    lambda pack, i, j: [
      min(
        pack[i - 1][j][0],
        pack[i - 1][j][1] + int(j + 1 < M and not maze[i - 1][j + 1])
      ) + int(maze[i][j]),
      min(
        pack[i][j - 1][1],
        pack[i][j - 1][0] + int(i + 1 < N and not maze[i + 1][j - 1])
      ) + int(maze[i][j])
    ]
  ]))

def main():
  N, M = readSplitted()
  print getMinToChange(N, M, [[x == 'b' for x in raw_input()] for _ in xrange(N)])

main()
