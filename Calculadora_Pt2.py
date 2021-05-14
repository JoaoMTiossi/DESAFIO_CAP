
from datetime import datetime

def exibir_menu():
    
    print('''
    -------------------- Menu --------------------
        
                1. Cadastrar um Anuncio
                2. Procurar por Anuncio
                3. Procurar por Data
                4. Formatação de dados
        
    ----------------------------------------------
    ''')
    
def exibir_dados():
    
    print('''
    -------------- FORMATO DE DADOS --------------
            
            Nomes - Todos os formatos aceitos
            Nome Anuncio - Todos os formatos aceitos
            Datas -  dd/mm/aa        
            Investimento - Numeros
        
        
    ----------------------------------------------
    ''')

def cadastrar(Anuncios):
    try:
        Nome = input('Digite seu nome: ')
        NomeAnuncio = input('Digite o nome do seu Anuncio: ')
        Data0 = (input('Digite a data inicial: '))
        Data0 = datetime.strptime(Data0,'%d/%m/%Y')
        Data1 = input('Digite a data final: ')
        Data1 = datetime.strptime(Data1,'%d/%m/%Y')
        Investimento = int(input('Digite o valor de investimento diario: '))
        Datafim = int((Data1 - Data0).days* int(Investimento))
        Anuncios.append((Nome, NomeAnuncio, Data0, Data1, Investimento, Datafim))
    
    
        print("---------- Cadastro Realizado com Sucesso! ----------")
    except:
         print(f'\033[0;31mERRO:voce digitou algum valor invalido!\033[m')
         print(f'\033[0;31mPara saber os formatos selecione a opção 4 no menu\033[m')

def PesquisaData(Anuncios):
    try:
        Data0_desejada = input('Digite a data INICIAL de pesquisa: ')
        Data0_desejada = datetime.strptime(Data0_desejada,'%d/%m/%Y')
        Data1_desejada = input('Digite a data FINAL de pesquisa: ')
        Data1_desejada = datetime.strptime(Data1_desejada,'%d/%m/%Y')
    
        for Datafiltro in Anuncios:
            Nome, NomeAnuncio, Data0, Data1, Investimento, Datafim = Datafiltro
            if Data0_desejada <= Data0 <= Data1_desejada:
                
                
                VALOR = Datafiltro[5]
                VIEW = VALOR * 30 
                PLUS = VIEW
                SHARECONTA = 0
            
                while SHARECONTA < 4:
            
                    CLIQUE = PLUS * 0.12
                    SHARE = CLIQUE*0.15
                    PLUS = SHARE*40
                    
                    VIEW = VIEW + PLUS
                    SHARECONTA = SHARECONTA + 1 
                
                print ("\n-----------------------------------------------------------------------------\n")
                print ("- A quantidade max. de visualizações é de aproximadamente: %.0f" % VIEW)        
                print ("- A quantidade max. de cliques é de aproximadamente: %.0f" %CLIQUE)
                print ("- A quantidade max. Compartilhamentos é de aproximadamente: %.0f" %SHARE)
                print ("- A quantidade total investida é de: ",Datafim)
                print ("\n-----------------------------------------------------------------------------")
            
            else:
                print("\nCaso seu anuncio não esteja a cima, o mesmo não foi encontrado. Pesquise novamente!\n")
    except:
         print(f'\033[0;31mERRO:voce digitou algum valor invalido!\033[m')
         print(f'\033[0;31mPara saber os formatos selecione a opção 4 no menu\033[m')


def PesquisaAnuncio(Anuncios):
    Anuncio_Desejado = input('Digite o nome do ANUNCIO desejado: ')
    for Anuncio in Anuncios:
        Nome, NomeAnuncio, Data0, Data1, Investimento, Datafim = Anuncio
        if NomeAnuncio == Anuncio_Desejado:
                        
            VALOR = Anuncio[5]
            VIEW = VALOR * 30 
            PLUS = VIEW
            SHARECONTA = 0
        
            while SHARECONTA < 4:
        
                CLIQUE = PLUS * 0.12
                SHARE = CLIQUE*0.15
                PLUS = SHARE*40
                
                VIEW = VIEW + PLUS
                SHARECONTA = SHARECONTA + 1 
            
    
            print ("\n-----------------------------------------------------------------------------\n")
            print ("- A quantidade max. de visualizações é de aproximadamente: %.0f" % VIEW)        
            print ("- A quantidade max. de cliques é de aproximadamente: %.0f" %CLIQUE)
            print ("- A quantidade max. Compartilhamentos é de aproximadamente: %.0f" %SHARE)
            print ("- A quantidade total investida é de: ",Datafim)
            print ("\n-----------------------------------------------------------------------------")
        
        
        else:
            print("\nCaso seu anuncio não esteja a cima, o mesmo não foi encontrado. Pesquise novamente!\n")

def sair():
   exit()


def main():
    
    def validarEntrada (msg):
        válido = False
        while not válido:
            entrada = str(input(msg)).replace(',','.').strip()
            if entrada.isalpha() or entrada =='':
                print(f'\033[0;31mERRO:\"{entrada}\" é um valor invalido!\033[m')
                print(f'\033[0;31mDigite um valor valido!\033[m')
            else:
                válido = True
                return float(entrada)
        
    Anuncios = []

    while True:
        exibir_menu()
        opcao = validarEntrada ("Digite a opçao desejada: ")
        if opcao == 1:
            cadastrar(Anuncios)
        elif opcao == 2:
            PesquisaAnuncio(Anuncios)
        elif opcao == 3:
            PesquisaData(Anuncios)
        elif opcao == 4:
            exibir_dados() 
        else:
            print(f'\033[0;31mERRO:\"{opcao}\" é um valor invalido!\033[m')
            print(f'\033[0;31mDigite um valor valido!\033[m')
        
                
            

main()