class Filmes:

    def __init__(self, titulo, genero, categoria, lancamento, foto, video, id = None):

        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__categoria = categoria
        self.__lancamento = lancamento
        self.__foto = foto
        self.__video = video

    def perfil_video(self):
        if self.__id is not None:
            return f'filme/{self.__id}'
        
        return f'filme/desconhecido'
    
    @property
    def id(self):
        return self.__id
    @property
    def titulo(self):
        return self.__titulo
    @property
    def genero(self):
        return self.__genero
    @property
    def categoria(self):
        return self.__categoria
    @property
    def lancamento(self):
        return self.__lancamento
    @property
    def foto(self):
        return self.__foto
    @property
    def video(self):
        return self.__video
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
    @lancamento.setter
    def lancamento(self, lancamento):
        self.__lancamento = lancamento
    @foto.setter
    def foto(self, foto):
        self.__foto = foto
    @video.setter
    def video(self, video):
        self.__video = video
    
        
        