def picos_vales(h):
  if h[1] > h[0]:
    subiu = True
  elif h[1] < h[0]:
    subiu = False
  else:
    return 0
  
  for i in range(2, len(h)):
    if h[i] > h[i-1] and not subiu:
      subiu = True
    elif h[i] < h[i-1] and subiu:
      subiu = False
    else:
      return 0
  return 1

def main(): 
  n = int(input())
  h = list(map(int, input().split()))

  print(picos_vales(h))

main()