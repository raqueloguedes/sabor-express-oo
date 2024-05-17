class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

musica4 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

#No código fornecido, a pessoa criou uma classe Musica com três atributos: nome, artista e duracao. Em seguida, criou uma instância da classe musica1 e atribuiu valores apenas a dois atributos: nome e duracao, deixando o atributo artista sem ser atribuído. Ao tentar imprimir as informações da música musica1.artista, você verá que o atributo artista não foi explicitamente atribuído a nenhum valor, então ele terá o valor padrão para atributos de classe não inicializados, que é uma string vazia. Neste caso, nenhum erro será exibido no console, e a saída mostrará as informações disponíveis, mesmo que o artista não tenha sido especificamente atribuído.