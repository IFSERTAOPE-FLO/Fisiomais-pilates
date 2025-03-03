from subgrupo_de_Deborah import Anamnese, AssinaturaPilates, Assinaturas
from teste import SistemaLogin


def menu():
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
            nome = input("Digite o nome do aluno: ")
            assinaturas.cadastrar_aluno(nome)
        elif opcao == "2":
            aluno_id = input("Digite o ID do aluno: ")
            tipo = input("Digite o tipo de assinatura (diariamente, semanal, mensal, anual): ").lower()
            data_inicio = input("Digite a data de início (DD/MM/YYYY ou YYYY-MM-DD): ")
            assinaturas.adicionar_assinatura(aluno_id, tipo, data_inicio)
        elif opcao == "3":
            aluno_id = input("Digite o ID do aluno cuja assinatura deseja cancelar: ")
            assinaturas.cancelar_assinatura(aluno_id)
        elif opcao == "4":
            aluno_id = input("Digite o ID do aluno cuja assinatura deseja renovar: ")
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



#MENU :



def menu_1(): 
 while True:
  print("=-="*20)
  print('''\n          =- ! Bem-vindo ao Studio de Pilates ! -=
        
                              -
        
1 - Cadastro
2 - Login
3 - Sair 
        
''')
  print("=-="*20)

  opcao = int(input("\nEscolha uma opção : "))



  match opcao:
   case 1:
    user_assinatura = AssinaturaPilates(None, "anual", data_inicio="2025-01-19")
    user_dados = Anamnese(None, None, None, None, None, None, None, None)
    user_dados.questionario()
    menu()
    pass
     

   case 2:
    aluno_id = str(input("Digite o ID do aluno: "))
    senha = str(input("Digite a senha: "))
    login_sistema = SistemaLogin()
    if login_sistema.login(aluno_id, senha):
        menu()
    pass

   
   case 3:
    break
 

   case _:
    pass
     
menu_1()