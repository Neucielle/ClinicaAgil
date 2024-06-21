from clinica.persistencia import inicializar_banco, session
from clinica.menu import Menu

def main():
    inicializar_banco()
    menu = Menu(session)
    menu.exibir_menu()

if __name__ == "__main__":
    main()
