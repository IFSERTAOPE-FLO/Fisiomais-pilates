from AssinaturaPilates import Assinaturas
from Anamnese import Anamnese
from datetime import datetime  

class Aluno(Anamnese, Assinaturas):  
    def _init_(self, nome, peso, altura, idade, condicoes=None):
        super()._init_(nome, peso, altura, idade, condicoes)  

        assinaturas_system = Assinaturas()

        
        assinatura = assinaturas_system.buscar_assinatura_por_nome(nome)
        if not assinatura:
            raise ValueError(f"Erro: Não há assinatura ativa para o aluno '{nome}'. Cadastre primeiro.")

        aluno_id = assinatura['aluno_id']
        tipo = assinatura['tipo']
        data_inicio = assinatura['data_inicio']

        # Armazenando os dados de assinatura
        self.id = aluno_id
        self.nome = nome  
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.condicoes = condicoes
        self.assinatura = assinatura  
        self._senha = assinatura['senha']  

    def exibir_dados(self):
        print("\n=-=-=-= DADOS DO ALUNO =-=-=-=")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} m")
        print(f"Idade: {self.idade}")
        print(f"Condições médicas: {', '.join(self.condicoes) if self.condicoes else 'Nenhuma'}")
        print("=-=-=-=\n")

    def alterar_dados(self):
        print("Alteração de dados do aluno: ")

        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
        if novo_nome:
            self.nome = novo_nome

        try:
            novo_peso = input("Digite o novo peso (ou pressione Enter para manter o atual): ")
            if novo_peso:
                self.peso = float(novo_peso)
        except ValueError:
            print("Valor inválido para peso. Use números decimais.")

        try:
            nova_altura = input("Digite a nova altura (ou pressione Enter para manter o atual): ")
            if nova_altura:
                self.altura = float(nova_altura)
        except ValueError:
            print("Valor inválido para altura. Use números decimais.")

        print(f"Dados do aluno {self.nome} alterados com sucesso!")

    def alterar_senha(self, nova_senha):
        Assinaturas().atualizar_senha(self.id, nova_senha)  
        print("Senha alterada com sucesso!")

    def verificar_senha(self, senha):
        return Assinaturas().verificar_senha(self.id, senha)  

def cadastrar_aluno():
    print("\n=-=-=-= CADASTRO DE ALUNO =-=-=-=")

    nome = input("Digite o nome do aluno: ")

    assinaturas_system = Assinaturas()

    # Buscar a assinatura ativa do aluno
    assinatura = assinaturas_system.buscar_assinatura_por_nome(nome)
    if not assinatura:
        print("Erro: O aluno não possui uma assinatura ativa. Cadastre a assinatura primeiro.")
        return None

    peso = float(input("Digite o peso do aluno (kg): "))
    altura = float(input("Digite a altura do aluno (m): "))
    idade = int(input("Digite a idade do aluno: "))
    
    condicoes_medicas = input("Informe as condições médicas do aluno (separadas por vírgula, ou 'Nenhuma' se não houver): ")
    condicoes_medicas = [] if condicoes_medicas.lower() == 'nenhuma' else [x.strip() for x in condicoes_medicas.split(',')]

    aluno = Aluno(nome, peso, altura, idade, condicoes_medicas)

    aluno.exibir_dados()
    aluno.questionario()  

    return aluno

if _name_ == "_main_":
    try:
        aluno1 = cadastrar_aluno()
        if aluno1:
            aluno1.exibir_dados()

            nova_senha = input("Digite a nova senha: ")
            aluno1.alterar_senha(nova_senha)

            senha_teste = input("Digite a senha para verificação: ")
            if aluno1.verificar_senha(senha_teste):
                print("Senha verificada com sucesso!")
            else:
                print("Senha incorreta.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")