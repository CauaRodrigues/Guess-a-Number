from modulesPy import _functions as fun

while True:
    fun.Clear()

    print(
        """
        G U E S S   A   N U M B E R
        """
    )

    print('Seja muito bem vindo(a) ao Guess a Number.\nVamos começar escolhendo qual nivel de jogo você deseja jogar.\nNíveis disponíveis:')
    fun.Levels()

    chosen_level = str(input('E ai? Qual nível você escolhe? Digite o comando do nível para escolher.\n-->> ')).strip().upper()

    fun.Clear()

    while chosen_level == 'EXIT':
        fun.Exit()
        print('Escolha o modo e continue para jogar.\n')

        fun.Levels()
        chosen_level = str(input('E ai? Qual nível você escolhe? Digite o comando do nível para escolher.\n-->> ')).strip().upper()

        fun.Clear()


    while chosen_level not in 'EMH' or len(chosen_level) != 1:
        print('Você não digitou uma opção válida!')
        fun.Levels()

        chosen_level = str(input('Digite novamente.\n-->> ')).strip().upper()
        fun.Clear()

        while chosen_level == 'EXIT':
            fun.Exit()
            print('Escolha o modoe continue para jogar.\n')

            fun.Levels()
            chosen_level = str(input('E ai? Qual nível você escolhe? Digite o comando do nível para escolher.\n-->> ')).strip().upper()

            fun.Clear()
    

    if chosen_level == 'E':
        print('Ok, vamos no fácil então.')
        fun.Rules(chosen_level)
        print('Chega de enrolação, vamos começar!\n')

        print('Escolhendo o número...')
        number = fun.RandomNumber()
        fun.Timer()
        fun.Clear()
        print('Número escolhido! Agora é com você!\n')
        try_list = list()

        for attempts in range (1, 8):
            attempt_number = attempts
            print(f'Tentativas restantes: {attempts} / 7')
            print(number)

            chosen_number = input('Tente acertar o número\n-->> ').strip().upper()
            fun.Clear()

            if not chosen_number.isdigit():
                if chosen_number == 'EXIT':
                    fun.Exit()

                elif chosen_number == 'EXITMOD':
                    if fun.ExitMod():
                        change_mode = True
                        break

                else:
                    print('#### Digite apenas números inteiros! ####\n')
                    change_mode = False
                    win = False
                    chosen_number = 0

            elif chosen_number.isdigit():
                change_mode = False

                chosen_number = int(chosen_number)

                if fun.ComparingNumber(chosen_level, number, chosen_number, attempt_number):
                    win = True
                    try_list.append(chosen_number)
                    break
                
                else:
                    win = False
                    pass

            try_list.append(chosen_number)
 
        
        if change_mode:
            continue

        if not win:
            print('Não desista! Você pode tentar de novo!\n')
            fun.ShowData(chosen_level, number, attempt_number, try_list)

        elif win:
            fun.ShowData(chosen_level, number, attempt_number, try_list)
        
        replay = str(input('Deseja tentar de novo? [Y/n]\n-->> '))

        

    
    elif chosen_level == 'M':
        print('Certo! Dificuldade média, boa escolha.')
        fun.Rules(chosen_level)
        
        print('ok')
    
    elif chosen_level == 'H':
        print('Olha! Parece que temos alguém que gosta de desafios.')
        fun.Rules(chosen_level)

        print('ok')

    break