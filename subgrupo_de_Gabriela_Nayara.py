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
