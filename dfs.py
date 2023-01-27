from no import No

# Depth-First Search - Busca em Profundidade
def dfs(problema):
  no = problema.iniciar()

  pilha = Pilha()
  pilha.push(no)

  visitados = Visitados(no.estado)

  while not pilha.esta_vazio():
    no = pilha.pop()
    visitados.adicionar(no)

    # faz o teste objetivo. Se chegou no resultado final
    # retorna o No correspondente
    if(testar_objetivo(problema, no)):
      print(f"Estados visitados: {visitados.tamanho()}")
      return no
    
    # função sucessores define os Nós sucessores
    nos_sucessores = gerar_sucessores(problema, no)

    # para cada sucessor, se armazena se ainda não visitado
    for no_sucessor in nos_sucessores:
      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor): pilha.push(no_sucessor)

  print(f"Estados visitados: {visitados.tamanho()}")
  return None

def testar_objetivo(problema, no):
  return problema.testar_objetivo(no.estado)

def gerar_sucessores(problema, no):
  sucessores = problema.gerar_sucessores(no.estado)
  nos_sucessores = [No(estado, no, aresta) for (estado, aresta) in sucessores]
  return nos_sucessores

class Visitados:
  def __init__(self, estado_inicial):
    # Conjuntos (Sets) em python e {1, 2, 3}
    # necessita ser uma tupla por ser comparável com ==
    self.visitados = set({tuple(estado_inicial)})
  
  def adicionar(self, no):
    self.visitados.add(tuple(no.estado))
  
  def foi_visitado(self, no):
    return tuple(no.estado) in self.visitados

  def tamanho(self):
    return len(self.visitados)

class Pilha:
  def __init__(self):
    self.pilha = []
  
  def push(self, item):
    self.pilha.append(item)
  
  def pop(self):
    if(self.esta_vazio()):
      return None
    else:
      return self.pilha.pop()

  def esta_vazio(self):
    return len(self.pilha) == 0

  def tamanho(self):
    return len(self.pilha)