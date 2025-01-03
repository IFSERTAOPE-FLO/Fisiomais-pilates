class Aluno(Anamnese, Assinaturas):
    def __init__(self, id, nome, peso, altura, condicoes, idade, senha):
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

        novo_peso = input("Digite o novo peso (ou pressione Enter para manter o atual): ")
        try:
            if novo_peso:
                self.peso = float(novo_peso)
        except ValueError:
            print("Valor inválido para peso. Use números decimais.")

        nova_altura = input("Digite a nova altura (ou pressione Enter para manter a atual): ")
        try:
            if nova_altura:
                self.altura = float(nova_altura)
        except ValueError:
            print("Valor inválido para altura. Use números decimais.")

        print(f"Dados do aluno {self.nome} alterados com sucesso!") # Mensagem de sucesso aqui

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} m")
        if self.condicoes:
            print(f"Condições médicas: {', '.join(self.condicoes)}")
        print(f"Idade: {self.idade}")




