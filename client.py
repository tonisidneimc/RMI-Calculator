import sys
import Pyro4

if __name__ == "__main__" :
  if len(sys.argv) < 4 : 
    print("Usage: client.py URI N1 N2")
    sys.exit(1)
  
  uri = sys.argv[1]
  a, b = map(int, sys.argv[2:4])
  
  calc = Pyro4.Proxy(uri)
  
  print(f"{a} + {b} = ", calc.add(a, b))
  print(f"{a} - {b} = ", calc.sub(a, b))
  print(f"{a} * {b} = ", calc.mul(a, b))
  print(f"{a} / {b} = ", calc.div(a, b))
