from subgrupo_de_Deborah import Assinaturas
from subgrupo_de_Deborah import Anamnese
import hashlib

class Usuario(Assinaturas, Anamnese):
    def __init__(self, usuario_id, senha, nome):
        super().__init__()
        self.usuario_id = usuario_id
        self._senha = hashlib.sha256(senha.encode()).hexdigest()
        self.nome = nome

    def verificar_senha(self, senha_tentativa):
        senha_hash = hashlib.sha256(senha_tentativa.encode()).hexdigest()
        return senha_hash == self._senha

    def __str__(self):
        return f"ÏD: {self.usuario_id}, Nome: {self.nome}"
        usuario1 = Usuario(usuario = "001", nome = "Alicia", senha = "senha123")
        print(usuario1)
        print(f"senha de {usuario1.nome} está correto?, {usuario1.verificar_senha} senha123")

 
               