from .persistencia import salvar_paciente, salvar_consulta, carregar_pacientes, carregar_consultas, deletar_consulta

class Menu:
    def __init__(self, session):
        self.session = session

    def exibir_menu(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Cadastrar Paciente")
            print("2. Marcar Consulta")
            print("3. Cancelar Consulta")
            print("4. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.cadastrar_paciente()
            elif opcao == "2":
                self.marcar_consulta()
            elif opcao == "3":
                self.cancelar_consulta()
            elif opcao == "4":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_paciente(self):
        nome = input("Digite o nome do paciente: ")
        telefone = input("Digite o telefone do paciente: ")
        salvar_paciente(self.session, nome, telefone)
        print("Paciente cadastrado com sucesso!")

    def listar_pacientes(self):
        pacientes = carregar_pacientes(self.session)
        for idx, paciente in enumerate(pacientes, start=1):
            print(f"{idx}. {paciente.nome} - {paciente.telefone}")
        return pacientes

    def marcar_consulta(self):
        print("\n=== Pacientes Cadastrados ===")
        pacientes = self.listar_pacientes()
        paciente_idx = int(input("Digite o número do paciente: ")) - 1

        if 0 <= paciente_idx < len(pacientes):
            paciente_id = pacientes[paciente_idx].id
            data = input("Digite a data da consulta (DD/MM/YYYY): ")
            hora = input("Digite a hora da consulta (HH:MM): ")
            especialidade = input("Digite a especialidade desejada: ")
            salvar_consulta(self.session, paciente_id, data, hora, especialidade)
            print("Consulta marcada com sucesso!")
        else:
            print("Número de paciente inválido.")

    def listar_consultas(self):
        consultas = carregar_consultas(self.session)
        for idx, consulta in enumerate(consultas, start=1):
            paciente_nome = consulta.paciente.nome
            print(f"{idx}. {paciente_nome} - {consulta.data} {consulta.hora} - {consulta.especialidade}")
        return consultas


    def cancelar_consulta(self):
        print("\n=== Consultas Marcadas ===")
        consultas = self.listar_consultas()
        consulta_idx = int(input("Digite o número da consulta a ser cancelada: ")) - 1

        if 0 <= consulta_idx < len(consultas):
            consulta_id = consultas[consulta_idx].id
            print(f"Consulta de {consultas[consulta_idx].paciente.nome} em {consultas[consulta_idx].data} às {consultas[consulta_idx].hora} para {consultas[consulta_idx].especialidade}.")
            confirmar = input("Tem certeza que deseja cancelar esta consulta? (s/n): ")
            if confirmar.lower() == 's':
                deletar_consulta(self.session, consulta_id)
                print("Consulta cancelada com sucesso!")
            else:
                print("Cancelamento abortado.")
        else:
            print("Número de consulta inválido.")
