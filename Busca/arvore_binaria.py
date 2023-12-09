class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

def inserir(raiz, chave):
    if raiz is None:
        return No(chave)
    
    # Se a chave for menor, insira na subárvore esquerda
    if chave < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, chave)
    # Se a chave for maior, insira na subárvore direita
    elif chave > raiz.chave:
        raiz.direita = inserir(raiz.direita, chave)

    return raiz

def buscar(raiz, chave):
    # Se a raiz é None ou a chave está na raiz
    if raiz is None or raiz.chave == chave:
        return raiz
    
    # Se a chave é maior que a raiz, busque na subárvore direita
    if chave > raiz.chave:
        return buscar(raiz.direita, chave)
    
    # Se a chave é menor que a raiz, busque na subárvore esquerda
    return buscar(raiz.esquerda, chave)

# Exemplo de uso:
raiz = None
chaves = [50, 30, 20, 40, 70, 60, 80]

# Inserir elementos na árvore
for chave in chaves:
    raiz = inserir(raiz, chave)

# Buscar um elemento
elemento_buscado = 60
resultado = buscar(raiz, elemento_buscado)

if resultado:
    print(f"Elemento {elemento_buscado} encontrado na árvore.")
else:
    print(f"Elemento {elemento_buscado} não encontrado na árvore.")

# Neste exemplo, a classe No representa um nó da árvore.
# As funções inserir e buscar são utilizadas para inserir elementos e procurar elementos na árvore binária de busca.
# Este é um exemplo simples, e na prática, você pode precisar implementar funcionalidades adicionais.
# Como remoção de elementos ou percorrimento em ordem da árvore.