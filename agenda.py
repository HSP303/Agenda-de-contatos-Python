AGENDA  = {}

def mostrar_contato():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print()
    else:
        print('>>>> Agenda vazia')


def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print("Telefone:", AGENDA[contato]["tel"])
        print("Email:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"]) 
    except KeyError:
        print()
        print('>>> Contato {} inexistente'.format(contato))
        print()
    except Exception as error:
        print('>>> Um erro inesperado ocorreu')
        print(error)



def ler_detalhes():
    tel = input('Digite o telefone:')
    email = input('Digite o Email:')
    endereco = input('Digite o Endereço:')
    return tel,email,endereco 


def inserir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel':tel,
        'email':email,
        'endereco':endereco,
    }
    save()



def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        save()
        print('>>>>Contato {} excluido com sucesso'.format(contato))
    except KeyError:
        print()
        print('>>> Contato {} inexistente'.format(contato))
        print()
    except Exception as error:
        print('>>> Um erro inesperado ocorreu')
        print(error)

def imprimir_menu():
    print('------------------------------------------------')
    print('1-Mostrar todos os contatos')
    print('2-Buscar contato')
    print('3-Incluir contato')
    print('4-Editar contato')
    print('5-Excluir contato')
    print('6-Exportar agenda para arquivo CSV')
    print('7-Importar arquivo CSV')
    print('0-Fechar agenda')
    print('------------------------------------------------')


def exportar_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'x') as file:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write('{},{},{},{} \n'.format(contato, tel, email, endereco))
            
        print('>>>> Agenda exportada com sucesso')

    except FileExistsError as erro:
        print('>>>> Arquivo não encontrado')



def importar_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                inserir_editar_contato(nome, tel, email, endereco)
        

    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Ocourreu um erro')
        print(error)


def save():
    with open( 'database.csv', 'w') as file:
                for contato in AGENDA:
                    tel = AGENDA[contato]['tel']
                    email = AGENDA[contato]['email']
                    endereco = AGENDA[contato]['endereco']
                    file.write('{},{},{},{} \n'.format(contato, tel, email, endereco))


def load():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                
                AGENDA[nome] = {
                'tel':tel,
                'email':email,
                'endereco':endereco,
                }
        
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('>>>> Ocourreu um erro')
        print(error)



load()

while True:
    imprimir_menu()

    print()
    opcao = input('Digite uma opção: ')
    print()

    if opcao == '1':
        mostrar_contato()
        print()
    
    elif opcao == '2':
        contato = input('Digite o contato: ')
        print()
        buscar_contato(contato)
        print()
    
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>> O contato {} já existe'.format(contato))
        except:
            tel,email,endereco = ler_detalhes()
            inserir_editar_contato(contato, tel, email, endereco)
            print('>>>> O contato {} foi adicionado com sucesso'.format(contato))
        print()
    
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>> Editando o contato {}'.format(contato))
            print()
            tel,email,endereco = ler_detalhes()
            inserir_editar_contato(contato, tel, email, endereco)
            print('>>>> O contato {} foi editado com sucesso'.format(contato))
        except:
            print('>>>> O contato {} não existe'.format(contato))
        print()
    
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        print()
        excluir_contato(contato)
    
    elif opcao == '6':
        arquivo = input('Digite qual será o nome do arquivo: ')
        exportar_csv(arquivo)

    elif opcao == '7':
        arquivo = input('Digite o nome do arquivo: ')
        importar_csv(arquivo)
    
    elif opcao == '0':
        print('Fechando o programa...')
        break
   
    else:
        print('Opção inválida')
        print()

