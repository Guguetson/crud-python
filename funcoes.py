def cabecalho(): #definindo a função cabeçalho
  print("-"*50)
  print('Seja bem vindo ao meu programa de CRUD de jogadores do CR FLAMENGO!')

def cadastrar_dados(): #definindo a função cadastro
  try:
    with open('Dados.txt','a') as arquivo: #abre arquivo Dados.txt no modo de adicionar "a" para acrescentar novos dados
      nome=input("Digite o nome do(a) atleta: ") #declarando variáveis
      sexo=input("Digite o sexo do(a) atleta: ") #declarando variáveis
      nascimento=int(input("Insira o número do ano de nascimento do(a) atleta: ")) #declarando variáveis
      cidade=input("Digite a cidade que o(a) atleta reside: ") #declarando variáveis
      estado=input("Digite o estado que o(a) atleta reside: ") #declarando variáveis
      posicao=input("Digite a posição em que a(a) atleta atua: ") #declarando variáveis
      responsavel=input("Digite o nome do(a) responsável pelo(a) atleta: ")#declarando variáveis
      jogador= f"{nome}, {sexo}, {nascimento}, {posicao}, {cidade}, {estado}, {responsavel}, \n" #string formatada, com os dados preenchidos das variáveis
      arquivo.write(jogador) #escreve a string jogador no arquivo Dados.txt
      print("Dados cadastrados com sucesso!\n")
  except ValueError: #tratamento de erros
    print("Valor inválido! Certifique-se de digitar apenas valores númericos no ano de nascimento do(a) atleta.")
    print("Lembre-se que o preenchimento dos dados influencia diretamente na avaliação do(a) atleta, certifique-se de ser coerente e honesto ao preencher os dados.\n")
  except Exception as e: #tratamento de erros
    print("Ocorreu um erro ao cadastrar os dados: ",str(e))

def listar_dados(): #definindo a função listar
  try:
    arquivo=open('Dados.txt', 'r') #abre arquivo Dados.txt no modo de leitura "r"
    linhas=arquivo.readlines() #lê todas as linhas do arquivo e as armazena em uma lista chamada 'linhas'
    if not linhas: #verifica se tem elementos a lista linhas
      print("Nenhum dado cadastrado.\n")
    else:
      print("\nDados cadastrados: ")
      for linha in linhas: #percorre todas as linhas da minha lista
        dados=linha.strip().split(',') # .strip() remove espaços em branco no início e no final da linha e .split()separa os dados pela vírgula
        print("Nome: ", dados[0]) #printando baseado no índice dos elementos
        print("Sexo: ", dados[1])
        print("Ano de nascimento: ", dados[2])
        print("Posição: ", dados[3])
        print("Cidade: " ,dados[4])
        print("Estado: ", dados[5])
        print("Responsável: ", dados[6])
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
  except FileNotFoundError: #tratamento de erros
    print("Arquivo de dados não encontrado.\n")
  except Exception as e: #tratamento de erros
    print("Ocorreu um erro ao listar os dados: ", str(e))

def alterar_dados(): #definindo a função alterar
    try:
        with open('Dados.txt', 'r') as arquivo: #abre arquivo Dados.txt no modo de leitura "r"
            linhas=arquivo.readlines() #lê todas as linhas do arquivo e as armazena em uma lista chamada 'linhas'
        if not linhas: #verifica se tem elementos a lista linhas
            print("Nenhum dado foi cadastrado.")
            return #retorna da função caso nao tenha linhas

        nome=input("Digite o nome do(a) atleta que deseja alterar os dados: ") #solicita o nome do atleta a ser alterado.
        encontrado=False #variavel para verificar se o jogador foi encontrado

        with open("Dados.txt", "w") as arquivo: #abre arquivo Dados.txt no modo de escrita "w" para substituir os dados ja existentes
            for linha in linhas: #percorre todas as linhas da minha lista
                dados=linha.strip().split(',') #.strip() remove espaços em branco no início e no final da linha e .split()separa os dados pela vírgula
                if dados[0]==nome: #verifica se o nome na linha corresponde ao nome digitado
                    novo_nome=input("Digite o novo nome do(a) atleta: ") #pedindo novos dados para serem alterados
                    novo_sexo=input("Digite o novo sexo do(a) atleta: ")
                    novo_nascimento=int(input("Insira o número do ano de nascimento do(a) atleta: "))
                    novo_posicao=input("Digite a nova posição em que a(a) atleta atua: ")
                    nova_cidade=input("Digite a nova cidade que o(a) atleta reside: ")
                    novo_estado=input("Digite o novo estado que o(a) atleta reside: ")
                    novo_responsavel=input("Digite o novo nome do(a) responsável pelo(a) atleta: ")
                    alt_jogador= f"{novo_nome}, {novo_sexo}, {novo_nascimento}, {novo_posicao}, {nova_cidade}, {novo_estado}, {novo_responsavel},\n" #cria uma nova linha com os dados alterados
                    arquivo.write(alt_jogador) #escreve a string alt_jogador no arquivo Dados.txt com os dados alterados
                    encontrado=True  #indicando que o jogador foi encontrado e os dados foram alterados
                    print("Dados alterados com sucesso!\n")
                else:
                    arquivo.write(linha) #escreve a linha origina no arquivo

        if not encontrado:
             print("Nome do(a) atleta não encontrada nos cadastros.")
    except FileNotFoundError: #tratamento de erros
         print("Arquivo de dados não encontrado.\n")
    except Exception as e: #tratamento de erros
            print("Ocorreu um erro ao alterar os dados: ", str(e))

def excluir_dados(): #definindo a função excluir
  try:
    with open('Dados.txt', 'r') as arquivo: #abre arquivo Dados.txt no modo de leitura "r"
      linhas=arquivo.readlines() #lê todas as linhas do arquivo e as armazena em uma lista chamada 'linhas'
      if not linhas: #verifica se tem elementos a lista linhas
        print("Nenhum dado foi cadastrado.")
        return #retorna da funçao caso nao tenha linhas
    nome=input("Digite o nome do(a) atleta que deseja excluir os dados: ")
    encontrado=False
    with open('Dados.txt','w') as arquivo: #abre arquivo Dados.txt no modo de escrita "w" para substituir os dados ja existentes
      for linha in linhas: #percorre todas as linhas da minha lista
        dados=linha.strip().split(',') #.strip() remove espaços em branco no início e no final da linha e .split()separa os dados pela vírgula
        if dados[0]==nome: #verifica se o nome na linha corresponde ao nome digitado
          encontrado=True #indicando que o jogador foi encontrado e os dados foram excluidos
          print("Dados excluídos com sucesso!")
        else:
          arquivo.write(linha) #escreve a linha no arquivo, retirando a do atleta a ser excluído.
  except ValueError: #tratamento de erros
    print("Valor inválido! Certifique-se de digitar apenas valores númericos para a identidade do(a) atleta.")
  except FileNotFoundError: #tratamento de erros
    print("Arquivo de dados não encontrado.\n")
  except Exception as e: #tratamento de erros
    print("Ocorreu um erro ao alterar os dados: ", str(e))

def backup_dados(): #definindo a função backup
    try:
        with open("Dados.txt", "r") as arquivo_origem: #abre arquivo de origem Dados.txt no modo de leitura "r"
              with open("backup_Dados.txt", "w") as arquivo_backup: #abre o arquivo de backup Backup_Dados.txt no modo escrita "w"
                   conteudo = arquivo_origem.read() #lê todo o arquivo
                   arquivo_backup.write(conteudo) #escreve o conteudo lido no arquivo
        print("O backup do arquivo selecionado foi realizado com sucesso!")
    except FileNotFoundError: #tratamento de erros
        print("O arquivo de dados selecionado não encontrado.")
    except Exception as e: #tratamento de erros
        print("Ocorreu um erro ao realizar o backup dos dados:", str(e))

def sair(): #definindo a função sair
    try:
      print("Programa encerrado.")
    except Exception as e: #tratamento de erros
      print("Ocorreu um erro ao sair do programa: ", str(e))

def menu(): #definindo a função menu
  while True: #fica num loop infinito até que a opção sair(função) seja selecionada
    cabecalho()
    print("Escolha uma opção: \n")
    print("1 - Cadastrar Dados")
    print("2 - Listar Dados")
    print("3 - Alterar Dados")
    print("4 - Excluir Dados")
    print("5 - Realizar Backup do Arquivo")
    print("0 - Sair do programa")
    print("-"*30,"\n")

    try:
      opcao=int(input("Digite o número que corresponde a opção que você deseja executar: " ))

      if opcao==1:
        cadastrar_dados()
      elif opcao==2:
        listar_dados()
      elif opcao==3:
        alterar_dados()
      elif opcao==4:
        excluir_dados()
      elif opcao==5:
        backup_dados()
      elif opcao==0:
        sair()
        break; #sai do loop infinito, encerrando o menu
      else:
        print("Sua escolha está fora do menu de opções, por favor selecione um número que esteja dentro do menu de opções.\n")

    except ValueError: #tratamento de erros
      print("Valor inválido. Certifique-se de digitar apenas valores númericos que estão dentro das opções do menu.\n")
    except Exception as e: #tratamento de erros
      print("Ocorreu um erro ao executar o algoritmo: ", str(e))
