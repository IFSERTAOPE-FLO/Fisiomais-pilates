#Classes : Instrutor, Administração
from datetime import datetime

class InstrutorPilates:
    def __init__(self, identificador, nome, formacao, telefone, email, dados_bancarios, senha):
        self.identificador = identificador
        self.nome = nome
        self.formacao = formacao
        self.telefone = telefone
        self.email = email
        self.dados_bancarios = dados_bancarios
        self.senha = senha
        self.agenda = {}
        self.aulas_ministradas = []
        self.avaliacoes_turmas = {}

    def adicionar_agendamento(self, turma, data, horario):
        if not isinstance(data, datetime):
            raise ValueError("O parâmetro 'data' deve ser do tipo datetime.")
        
        data_str = data.strftime('%Y-%m-%d')

        if data_str not in self.agenda:
            self.agenda[data_str] = []
        
        for agendamento in self.agenda[data_str]:
            if agendamento['horario'] == horario:
                raise ValueError(f"O horário {horario} já está ocupado.")
        
        self.agenda[data_str].append({
            'turma': turma,
            'horario': horario
        })
        print(f"Agendamento adicionado para {turma} em {data_str} às {horario}.")

    def registrar_aula_ministrada(self, turma, data, horario):
        if not isinstance(data, datetime):
            raise ValueError("O parâmetro 'data' deve ser do tipo datetime.")
        
        self.aulas_ministradas.append({
            'turma': turma,
            'data': data.strftime('%Y-%m-%d'),
            'horario': horario
        })
        print(f"Aula ministrada registrada: {turma}, {data.strftime('%Y-%m-%d')} às {horario}.")

    def aulas_ministradas_por_dia(self, data):
        if not isinstance(data, datetime):
            raise ValueError("O parâmetro 'data' deve ser do tipo datetime.")
        
        data_str = data.strftime('%Y-%m-%d')
        return sum(1 for aula in self.aulas_ministradas if aula.get('data') == data_str)

    def avaliar_turma(self, turma, avaliacao):
        self.avaliacoes_turmas[turma] = avaliacao
        print(f"Instrutor {self.nome} avaliou a  {turma} com: {avaliacao}")
        return f"A turma {turma} foi avaliada com: {avaliacao}"

    def listar_instrutores(self, lista_instrutores):
        nomes = [instrutor.nome for instrutor in lista_instrutores]
        print("Listando instrutores registrados:")
        for nome in nomes:
            print(nome)
        return nomes

instrutor1 = InstrutorPilates(
    identificador=1,
    nome="Alice Santos",
    formacao="Educação Física",
    telefone="(11) 91234-5678",
    email="alice.santos@clinica.com",
    dados_bancarios="Banco = 123, Agência: 4567, Conta: 890123-4",
    senha="senha123"
)

instrutor2 = InstrutorPilates(
    identificador=2,
    nome="Maya Barros",
    formacao="Educação Física",
    telefone="(11) 98765-4321",
    email="maya.barros@clinica.com",
    dados_bancarios="Banco = 456, Agência: 1234, Conta: 567890-1",
    senha="senha456"
)

hoje = datetime.now()

instrutor1.adicionar_agendamento("turma A", hoje, "10:00")
instrutor1.adicionar_agendamento("turma B", hoje, "11:00")

instrutor1.registrar_aula_ministrada("turma A", hoje, "10:00")
instrutor1.registrar_aula_ministrada("turma B", hoje, "11:00")

print(f"Número de aulas ministradas hoje ({hoje.strftime('%d-%m-%y')}): {instrutor1.aulas_ministradas_por_dia(hoje)}")

instrutor2.adicionar_agendamento("turma A", hoje, "10:00")
instrutor2.adicionar_agendamento("turma B", hoje, "11:00")

instrutor2.registrar_aula_ministrada("Turma A", hoje, "10:00")
instrutor2.registrar_aula_ministrada("turma B", hoje, "11:00")

print(f"Número de aulas ministradas hoje ({hoje.strftime('%d-%m-%y')}): {instrutor2.aulas_ministradas_por_dia(hoje)}")

instrutor1.avaliar_turma("Turma A", "Excelente")
instrutor2.avaliar_turma("Turma B", "Bom desempenho")

instrutores = [instrutor1, instrutor2]

instrutores_listados = instrutor1.listar_instrutores(instrutores)
print(instrutores_listados)



from datetime import datetime

class Administracao(Assinaturas):
    def __init__(self, senha, telefone, nivel_acesso):
        super().__init__()
        self.senha = senha
        self.telefone = telefone
        self.nivel_acesso = nivel_acesso
        self.turmas_gestionadas = []
        self.observacoes = []
        self.relatorios = {}
        self.instrutores = {}

    def cadastrar_instrutor(self, instrutor_id, nome, especialidade):
        if instrutor_id in self.instrutores:
            print(f"Erro: Instrutor com ID {instrutor_id} já cadastrado.")
            return
        self.instrutores[instrutor_id] = {
            'nome': nome,
            'especialidade': especialidade
        }
        print(f"Instrutor {nome} cadastrado com sucesso!")

    def listar_instrutores(self):
        print("Instrutores cadastrados:")
        for instrutor_id, dados in self.instrutores.items():
            print(f"ID: {instrutor_id}, Nome: {dados['nome']}, Especialidade: {dados['especialidade']}")

    def adicionar_turma(self, turma_id, instrutor_id, horario):
        if turma_id in self.turmas:
            print("Erro: Turma já existente.")
            return
        if instrutor_id not in self.instrutores:
            print("Erro: Instrutor não cadastrado.")
            return
        self.turmas[turma_id] = {
            'instrutor_id': instrutor_id,
            'horario': horario,
            'alunos': []
        }
        self.turmas_gestionadas.append(turma_id)
        print(f"Turma {turma_id} adicionada com sucesso!")

    def listar_turmas(self):
        print("Turmas existentes:")
        for turma_id, info in self.turmas.items():
            instrutor_nome = self.instrutores[info['instrutor_id']]['nome']
            print(f"Turma ID: {turma_id}, Instrutor: {instrutor_nome}, Horário: {info['horario']}")

    def adicionar_observacao(self, observacao):
        self.observacoes.append(observacao)
        print("Observação adicionada.")

    def gerar_relatorio(self, relatorio_id, descricao):
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.relatorios[relatorio_id] = {
            'descricao': descricao,
            'data': data
        }
        print(f"Relatório {relatorio_id} gerado em {data}.")

    def acessar_pagamentos(self):
        print("Lista de pagamentos pendentes e realizados:")
        for assinatura in self.assinaturas:
            print(assinatura)

    def acessar_agenda(self):
        print("Agenda de turmas e horários:")
        for turma_id, info in self.turmas.items():
            instrutor_nome = self.instrutores[info['instrutor_id']]['nome']
            print(f"Turma: {turma_id}, Instrutor: {instrutor_nome}, Horário: {info['horario']}")

# Exemplo de uso
admin = Administracao(senha="1234", telefone="(11) 98765-4321", nivel_acesso="Administrador")
admin.cadastrar_aluno(1, "João Silva")
admin.cadastrar_instrutor(101, "Carlos Souza", "Pilates Avançado")
admin.adicionar_turma("T01", 101, "Segundas e Quartas - 19h")
admin.listar_alunos()
admin.listar_instrutores()
admin.listar_turmas()
admin.adicionar_observacao("Revisar materiais de treino.")
admin.gerar_relatorio("R01", "Resumo mensal de atividades.")
admin.acessar_agenda()

