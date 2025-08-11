#  Configuração inicial e importações:
# Importação de bibliotecas necessárias

import os

# Lista de dicionários representando os restaurantes
restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina','categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print("""
𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼
    """ )

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Deletar um restaurante')
    print('5. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') # Limpa a tela (funciona apenas no Windows)
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Função para cadastrar um novo restuarante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    """

    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Função para listar todos os restaurantes cadastrados
    """
    exibir_subtitulo('Listando os restaurantes\n')

    print(f'{'nome_restaurante'.ljust(21)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Função para processar a escolha do usuário no menu
    """

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            # print('\nOpção 1 escolhida')
            # voltar_ao_menu_principal()
            cadastrar_novo_restaurante()
        if opcao_escolhida == 2:
            # print('\nOpção 2 escolhida\n')
            # voltar_ao_menu_principal()
            listar_restaurantes()
        if opcao_escolhida == 3:
            # print('\nOpção 3 escolhida')
            # voltar_ao_menu_principal()
            alterar_estado_do_restaurante()
        if opcao_escolhida == 4:
            deletar_restaurante()
        if opcao_escolhida == 5:
            # print('\nOpção 4 escolhida')
            # voltar_ao_menu_principal()
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def alterar_estado_do_restaurante():
    """
    Função para ativar ou desativar um restaurante
    """
    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Inverte o estado (Ex. False para True)
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def deletar_restaurante():
    """
    Função para deletar um restaurante
    """
    exibir_subtitulo('Deletando um restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja deletar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            deletar = input(f'Você tem certeza que deseja deletar o restaurante {nome_restaurante}?\nResponda:\nSim ou Não\n')

            if deletar == 'Sim':
                restaurantes.remove(restaurante)
                mensagem = f'O restaurante {nome_restaurante} foi deletado com sucesso!'
            elif deletar == 'Não':
                mensagem = 'Operação cancelada'
            else:
                mensagem = 'Opção invalida'
            
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def main():
    """
    Função principal que inicia o programa
    """
    os.system('cls') # Limpa a tela (funciona apenas no Windows)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


