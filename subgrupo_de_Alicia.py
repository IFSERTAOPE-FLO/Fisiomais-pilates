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
