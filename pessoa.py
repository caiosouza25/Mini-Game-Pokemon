import random

from time import sleep

from Pokemon import *

nomes = ['gary', 'misty', 'brok', 'jessy', 'james', 'ash', 'may']
POKEMONS = [
    PokemonAgua('gyarados'),
    PokemonAgua('blastoise'),
    PokemonAgua('lapras'),
    PokemonFogo('charizard'),
    PokemonFogo('rapidash'),
    PokemonFogo('ninetales'),
    PokemonEletrico('electabuzz'),
    PokemonEletrico('pikachu'),
    PokemonEletrico('magneton')
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(nomes)

        self.pokemons = pokemons
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'{self} possui os seguintes pokemons: ')
            for indice, pokemon in enumerate(self.pokemons):
                print(f'{indice} - {pokemon}')
        else:
            print(f'{self} nao tem nenhum pokemon')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERROR: o jogador nao possui nenhum pokemon')

    def mostra_dinheiro(self):
        print(f'vc possui R${self.dinheiro}')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f'vc ganhou R${quantidade}')

    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()
        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha!')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha')
                    break
        else:
            print('essa batalha nao pode ocorrer!')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = (input('escolha uma opçao: ')).strip()
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} eu escolho vc !!!')
                    return pokemon_escolhido
                except:
                    print('escolha invalida')
        else:
            print('ERROR: esse jogador nao possui nenhum pokemon')

    def explorar(self):
        print(f'explorando floresta em busca de novos pokemons...')
        sleep(2)
        if random.random() <= 0.4:
            pokemon = random.choice(POKEMONS)
            print(f'um {pokemon} selvagem apareceu!')
            resposta = str(input('Deseja capturar esse pokemon ? [S/N]: ')).upper().strip()[0]
            if resposta == 'S':
                chance = random.random()
                print('Pokebola vai...')
                sleep(3)
                if chance <= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f'lamento a pokebola falhou. o {pokemon} fugiu')
            elif resposta == 'N':
                print('OK, Boa viagem')
            else:
                print('devido ao seu comando invalido, o pokemon fugiu :/')
                print('acorda pro mundo JOWWWW! fica ae panguando rsrsrs')
        else:
            print('infelizmente, nesse mato nao tem grilo rsrs..')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            poke_alea = []
            for i in range(random.randint(1, 6)):
                pokerandom = random.choice(POKEMONS)
                poke_alea.append(pokerandom)

            super().__init__(nome=nome, pokemons=poke_alea)

        else:
            super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERROR: o jogador nao possui nenhum pokemon')
