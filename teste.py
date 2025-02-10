from subgrupo_de_Deborah import Assinaturas

class SistemaLogin(Assinaturas):
    def __init__(self):
        super().__init__()

    def login(self, aluno_id, senha):
        if aluno_id in self.alunos and self.alunos[aluno_id]['senha'] == senha:
            print(f"Login bem-sucedido! Bem-vindo, {self.alunos[aluno_id]['nome']}!")
            return True
        else:
         print("Erro: ID ou senha não encontrados.")
         print("alguma informação está incorreta caso tenha dúvidas ou ter esquecido sua senha ou id entre em contato com o administrador nesse email:")
         print("assistencia.clinicapilates@gmail.com")
         return False
