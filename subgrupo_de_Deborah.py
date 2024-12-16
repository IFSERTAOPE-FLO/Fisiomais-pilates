#Classes : Aluno, Instrutor, Aula

class Aluno:
  def __init__(self, id_aluno, nome, peso, altura, condicoes, idade, senha):
    self._id_aluno = id_aluno
    self.nome = nome
    self.peso = peso
    self.altura = altura
    self.condicoes = condicoes
    self.idade = idade
    self._senha = senha