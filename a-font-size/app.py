readSplitted = lambda: [int(x) for x in raw_input().split(' ')]
upperDiv = lambda a, b: a / b + (1 if a % b else 0)
sum = lambda array: reduce(lambda a, b: a + b, array, 0)

# Find largest i from [a, b] s.t. fn(i) <= target.
def maxLeq(a, b, fn, target):
  while a < b:
    i = (a + b) / 2
    if fn(i) > target:
      b = i - 1
    elif a == i:
      return a if fn(b) > target else b
    else:
      a = i
  return b

# With width W, height H and paragraphs A (each has A[i] words),
# how many pages we need if using size S?
def pageCount(W, H, A, S):
  wordPerLine = W / S
  return upperDiv(
    sum(upperDiv(a, wordPerLine) for a in A), # total lines
    H / S # line per page
  )

# Find largest size S s.t. its page count <= P
def fontsize(N, P, W, H, A):
  return maxLeq(
    1, min(W, H),
    lambda S: pageCount(W, H, A, S),
    P
  )

def main():
  for _ in xrange(input()):
    N, P, W, H = readSplitted()
    A = readSplitted()
    print fontsize(N, P, W, H, A)

main()
