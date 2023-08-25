from src.application.aluno_repository import AlunoRepository

class InMemoryAlunoRepository(AlunoRepository):

    def __init__(self):
        self._alunos = []
        self._contador = 1

    def save(self, aluno):
        aluno.id = self._contador
        self._alunos.append(aluno)
        self._contador += 1
        return aluno