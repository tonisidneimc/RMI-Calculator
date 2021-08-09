import Pyro4

@Pyro4.expose
class Calculadora(object) :
  def add(self, a, b) :
    res = a + b;
    print(f"Chamada remota: {a}+{b} = {res}")
    return res
    
  def sub(self, a, b) :
    res = a - b;
    print(f"Chamada remota: {a}-{b} = {res}")
    return res
    
  def mul(self, a, b) :
    res = a * b;
    print(f"Chamada remota: {a}*{b} = {res}")
    return res
    
  def div(self, a, b) :
    res = a / b;
    print(f"Chamada remota: {a}/{b} = {res}")
    return res

if __name__ == "__main__" :
  
  daemon = Pyro4.Daemon()
  
  try :
    uri = daemon.serveSimple (
    {
      Calculadora : "Calculadora"  # registra a class
    },
    host = "localhost",
    port = 8080,
    ns = False, verbose = True)  
  
  except KeyboardInterrupt :
    print("Exiting...")
  
