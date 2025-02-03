


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
    
    def exibir_instrutor_responsavel(self):
       print(f"Instrutor Responsável: {self.instrutor.nome}")
       return self.instrutor.nome
    
    def reservar_aula(self):
       if self.ocupado:
          print("A aula já está ocupada, desculpe!!")
       else:
          self.ocupado = True 
          print(f"Aula de {self.tipo_de_aula} em {self.data_hora.strftime('%d/%m/%y %h:%m')} foi reservada com sucesso!!")
          if not self.instrutor.disponibilidade(self.data_hora, self.duração):
            print("O instrutor não está disponível neste horário.")
            return False

        # Verificar capacidade máxima de alunos
       if len(self.alunos) >= self.capacidade_maxima:
         print("A aula atingiu a capacidade máxima de alunos.")
         return False  
