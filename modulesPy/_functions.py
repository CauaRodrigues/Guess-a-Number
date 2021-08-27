import os
import platform
import time
import random


def Clear():
    if platform.system() == 'Windows':
        os.system('cls')

    else:
        os.system('clear')

def Levels():

    print(
    """
        Dificuldade:    |Comando:    |Tentativas:   |Números:   

    --- Fácil           |-->> E      |07            |0 à 20     
    --- Médio           |-->> M      |10            |0 à 40     
    --- Difícil         |-->> H      |15            |0 à 65 

    --- Sair            |-->> exit
    --- Voltar ao Início|-->> exitmod

    """)

def Exit():
    check_exit = str(input('Tem certeza que deseja sair? [Y/n]\n-->> ')).strip().lower()
    Clear()

    while check_exit not in 'yn' or len(check_exit) != 1:
        print('Opção inválida. Tente novamente:')

        check_exit = str(input('Tem certeza que deseja sair? [Y/n]\n-->> ')).strip().lower()
        Clear()


    if check_exit == 'y':
        print('Pena que você tem que ir ;-;\nEspero poder encontrar você novamente :)')
        exit()
    
    elif check_exit == 'n':
        print('Que legal! Ainda bem que você decidiu ficar ^-^')
        return

def ExitMod():
    check_exitMod = str(input('Tem certeza de que deseja sair desse modo? O seu progresso não será salvo. [Y/n]\n-->> ')).strip().lower()
    Clear()

    while check_exitMod not in 'yn' or len(check_exitMod) != 1:
        print('Opção inválida. Tente Novamente:')
        check_exitMod = str(input('Tem certeza de que deseja sair desse modo? O seu progresso não será salvo. [Y/n]\n-->> ')).strip().lower()
        Clear()


    if check_exitMod == 'y':
        print('Saindo...')
        time.sleep(1.5)
        return True

    if check_exitMod == 'n':
        print('Ufa... Pensei que você iria desistir hahaha.')
        return False

def Timer():
    print('Tenha paciência...')
    time.sleep(3)

def RandomNumber(chosen_level):
    if chosen_level == 'E':
        number = random.randint(0, 20)
        return number
    
    elif chosen_level == 'M':
        number = random.randint(0, 40)
        return number
    
    elif chosen_level == 'H':
        number = random.randint(0, 65)
        return number

def Rules(chosen_level):

    rules = str(input('Antes de começarmos, você quer rever as regras desse nível? [Y/n] \n-->> ')).strip().lower()
    Clear()

    while rules == 'exit':
        Exit()

        rules = str(input('Você quer rever as regras desse nível? [Y/n] \n-->> ')).strip().lower()
        Clear()

    while rules not in 'yn' or len(rules) != 1:
        print('Opção inválida. Tente novamente:')
        rules = str(input('Você quer rever as regras desse nível? [Y/n] \n-->> ')).strip().lower()
        Clear()

        while rules == 'exit':
            Exit()

            rules = str(input('Você quer rever as regras desse nível? [Y/n] \n-->> ')).strip().lower()
            Clear()

    if rules == 'n':
        pass

    elif rules == 'y':

        if chosen_level == 'E':
            print(
            """
            _______________________________________________________________________________
            |                                                                             |
            |   Dificuldade: Fácil                                                        |
            |   Tentativas: 7                                                             |
            |   Números: 0 à 20                                                           |
            |                                                                             |
            |   Para sair do modo e voltar ao início: -->> exitmod                        |  
            |   Para sair do jogo: -->> exit                                              |
            |                                                                             |
            |   Obs: Os comandos para sair podem ser digitados a qualquer momento.        |
            |_____________________________________________________________________________|
            """
            )

            come_back = str(input('Pressione enter para voltar ao jogo... '))
            come_back = ''
            Clear()

            pass
        
        elif chosen_level == 'M':
            print(
            """
            _______________________________________________________________________________
            |                                                                             |
            |   Dificuldade: Médio                                                        |
            |   Tentativas: 10                                                             |
            |   Números: 0 à 40                                                           |
            |                                                                             |
            |   Para sair do modo e voltar ao início: -->> exitmod                        |  
            |   Para sair do jogo: -->> exit                                              |
            |                                                                             |
            |   Obs: Os comandos para sair podem ser digitados a qualquer momento.        |
            |_____________________________________________________________________________|
            """
            )

            come_back = str(input('Pressione enter para voltar ao jogo... '))
            come_back = ''
            Clear()

            pass
        
        elif chosen_level == 'H':

            print(
            """
            _______________________________________________________________________________
            |                                                                             |
            |   Dificuldade: Difícil                                                      |
            |   Tentativas: 15                                                             |
            |   Números: 0 à 65                                                           |
            |                                                                             |
            |   Para sair do modo e voltar ao início: -->> exitmod                        |  
            |   Para sair do jogo: -->> exit                                              |
            |                                                                             |
            |   Obs: Os comandos para sair podem ser digitados a qualquer momento.        |
            |_____________________________________________________________________________|
            """
            )

            come_back = str(input('Pressione enter para voltar ao jogo... '))
            come_back = ''
            Clear()

            pass

def ComparingNumber(chosen_level, number, chosen_number, attempt_number):
    
    if chosen_level == 'E':

        if chosen_number > number:
            print('\n ** Chute Alto ;-; ** \n')
        
            if chosen_number > 20:
                print('!!! PASSOU O LIMITE !!!')
                    
        elif chosen_number < number:
            print('\n ** Chute Baixo ): ** \n')

            if chosen_number < 0:
                print('!!! PASSOU O MÍNIMO !!!')
        
        elif chosen_number == number:

            if attempt_number == 1:
                print('\n ** Acertou de primeira, parabéns ** \n')
            
            elif attempt_number == 7:
                print('\n ** Quase perdeu hehe. Parabéns! ** \n')
            
            else:
                print('\n ** Parabéns!! Você acertou! ** \n')
            
            return True

    elif chosen_level == 'M':

        if chosen_number > number:
            print('\n ** Chute Alto ;-; ** \n')
        
            if chosen_number > 40:
                print('!!! PASSOU O LIMITE !!!')
                    
        elif chosen_number < number:
            print('\n ** Chute Baixo ): ** \n')

            if chosen_number < 0:
                print('!!! PASSOU O MÍNIMO !!!')
        
        elif chosen_number == number:

            if attempt_number == 1:
                print('\n ** Acertou de primeira, parabéns ** \n')
            
            elif attempt_number == 10:
                print('\n ** Quase perdeu hehe. Parabéns! ** \n')
            
            else:
                print('\n ** Parabéns!! Você acertou! ** \n')
            
            return True

    elif chosen_level == 'H':

        if chosen_number > number:
            print('\n ** Chute Alto ;-; ** \n')
        
            if chosen_number > 65:
                print('!!! PASSOU O LIMITE !!!')
                    
        elif chosen_number < number:
            print('\n ** Chute Baixo ): ** \n')

            if chosen_number < 0:
                print('!!! PASSOU O MÍNIMO !!!')
        
        elif chosen_number == number:

            if attempt_number == 1:
                print('\n ** Acertou de primeira, parabéns ** \n')
            
            elif attempt_number == 15:
                print('\n ** Quase perdeu hehe. Parabéns! ** \n')
            
            else:
                print('\n ** Parabéns!! Você acertou! ** \n')
            
            return True

def ShowData(chosen_level, number, attempt_number, try_list):

    if chosen_level == 'E':
        show_level = 'Fácil'
        try_limit = 7
    
    elif chosen_level == 'M':
        show_level = 'Médio'
        try_limit = 10
    
    elif chosen_level == 'H':
        show_level = 'Difícil'
        try_limit = 15
    
    print(
        f'Dificuldade: {show_level}\n'
        f'Número correto: {number}\n'
        f'Número de Tentativas: {attempt_number} / {try_limit}\n'
        f'Maior número tentado: {max(try_list)}\n'
        f'Menor número tentado: {min(try_list)}\n'
        f'Números tentados:')
    for numbers in try_list:
        print(numbers, end=' - ')

    print('\n')