#Classes : Aluno, Assinaturas, Login

class Anamnese:
  def __init__(self, nome, peso, altura, idade, senha, telefone, endereco, estado_civil, profissao, responsavel):
    self.nome = nome
    self.peso = peso
    self.altura = altura
    self.idade = idade
    self.senha = senha
    self.telefone = telefone
    self.endereco = endereco
    self.estado_civil = estado_civil
    self.profissao = profissao
    self.responsavel = responsavel
  
  def questionario():
    input("Já praticou pilates antes (S/N)? R = ")
    input("Pratica ou praticou outras atividades fisícas (S/N)? R = ")
    input(" (S/N)? R = ")

class Assinatura:
  def __init__():

class Aluno(Assinatura):
  def __init__(self, assinatura, anamnese):
   self.assinatura = assinatura
   self.anamnese = anamnese

assinatura = Assinatura() 
lana = Aluno(anamnese, assinatura)