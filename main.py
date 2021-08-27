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
    

    while chosen_level == 'E':
        print('Ok, vamos no fácil então.')
        fun.Rules(chosen_level)
        print('Chega de enrolação, vamos começar!\n')

        print('Escolhendo o número...')
        number = fun.RandomNumber(chosen_level)
        fun.Timer()
        fun.Clear()
        print('Número escolhido! Agora é com você!\n')
        try_list = []

        for attempts in range (1, 8):
            attempt_number = attempts
            print('Números: 0 à 20')
            print(f'Tentativas restantes: {attempts} / 7')

            chosen_number = input('Tente acertar o número\n-->> ').strip().upper()
            fun.Clear()

            if not chosen_number.isdigit():
                if chosen_number == 'EXIT':
                    fun.Exit()
                    win = False
                    chosen_number = 0

                elif chosen_number == 'EXITMOD':
                    if fun.ExitMod():
                        change_mode = True
                        break

                    win = False
                    chosen_number = 0

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
            break

        if not win:
            print('Não desista! Você pode tentar de novo!\n')
            fun.ShowData(chosen_level, number, attempt_number, try_list)

        elif win:
            fun.ShowData(chosen_level, number, attempt_number, try_list)
        
        replay = str(input('Deseja jogar novamente? [Y/n]\n-->> ')).strip().lower()
        fun.Clear()

        while replay not in 'yn':
            print('Ops... Você não digitou uma opção válida. Tente de novo:') 
            replay = str(input('Deseja jogar nesse modo novamente? [Y/n]\n-->> ')).strip().lower()
            fun.Clear()

        if replay == 'y':
            continue

        while replay == 'n':
            exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
            fun.Clear()

            while exit_or_return not in 'yn':
                print('Ops... Você não digitou uma opção válida. Tente de novo:')
                exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
                fun.Clear()
            
            if exit_or_return == 'y':
                fun.Exit()
                pass

            elif exit_or_return == 'n':
                change_mode = True
                break

        if change_mode:
            break
    
    while chosen_level == 'M':
        print('Certo! Dificuldade média, boa escolha.')
        fun.Rules(chosen_level)
        print('Chega de enrolação, vamos começar!\n')

        print('Escolhendo o número...')
        number = fun.RandomNumber(chosen_level)
        fun.Timer()
        fun.Clear()
        print('Número escolhido! Agora é com você!\n')
        try_list = []

        for attempts in range (1, 11):
            attempt_number = attempts
            print('Números: 0 à 40')
            print(f'Tentativas restantes: {attempts} / 10')

            chosen_number = input('Tente acertar o número\n-->> ').strip().upper()
            fun.Clear()

            if not chosen_number.isdigit():
                if chosen_number == 'EXIT':
                    fun.Exit()
                    win = False
                    chosen_number = 0

                elif chosen_number == 'EXITMOD':
                    if fun.ExitMod():
                        change_mode = True
                        break

                    win = False
                    chosen_number = 0

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
            break

        if not win:
            print('Não desista! Você pode tentar de novo!\n')
            fun.ShowData(chosen_level, number, attempt_number, try_list)

        elif win:
            fun.ShowData(chosen_level, number, attempt_number, try_list)
        
        replay = str(input('Deseja jogar novamente? [Y/n]\n-->> ')).strip().lower()
        fun.Clear()

        while replay not in 'yn':
            print('Ops... Você não digitou uma opção válida. Tente de novo:') 
            replay = str(input('Deseja jogar nesse modo novamente? [Y/n]\n-->> ')).strip().lower()
            fun.Clear()

        if replay == 'y':
            continue

        while replay == 'n':
            exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
            fun.Clear()

            while exit_or_return not in 'yn':
                print('Ops... Você não digitou uma opção válida. Tente de novo:')
                exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
                fun.Clear()
            
            if exit_or_return == 'y':
                fun.Exit()
                pass

            elif exit_or_return == 'n':
                change_mode = True
                break

        if change_mode:
            break
    
    while chosen_level == 'H':
        print('Olha! Parece que temos alguém que gosta de desafios.')
        fun.Rules(chosen_level)
        print('Chega de enrolação, vamos começar!\n')

        print('Escolhendo o número...')
        number = fun.RandomNumber(chosen_level)
        fun.Timer()
        fun.Clear()
        print('Número escolhido! Agora é com você!\n')
        try_list = []

        for attempts in range (1, 16):
            attempt_number = attempts
            print('Números: 0 à 65')
            print(f'Tentativas restantes: {attempts} / 15')
        
            chosen_number = input('Tente acertar o número\n-->> ').strip().upper()
            fun.Clear()

            if not chosen_number.isdigit():
                if chosen_number == 'EXIT':
                    fun.Exit()
                    win = False
                    chosen_number = 0

                elif chosen_number == 'EXITMOD':
                    if fun.ExitMod():
                        change_mode = True
                        break

                    win = False
                    chosen_number = 0

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
            break

        if not win:
            print('Não desista! Você pode tentar de novo!\n')
            fun.ShowData(chosen_level, number, attempt_number, try_list)

        elif win:
            fun.ShowData(chosen_level, number, attempt_number, try_list)
        
        replay = str(input('Deseja jogar novamente? [Y/n]\n-->> ')).strip().lower()
        fun.Clear()

        while replay not in 'yn':
            print('Ops... Você não digitou uma opção válida. Tente de novo:') 
            replay = str(input('Deseja jogar nesse modo novamente? [Y/n]\n-->> ')).strip().lower()
            fun.Clear()

        if replay == 'y':
            continue

        while replay == 'n':
            exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
            fun.Clear()

            while exit_or_return not in 'yn':
                print('Ops... Você não digitou uma opção válida. Tente de novo:')
                exit_or_return = str(input('O que você deseja fazer? Sair do jogo ou ir para o início? [Y] para sair, [n] para voltar ao ínicio\n-->> ')).strip().lower()
                fun.Clear()
            
            if exit_or_return == 'y':
                fun.Exit()
                pass

            elif exit_or_return == 'n':
                change_mode = True
                break

        if change_mode:
            break

    


    if change_mode:
        continue

    break