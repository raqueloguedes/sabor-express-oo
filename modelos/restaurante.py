class Restaurante:
    #nome da clss sempre com letra maiuscula
    restaurantes = []

    def __init__(self, nome, categoria):
        # o init é o "construtor" de uma classe em Python, responsável por inicializar os objetos dessa classe com valores específicos.
        # self é tipo individual daquele que ta sendo referido
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
        #append vai inserir na lista todo objt criado
    
    def __str__(self):
        #metodo especial str vai transformar aquela numeração do objeto em strig
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    #property é usado para mudar a propriedade de um atributo
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()