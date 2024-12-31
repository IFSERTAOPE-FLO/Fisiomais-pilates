#Classes : Aluno, Aula, Turma
class Aluno(Anamnese, Assinaturas):
    def__init__ (self, id, nome, peso, altura, condicoes, idade, senha):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.condicoes = condicoes
        self.idade = idade
        self._senha = senha  

    def alterar_dados(self):
        print("Alteração de dados do aluno: ")
        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
        if novo_nome:
            self.nome = novo_nome

        novo_peso = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
        try:
            if novo_peso:
                self.peso = float(novo_peso)
                except ValueError:
                    print("Valor inválido paa peso. Use números decimais.")

        nova_altura = input("Digite a nova altura (ou pressione Enter para manter a atual): ")
        try:
            if nova_altura:
                self.altura = float(nova_altura)
                except ValueError:
                    print("Valor inválido para altura.  Use números decimais.") 

                    print(f"Dados do aluno {self.nome} alterados com sucesso!")

        def exibir_dados(self):
            print(f"ID: {self.id}")
            print(f"Nome: {self.nome}")
            print(f"Peso: {self.peso:.2f} kg")
            print(f"Altura: {self.altura:.2f} m")   
                if self.condicoes:
                    print(f"Condições médicas: {', '.join(self.condicoes)}")  
                    print(f"Idade: {self.idade}")


# Classe: Aula
from datetime import datetime

class Aula:
    def __init__(self, data_hora, duração, tipo_de_aula, instrutor, aluno):
     
     if not self._validar_data_hora(data_hora):
        raise ValueError("o parâmetro 'data_hora' deve ser uma data e hora válida.")
     
     self.data_hora = data_hora 
     self.duração = duração
     self.tipo_de_aula = tipo_de_aula
     self.instrutor = instrutor
     self.aluno = aluno
     self.ocupado = False 

    def _validar_data_hora(self, valor):
       return isinstance(valor, datetime)
    
    def exibir_horarios(self):
       estado = "Está Ocupado" if self.ocupado else "Está Vago"
       print(f"aula de {self.tipo_de_aula} em {self.data_hora.strftime('%d/%m/%y %h:%m')} está {estado}.")
       return estado
    
    def mostrar_duração(self):
       print(f"duração de aula: {self.duração} em minutos.")
       return self.duração
    
    def exibir_instrutor_responsável(self):
       print(f"Instrutor Responsável: {self.instrutor.nome}")
       return self.instrutor.nome
    
    def reservar_aula(self):
       if self.ocupado:
          print("A aula já está ocupada, desculpe!!")
       else:
          self.ocupado = True 
          print(f"Aula de {self.tipo_de_aula} em {self.data_hora.strftime('%d/%m/%y %h:%m')} foi reservada com sucesso!!")
 
            #classe Turma
class Turma:
    def__init__ (self, nome_da_turma, instrutor, horario, numero_maximo, numero_minimo, numero_atual, aluno)
        self.nome_da_turma = nome_da_turma
        self.instrutor = instrutor
        self.horario = horario 
        self.numero_maximo = numero_maximo
        self.numero_minimo = numero_minimo
        self.alunos = []  

    def adicionar_aluno(self, aluno):
        if len(self.alunos) < self.numero_maximo:
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado à turma {self.nome_da_turma}.")
        else:
            print(f"A turma {self.nome_da_turma} atingiu o número máximo de alunos.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno.nome} removido da turma {self.nome_da_turma}.")
        else:
            print(f"O aluno {aluno.nome} não está na turma {self.nome_da_turma}.")

    def exibir_alunos(self):
      if self.alunos:
        print(f"Alunos da turma {self.nome_da_turma}:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")
      else:
        print(f"A turma {self.nome_da_turma} não possui alunos.")


    def exibir_dados_turma(self):
        print(f"Nome da Turma: {self.nome_da_turma}")
        print(f"Instrutor: {self.instrutor.nome}")
        print(f"Horário: {self.horario}")
        print(f"Número Máximo de Alunos: {self.numero_maximo}")
        print(f"Número Mínimo de Alunos: {self.numero_minimo}")
        self.exibir_alunos()
        print("-" * 20)




