from pessoa import *


def linha(msg):
    print(f'  {msg:}')
    tot = len(msg) + 4
    print('~'*tot)


def escolher_inicial(player):
    print('escolha um pokemon para iniciar sua aventura!')

    pikachu = PokemonEletrico('pikachu', level=1)
    charmander = PokemonFogo('charmander', level=1)
    squirtle = PokemonAgua('squirtle', level=1)

    print('vc possui 3 escolhas')
    print('[1]', pikachu)
    print('[2]', charmander)
    print('[3]', squirtle)

    while True:
        escolha = int(input('escolha uma opçao: '))
        if escolha == 1:
            player.capturar(pikachu)
            break
        elif escolha == 2:
            player.capturar(charmander)
            break
        elif escolha == 3:
            player.capturar(squirtle)
            break
        else:
            print('opçao invalida')


if __name__ == "__main__":
    linha('Mini Game De Pokemon!')

    nome = input('digite seu nome: ')
    print(f'Ola {nome}. Bem vindo ao universo de POKEMON!')
    print('sua missao e se tornar um grande mestre Pokemon, Boa sorte em sua jornada!')
    jogador = Player(nome)
    if jogador.pokemons:
        print('vi que vc ja possui alguns pokemons.. ')
    else:
        print('vc nao possui nenhum pokemon')
        escolher_inicial(jogador)
    print('OK. hoje sua batalha sera com meu subrinho gary, ele é iniciante,'
          'acredito que sera uma otima experiencia para voces.')
    gary = Inimigo(nome='gary', pokemons=[PokemonAgua('squirtle', level=1)])
    jogador.batalhar(gary)
    print('=-'*25)
    print('Ok. vc esta livre pra ir, Boa sorte!')

    while True:
        print('~'*16)
        linha('Menu Do Game')
        print(f'carteira atual: R${jogador.dinheiro}')
        print('=-'*17)
        print('[1] explorar o mapa')
        print('[2] batalhar com inimigos')
        print('[3] pokebag')
        print('[4] sair do jogo')
        resp = input('o que vc desaja fazer ? ').strip()
        if resp == '1':
            jogador.explorar()
        elif resp == '2':
            inimigo_ghost = Inimigo()
            jogador.batalhar(inimigo_ghost)
        elif resp == '3':
            jogador.mostrar_pokemons()
        elif resp == '4':
            print('FECHANDO O JOGO...')
            break
        else:
            print('ERROR: opçao invalida!')
            print('ta com o cu dando BOT ?')
