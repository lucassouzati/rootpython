from abc import ABC, abstractmethod

class AlunoRepository(ABC):

    @abstractmethod
    def save(self, aluno): 
        pass


