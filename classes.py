class Ong():
    id:str
    ong:str
    presidente:str
    projetos:list
    def __init__(self, id, ong, presidente):
        self.id = id
        self.ong = ong
        self.presidente = presidente
        self.projetos = []
class Projeto():
    projeto:str
    data:str
    responsavel:str
    status:str
    def __init__(self, id, projeto, descricao, responsavel, status):
        self.id = id
        self.projeto = projeto
        self.descricao = descricao
        self.responsavel = responsavel
        self.status = status
    