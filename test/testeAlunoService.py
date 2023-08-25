import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from src.application.aluno_service import AlunoService
from src.infrastructre.repository.in_memory_repository import InMemoryAlunoRepository
from src.domain.aluno import Aluno

class TestAlunoService(unittest.TestCase):

    def setUp(self):
        self.aluno_service = AlunoService(InMemoryAlunoRepository())
        self.aluno_exemplo = Aluno('Teste', 100)

    def test_criar_alujno(self):
        aluno = self.aluno_service.create(self.aluno_exemplo)
        self.assertEqual(aluno.nome, self.aluno_exemplo.nome)
        self.assertEqual(aluno.nota_final, self.aluno_exemplo.nota_final)
        self.assertIsNotNone(aluno.id)
    
