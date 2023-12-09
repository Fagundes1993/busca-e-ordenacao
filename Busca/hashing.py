class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, chave):
        # Função de hash simples para este exemplo
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = [(chave, valor)]
        else:
            for i, (ch, val) in enumerate(self.tabela[indice]):
                if ch == chave:
                    # Se a chave já existe, atualiza o valor
                    self.tabela[indice][i] = (chave, valor)
                    break
            else:
                # Se a chave não existe, adiciona à lista
                self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = self.hash(chave)
        if self.tabela[indice] is not None:
            for k, v in self.tabela[indice]:
                if k == chave:
                    return v
        return None

# Exemplo de uso:
tabela = TabelaHash(tamanho=10)

# Inserir elementos na tabela
tabela.inserir("nome", "João")
tabela.inserir("idade", 25)
tabela.inserir("cidade", "ExemploCity")

# Buscar elementos na tabela
print("Nome:", tabela.buscar("nome"))
print("Idade:", tabela.buscar("idade"))
print("Cidade:", tabela.buscar("cidade"))
print("Profissão:", tabela.buscar("profissao"))

# Neste exemplo, a classe TabelaHash possui métodos para calcular o índice usando uma função de hash simples e inserir e buscar elementos na tabela.
# A função hash usa a função hash incorporada do Python e reduz o valor resultante para caber no tamanho da tabela.
# Note que este é um exemplo simplificado e não leva em consideração colisões ou outras técnicas avançadas de tratamento de colisões.
# Tratar colisões é uma consideração importante ao trabalhar com tabelas de hash na prática.
# Existem várias estratégias para lidar com colisões, como encadeamento (uso de listas ligadas) ou resolução por sondagem (procurar o próximo local disponível).