#Classes : Aluno, Assinaturas, Login

class Assinatura:
  def __init__(self, id_aluno, nome, peso, altura, condicoes, idade, senha):
    self._id_aluno = id_aluno
    self.nome = nome
    self.peso = peso
    self.altura = altura
    self.condicoes = condicoes
    self.idade = idade
    self.senha = senha

class Aluno(Assinatura):
  def __init__(self, id_aluno, nome, peso, altura, condicoes, idade, senha):
   super().__init__(id_aluno, nome, peso, altura, condicoes, idade, senha)