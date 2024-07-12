import os

def titulo():
    print("𝓞𝓼 𝓟𝓪𝓼𝓼𝓪 𝓕𝓸𝓶𝓮")

def menu_iniciar():
    print('Escolha uma opção\n')
    print('1. Entrar como administrador.\n')
    print('2. Entrar como operador.\n')
    print('3. Entrar como Produção.\n')
    print('4. Finalizar app\n')

#def exibir_subtitulo(texto):
#    os.system('cls')
#    linha  = '*' *(len(texto) + 1)
#    print(linha)
#    print(texto)
#    print(linha)
#    print()

def opcao_invalida():
    main()

def mensagem_entrada(tipo_usuario):
    print()
    print(f'Entrou como {tipo_usuario}.')
    print()

def entrar_como_administrador():
    mensagem_entrada('Administrador')

def entrar_como_operador():
    mensagem_entrada('Operador')

def entrar_como_producao():
    mensagem_entrada('Producao')

def finalizar_app():
    print('Finalizando aplicativo...')
    exit()
    print()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1: 
            entrar_como_administrador()
        elif opcao_escolhida == 2: 
            entrar_como_operador()
        elif opcao_escolhida == 3: 
            entrar_como_producao()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            print('Opção inválida. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
        print()

def main():
    titulo()
    menu_iniciar()
    escolher_opcao()

if __name__ == "__main__":
    main()
