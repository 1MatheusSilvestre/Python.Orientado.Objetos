from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def _init_(self, _nome, categoria):
    #_init_. Ele vai construir para nós um método construtor, que é sempre chamado quando criamos uma instância de um objeto e espera alguma informação.
    #todas as informações do objeto vai ser somente dele
    #Para não confundirmos se o nome é do Praça ou do Pizza, sempre passamos o self como primeiro parâmetro
    #para entendermos que se trata daquele objeto que estamos referenciando naquele momento.
        self.nome = _nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        ##OS OBJETO QUE FOREM DA CLASSE RESTAURANTE, VAI TER TODOS ESSES VALORES, NOMES, CATEGORIA, ATIVO

    def _str_(self):
    #O método _str_ é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto
        return f'{self.nome} | {self.categoria}'
        #sempre para mostrar a parte textual, utilizar self.'str'

    @classmethod
    #boa prática indicar que se trata de um método da classe sempre que temos um método que não está referenciado com uma instância, mas sim à classe
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(25)} | {restaurante.ativo}')
            #fazendo um for para printar cada restaurante

    @property
    #PROPERTY quer modificar aquele atributo vai ser lido
    def ativo(self):
        return '⌧' if self._ativo else '☐'
        #o _ serve para mostrar q esse atributo nao pode ser alterado

    def alternar_estado(self):
        self._ativo = not self._ativo 
        #metodo para objetos

    def receber_avaliacao(self, cliente, nota):
    #metodo para fazer receber as avaliações
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
    #metodo para fazer media das avaliações
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        #round faz que apareça somente uma casa decimal
        return media