class Ong():
    ong:str
    presidente:str
    projetos:list
    def __init__(self, ong, presidente):
        self.ong = ong
        self.presidente = presidente
        self.projetos = []
class Projeto():
    projeto:str
    data:str
    responsavel:str
    status:str
    def __init__(self, projeto, descricao, responsavel, status):
        self.projeto = projeto
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status
    