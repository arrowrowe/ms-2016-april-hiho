readSplitted = lambda: [int(x) for x in raw_input().split(' ')]

def getMinToChange(N, M, maze):
  pack = [[[0, 0] for x in xrange(0, M)] for y in xrange(0, N)]
  total = N * M
  for i in xrange(1, N):
    pack[i][0] = [total, total]
  for i in xrange(1, M):
    pack[0][i] = [total, pack[0][i - 1][1] + int(maze[0][i])]
  for i in xrange(1, N):
    for j in xrange(1, M):
      pack[i][j] = [
        min(
          pack[i - 1][j][0],
          pack[i - 1][j][1] + int(j + 1 < M and not maze[i - 1][j + 1])
        ) + int(maze[i][j]),
        min(
          pack[i][j - 1][1],
          pack[i][j - 1][0] + int(i + 1 < N and not maze[i + 1][j - 1])
        ) + int(maze[i][j])
      ]
  return min(pack[N - 1][M - 1])

def main():
  N, M = readSplitted()
  print getMinToChange(N, M, [[x == 'b' for x in raw_input()] for _ in xrange(N)])

main()
