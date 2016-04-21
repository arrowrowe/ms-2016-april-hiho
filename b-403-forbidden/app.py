readSplitted = lambda: [int(x) for x in raw_input().split(' ')]
cutAt = lambda s, i: (s[:i], s[i + 1:]) if i > -1 else (s, None)
cutL = lambda s, c: cutAt(s, s.find(c))
cutR = lambda s, c: cutAt(s, s.rfind(c))

def matchByMask(mask, address, ip):
  alreadyMatched = 8
  for i in xrange(4):
    masked = address[i] ^ int(ip[i])
    if alreadyMatched < mask:
      if masked > 0:
        return False
    else:
      return masked < 2 ** (alreadyMatched - mask)
    alreadyMatched += 8
  return True

def isAllowed(rules, ip):
  for rule in rules:
    mode, address, mask = rule
    if ip == address if mask is None else (mask == 0 or matchByMask(mask, address, ip.split('.'))):
      return mode
  return True

def explain(raw):
  mode, addressAndMask = cutL(raw, ' ')
  mode = mode == 'allow'
  address, mask = cutR(addressAndMask, '/')
  if mask is not None:
    mask = int(mask)
    if mask > 0:
      address = map(int, address.split('.'))
  return mode, address, mask

def main():
  N, M = readSplitted()
  rules = [None] * N
  for i in xrange(N):
    rules[i] = explain(raw_input())
  for _ in xrange(M):
    print 'YES' if isAllowed(rules, raw_input()) else 'NO'

main()
