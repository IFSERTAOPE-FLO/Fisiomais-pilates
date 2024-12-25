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



from datetime import datetime, timedelta


class AssinaturaPilates:
    valores_tipo = {
        "diariamente": 30,
        "semanal": 200,
        "mensal": 800,
        "anual": 8500
    }


    def __init__(self, aluno_id, tipo, data_inicio):
        if tipo not in self.valores_tipo:
            raise ValueError("Tipo de assinatura inválido. Escolha entre 'diariamente', 'semanal', 'mensal' ou 'anual'.")


        self.aluno_id = aluno_id
        self.tipo = tipo
        self.data_inicio = self.formatar_data(data_inicio)
        self.data_fim = self.calcular_data_fim()
        self.valor_total = self.valores_tipo[tipo]
        self.valor_a_pagar = self.valor_total
        self.status = self.definir_status()


    def formatar_data(self, data):
        try:
            if "/" in data:
                return datetime.strptime(data, '%d/%m/%Y')
            elif "-" in data:
                return datetime.strptime(data, '%Y-%m-%d')
            else:
                raise ValueError("Formato de data inválido.")
        except ValueError:
            raise ValueError("Data inválida. Use o formato DD/MM/YYYY ou YYYY-MM-DD.")


    def calcular_data_fim(self):
        if self.tipo == "diariamente":
            return self.data_inicio + timedelta(days=1)
        elif self.tipo == "semanal":
            return self.data_inicio + timedelta(days=7)
        elif self.tipo == "mensal":
            return self.data_inicio + timedelta(days=30)
        elif self.tipo == "anual":
            return self.data_inicio + timedelta(days=365)


    def definir_status(self):
        return "ativa" if datetime.now() <= self.data_fim else "expirada"


    def renovar_assinatura(self, novo_tipo=None):
        if novo_tipo:
            self.tipo = novo_tipo
            self.valor_total = AssinaturaPilates.valores_tipo[novo_tipo]
            self.valor_a_pagar = self.valor_total
        self.data_inicio = datetime.now()
        self.data_fim = self.calcular_data_fim()
        self.status = self.definir_status()
        print(f"Assinatura renovada para o tipo '{self.tipo.capitalize()}' com sucesso! Nova data de término: {self.data_fim.strftime('%d/%m/%Y')}.")


    def __str__(self):
        return (f"Aluno ID: {self.aluno_id}, Tipo: {self.tipo.capitalize()}, "
                f"Data Início: {self.data_inicio.strftime('%d/%m/%Y')}, Data Fim: {self.data_fim.strftime('%d/%m/%Y')}, "
                f"Status: {self.status.capitalize()}, Valor Total: R${self.valor_total:.2f}")




class Assinaturas:
    def __init__(self):
        self.assinaturas = []
        self.alunos = {}
        self.turmas = {}  
        self.capacidade_turma = 35


    def cadastrar_aluno(self, aluno_id, nome):
        if aluno_id in self.alunos:
            print(f"Erro: Já existe um aluno com o ID {aluno_id}.")
        else:
            self.alunos[aluno_id] = nome
            print(f"Aluno {nome} (ID: {aluno_id}) cadastrado com sucesso.")


    def aluno_existe(self, aluno_id):
        return aluno_id in self.alunos


    def adicionar_assinatura(self, aluno_id, tipo, data_inicio):
        if not self.aluno_existe(aluno_id):
            print(f"Erro: O aluno com ID {aluno_id} não está cadastrado.")
            return


        if any(assinatura.aluno_id == aluno_id and assinatura.status == "ativa" for assinatura in self.assinaturas):
            print(f"Erro: O aluno com ID {aluno_id} já possui uma assinatura ativa.")
            return


        opcao_pilates = input("O aluno deseja fazer pilates individual ou em turma? (individual/turma): ").strip().lower()


        if opcao_pilates not in ["individual", "turma"]:
            print("Opção inválida. Escolha 'individual' ou 'turma'.")
            return


        nova_assinatura = AssinaturaPilates(aluno_id, tipo, data_inicio)


        if opcao_pilates == "turma":
            nova_assinatura.valor_total *= 0.75  
            turma_disponivel = None
            for turma, alunos in self.turmas.items():
                if len(alunos) < self.capacidade_turma:
                    turma_disponivel = turma
                    break


            if not turma_disponivel:
                turma_disponivel = f"Turma {len(self.turmas) + 1}"
                self.turmas[turma_disponivel] = []


            self.turmas[turma_disponivel].append(aluno_id)
            print(f"O aluno foi adicionado à {turma_disponivel}.")


            if len(self.turmas[turma_disponivel]) == self.capacidade_turma:
                print(f"{turma_disponivel} está cheia!")


        self.assinaturas.append(nova_assinatura)
        print(f"Assinatura adicionada para {self.alunos[aluno_id]}: {nova_assinatura}")


    def cancelar_assinatura(self, aluno_id):
        for assinatura in self.assinaturas:
            if assinatura.aluno_id == aluno_id:
                nome_aluno = self.alunos[aluno_id]
                confirmacao = input(f"Você deseja cancelar a assinatura do aluno {nome_aluno} (ID: {aluno_id})? (sim/não): ").strip().lower()
                if confirmacao == "sim":
                    self.assinaturas.remove(assinatura)
                    del self.alunos[aluno_id]
                    print(f"Assinatura do aluno {nome_aluno} foi cancelada e aluno removido.")
                else:
                    print("Cancelamento abortado.")
                return
        print(f"Erro: Nenhuma assinatura encontrada para o aluno {aluno_id}.")


    def renovar_assinatura(self, aluno_id, novo_tipo=None):
        for assinatura in self.assinaturas:
            if assinatura.aluno_id == aluno_id:
                if assinatura.status == "expirada":
                    print(f"A assinatura do aluno {self.alunos[aluno_id]} está expirada. Renovando agora...")
                assinatura.renovar_assinatura(novo_tipo)
                return
        print(f"Erro: Nenhuma assinatura encontrada para o aluno {aluno_id}.")


    def total_assinaturas(self):
        return len(self.assinaturas)


    def listar_assinaturas(self):
        return [str(assinatura) for assinatura in self.assinaturas]


    def listar_alunos(self):
        return self.alunos


    def listar_turmas(self):
        print("Turmas:")
        for turma, alunos in self.turmas.items():
            print(f"{turma}: {len(alunos)} alunos")




assinaturas = Assinaturas()


while True:
    print("\nMENU:")
    print("1 - Cadastrar Aluno")
    print("2 - Adicionar Assinatura")
    print("3 - Cancelar Assinatura")
    print("4 - Renovar Assinatura")
    print("5 - Listar Alunos")
    print("6 - Listar Assinaturas")
    print("7 - Listar Turmas")
    print("8 - Sair")


    opcao = input("Escolha uma opção: ").strip()


    if opcao == "1":
        aluno_id = int(input("Digite o ID do aluno: "))
        nome = input("Digite o nome do aluno: ")
        assinaturas.cadastrar_aluno(aluno_id, nome)


    elif opcao == "2":
        aluno_id = int(input("Digite o ID do aluno: "))
        tipo = input("Digite o tipo de assinatura (diariamente, semanal, mensal, anual): ").lower()
        data_inicio = input("Digite a data de início (DD/MM/YYYY ou YYYY-MM-DD): ")
        assinaturas.adicionar_assinatura(aluno_id, tipo, data_inicio)


    elif opcao == "3":
        aluno_id = int(input("Digite o ID do aluno cuja assinatura deseja cancelar: "))
        assinaturas.cancelar_assinatura(aluno_id)


    elif opcao == "4":
        aluno_id = int(input("Digite o ID do aluno cuja assinatura deseja renovar: "))
        novo_tipo = input("Digite o novo tipo de assinatura (diariamente, semanal, mensal, anual) ou pressione Enter para manter o tipo atual: ").lower()
        if novo_tipo == "":
            novo_tipo = None
        assinaturas.renovar_assinatura(aluno_id, novo_tipo)


    elif opcao == "5":
        alunos = assinaturas.listar_alunos()
        print("Alunos cadastrados:")
        for id, nome in alunos.items():
            print(f"ID: {id}, Nome: {nome}")


    elif opcao == "6":
        assinaturas_lista = assinaturas.listar_assinaturas()
        print("Assinaturas:")
        for assinatura in assinaturas_lista:
            print(assinatura)


    elif opcao == "7":
        assinaturas.listar_turmas()


    elif opcao == "8":
        print("Encerrando o programa. Até mais!")
        break


    else:
        print("Opção inválida. Tente novamente.")




