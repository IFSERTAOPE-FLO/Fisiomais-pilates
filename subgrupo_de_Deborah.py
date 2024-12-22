#Classes : Anamnese, Assinaturas, Login


class Anamnese:
  def __init__(self, nome, peso, altura, idade, telefone, endereco, profissao, responsavel):
    self.nome = nome
    self.peso = peso
    self.altura = altura
    self.idade = idade
    self.telefone = telefone
    self.endereco = endereco
    self.profissao = profissao
    self.responsavel = responsavel


    self.questoes = {
     "queixa" : None,
     "se_praticou_pilates" : None,
     "pratica_atividade_fisicas" : None,
     "qual_e_frequencia_da_atividade_fisicas" : None,
     "teve_cirurgia" : None,
     "detalhes_da_cirurgia" : None,
     "usa_medicamentos" : None,
     }
    self.objetivos = {
     "Postura" : None,
     "Aliviar_estresse" : None,
     "Alongamento" : None,
     "Aliviar_dor" : None,
     "Melhor_condicionamento" : None,
     "Fortalecer_musculos" : None
     }


  def questionario(self):
    print("=-=-"*10)
    print("\n=-=-=-=-=- FICHA DE ANAMNESE -=-=-=-=-=\n")
    print("=-=-"*10)


    print("\n- Dados :")
    self.nome = input("\nInforme seu nome completo : \nR = ")
    self.peso = float(input("\nInforme o seu peso: \nR = "))
    self.altura = float(input("\nInforme sua altura: \nR = "))
    self.idade = int(input("\nInforme sua idade: \nR = "))
    self.telefone = int(input("\nInforme o seu telefone: \nR = "))
    self.endereco = input("\nInforme o seu endereço: \nR = ")
    while True:
     if self.idade > 18:
      self.profissao = input("\nInforme a sua profissão: \nR = ")
      break
     else:
      self.profissao = "NÃO"
      break
    while True:
     if self.idade < 18:
      self.responsavel == input("Informe o nome do seu responsável : R = ")
      break
     else:
      self.responsavel = "NÃO"
      break
 


    print("\n - História Clínica :\n")
    self.questoes["queixa"] = input("\nQueixa principal : \nR = ")


    while True:
     self.questoes["se_praticou_pilates"] = input("\nJá praticou pilates antes (Sim/Não)? \nR = ").upper()
     if self.questoes["se_praticou_pilates"] == "SIM" or self.questoes["se_praticou_pilates"] == "NÃO":
      break
     else:
      pass


    while True:
     self.questoes["pratica_atividade_fisicas"] = input("\nPratica ou praticou outras atividades fisícas (Sim/Não)? \nR = ").upper()
     if self.questoes["pratica_atividade_fisicas"] == "SIM":
      self.questoes["qual_e_frequencia_da_atividade_fisicas"] = input("Qual a frequência da atividade fisica? \nR = ")
      break
     elif self.questoes["pratica_atividade_fisicas"] == "NÃO":
      break
     else:
      pass


    while True:
     self.questoes["teve_cirurgia"] = input("\nTeve cirurgia (Sim/Não)? \nR = ").upper()
     if self.questoes["teve_cirurgia"] == "SIM":
      self.questoes["detalhes_da_cirurgia"] = input("Informe detalhes da cirurgia : \nR = ")
      break
     elif self.questoes["teve_cirurgia"] == "NÃO":
      break
     else:
      pass
   
    while True:
     self.questoes["usa_medicamentos"] = input("\nUsa medicamentos (Sim/Não)? R = ").upper()
     if self.questoes["usa_medicamentos"] == "SIM" or self.questoes["usa_medicamentos"] == "NÃO":
      break
     else:
      pass



    print("\n- Objetivo(s) do paciente :\n")


    while True:
     self.objetivos["Postura"] = input("\nPostura  (Sim/Não)? R = ").upper()
     if self.objetivos["Postura"] == "SIM" or self.objetivos["Postura"] == "NÃO":
      break
     else:
      pass


    while True:
     self.objetivos["Aliviar_estresse"] = input("\nAliviar o estresse (Sim/Não)? R = ").upper()
     if self.objetivos["Aliviar_estresse"] == "SIM" or self.objetivos["Aliviar_estresse"] == "NÃO":
      break
     else:
      pass


    while True:
     self.objetivos["Alongamento"] = input("\nAlogamento (Sim/Não)? R = ").upper()
     if self.objetivos["Alongamento"] == "SIM" or self.objetivos["Alongamento"] == "NÃO":
      break
     else:
      pass


    while True:
     self.objetivos["Aliviar_dor"] = input("\nAliviar as dores (Sim/Não)? R = ").upper()
     if self.objetivos["Aliviar_dor"] == "SIM" or self.objetivos["Aliviar_dor"] == "NÃO":
      break
     else:
      pass


    while True:
     self.objetivos["Melhor_condicionamento"] = input("\nMelhorar o condicionamento físico (Sim/Não)? R = ").upper()
     if self.objetivos["Melhor_condicionamento"] == "SIM" or self.objetivos["Melhor_condicionamento"] == "NÃO":
      break
     else:
      pass


    while True:
     self.objetivos["Fortalecer_musculos"] = input("\nFortalecer os musculos (Sim/Não)? R = ").upper()
     if self.objetivos["Fortalecer_musculos"] == "SIM" or self.objetivos["Fortalecer_musculos"] == "NÃO":
      break
     else:
      pass




  def exibir_dados(self):
   print("=-=-"*10)
   print("\n=-=-=-=-=- FICHA DE ANAMNESE -=-=-=-=-=\n")
   print("=-=-"*10)


   print("\n- DADOS :")
   print(f'''
Nome : {self.nome}
Idade : {self.idade}
Responsável : {self.responsavel}
Profissão : {self.profissao}
Peso : {self.peso}
Altura : {self.altura}
Telefone : {self.telefone}
Endereço : {self.endereco}''')
   
   print("\n- HISTÓRIA CLÍNICA :\n")
   print("Queixa principal : ", self.questoes["queixa"])
   print("Praticou pilates : ", self.questoes["se_praticou_pilates"])
   if self.questoes["pratica_atividade_fisicas"] == "SIM":
    print(f"Pratica atividades física : ", self.questoes["pratica_atividade_fisicas"],". ", self.questoes["qual_e_frequencia_da_atividade_fisicas"])
   else:
    print(f"Pratica atividades física : ", self.questoes["pratica_atividade_fisicas"])
   if self.questoes["teve_cirurgia"] == "SIM":
    print(f"Teve cirurgia : ",self.questoes["teve_cirurgia"], ". ", self.questoes["detalhes_da_cirurgia"])
   else:
    print(f"Teve cirurgia : ",self.questoes["teve_cirurgia"])
   print(f"Usa medicamentos : ",self.questoes["usa_medicamentos"])


   print("\n- OBJETIVOS :\n")
   print(f"Melhorar a postura : ",self.objetivos["Postura"])
   print(f"Aliviar o estresse : ",self.objetivos["Aliviar_estresse"])
   print(f"Alongamento : ",self.objetivos["Alongamento"])
   print(f"Aliviar as dores : ",self.objetivos["Aliviar_dor"])
   print(f"Melhor condicionamento físico : ",self.objetivos["Melhor_condicionamento"])
   print(f"Fortalecer os musculos : ",self.objetivos["Fortalecer_musculos"])





class Assinatura:
  def __init__(self, senha):
   self.senha = senha


user1 = Anamnese(None, None, None, None, None, None, None, None)
user1.exibir_dados()