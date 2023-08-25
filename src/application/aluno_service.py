from src.application.aluno_repository import AlunoRepository
from src.domain.aluno import Aluno

class AlunoService:
    def __init__(self, repository: AlunoRepository):
        self.repository = repository

    def create(self, aluno):
        return self.repository.save(aluno)