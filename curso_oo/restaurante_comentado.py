from modelos.avaliacao_oo import Avaliacao

class Restaurante:
    #nome da clss sempre com letra maiuscula
    restaurantes = []

    def __init__(self, nome, categoria):
        # o init é o "construtor" de uma classe em Python, responsável por inicializar os objetos dessa classe com valores específicos.
        # self é tipo individual daquele que ta sendo referido
        self._nome = nome.title()
        #title() iniciais com letra maiuscula
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        #append vai inserir na lista todo objt criado
        #o _ nos atributos informa que esse atributo não deve ser alterado, é projegido
    
    def __str__(self):
        #metodo especial str vai retornar uma strig
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    #pra indicar que é um método da classe (exclusivo), recebe cls
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')
    #str em media transforma em string
    @property
    #property é usado para mudar como esse atributo vai ser lido
    def ativo(self):
        return '⌧' if self._ativo else '☐'
        #usamos emoji aqui pra ser lido como ativo e inativo

    def alternar_estado(self):
        #metod para alternar o estado do objeto
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media