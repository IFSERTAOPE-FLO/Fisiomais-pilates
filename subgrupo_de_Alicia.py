from Assinaturas import Assinaturas
from Anamnese import Anamnese

class Aluno(Anamnese, Assinaturas):  
    def __init__(self, nome, peso, altura, idade, condicoes=None):
        super().__init__(nome, peso, altura, idade, condicoes)  

        assinaturas_system = Assinaturas()
        assinatura = assinaturas_system.buscar_assinatura_por_nome(nome)
        
        if not assinatura:
            raise ValueError(f"Erro: Não há assinatura ativa para o aluno '{nome}'. Cadastre primeiro.")

        self.id = assinatura.aluno_id
        self.nome = nome  
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.condicoes = condicoes or []
        self.assinatura = assinatura  
        self._senha = assinaturas_system.alunos[self.id]["senha"]  

    def exibir_dados(self):
        print("\n=-=-=-= DADOS DO ALUNO =-=-=-=")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} m")
        print(f"Idade: {self.idade}")
        print(f"Condições médicas: {', '.join(self.condicoes) if self.condicoes else 'Nenhuma'}")
        print(f"Assinatura: {self.assinatura.tipo.capitalize()} - Status: {self.assinatura.status}")
        print("=-=-=-=\n")

    def alterar_dados(self):
        print("Alteração de dados do aluno: ")

        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ").strip()
        if novo_nome:
            self.nome = novo_nome

        try:
            novo_peso = input("Digite o novo peso (ou pressione Enter para manter o atual): ").strip()
            if novo_peso:
                self.peso = float(novo_peso)
        except ValueError:
            print("Valor inválido para peso. Use números decimais.")

        try:
            nova_altura = input("Digite a nova altura (ou pressione Enter para manter o atual): ").strip()
            if nova_altura:
                self.altura = float(nova_altura)
        except ValueError:
            print("Valor inválido para altura. Use números decimais.")

        print(f"Dados do aluno {self.nome} alterados com sucesso!")

    def alterar_senha(self, nova_senha):
        assinaturas_system = Assinaturas()
        assinaturas_system.alunos[self.id]["senha"] = nova_senha
        print("Senha alterada com sucesso!")

    def verificar_senha(self, senha):
        assinaturas_system = Assinaturas()
        return assinaturas_system.alunos[self.id]["senha"] == senha

def cadastrar_aluno():
    print("\n=-=-=-= CADASTRO DE ALUNO =-=-=-=")

    nome = input("Digite o nome do aluno: ").strip()
    assinaturas_system = Assinaturas()

    assinatura = assinaturas_system.buscar_assinatura_por_nome(nome)
    if not assinatura:
        print("Erro: O aluno não possui uma assinatura ativa. Cadastre a assinatura primeiro.")
        return None

    try:
        peso = float(input("Digite o peso do aluno (kg): ").strip())
        altura = float(input("Digite a altura do aluno (m): ").strip())
        idade = int(input("Digite a idade do aluno: ").strip())
    except ValueError:
        print("Erro: Insira valores numéricos válidos para peso, altura e idade.")
        return None

    condicoes_medicas = input("Informe as condições médicas do aluno (separadas por vírgula, ou 'Nenhuma' se não houver): ").strip()
    condicoes_medicas = [] if condicoes_medicas.lower() == 'nenhuma' else [x.strip() for x in condicoes_medicas.split(',')]

    aluno = Aluno(nome, peso, altura, idade, condicoes_medicas)
    aluno.exibir_dados()
    aluno.questionario()  

    return aluno

if __name__ == "_main_":
    try:
        aluno1 = cadastrar_aluno()
        if aluno1:
            aluno1.exibir_dados()

            nova_senha = input("Digite a nova senha: ").strip()
            aluno1.alterar_senha(nova_senha)

            senha_teste = input("Digite a senha para verificação: ").strip()
            if aluno1.verificar_senha(senha_teste):
                print("Senha verificada com sucesso!")
            else:
                print("Senha incorreta.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
