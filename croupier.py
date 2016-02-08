# -*- coding: utf-8 -*-
"""
controla uma rodada de poker
collect_ant = coleta o ant dos jogadores
collect bind = coleta o smal e o big blind
receives_card = distribui cartas para os jogadores
betting = controla a rodada de apostas
do_action = metodo que o jogador decide qual acao tomar
winners = define o jogador
pay = paga o pote aos vencedores
"""
import copy
import itertools
from player import Player
from poker import *


class TexasHoldem(object):
    """
    uma rodada de poker

    """
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    
    players = [] #dealer is first position
    flop = []
    pot = 0
    ant = 0
    smallblind = 0
    bigblind = 0

    def __init__(self, players, smallblind, bigblind, ant):
        """ """
        self.smallblind = smallblind
        self.bigblind = bigblind
        self.ant = ant
        self.players = players

    def transaction(self, player, payment, ant=False):
        """ operacao de transacao do player com o pot da rodada """
        value_transaction = 0
        if player.stack > payment-player.paid:
            player.stack -= payment-player.paid
            self.pot += payment-player.paid
            value_transaction = payment
            player.allin = False
            if not ant: player.paid = payment #ant nao conta
        elif player.stack < payment-player.paid:
            self.pot = player.stack
            value_transaction = player.stack
            player.stack = 0
            player.allin = True
            if not ant: player.paid = player.stack

            #player_handpot = self.pot
        return value_transaction
    ### devolve cartas do deck
    def draw(self, deck, n): 
        return [deck.pop(0) for i in xrange(0, n)]

    def collect_ant(self, player):
        """ coleta os valores do ant e coloca no pote """
        #zera variavel paid dos players
        for player in itertools.ifilter(lambda player: player.active, self.players):
            player.paid = 0
        self.transaction(player, self.ant, ant=True)



    def collect_blind(self):
        """ coleta os valores do blind e smallblind e coloca no pote """
        for pos, player in enumerate(self.players):
            if pos == 0:
                blind = self.smallblind
                player.smallblind = True
                player.blind = False
            elif pos == 1:
                blind = self.bigblind
                player.smallblind = False
                player.blind = True
            else:
                blind = 0
                player.paid = 0
                player.smallblind = player.blind = player.allin = False
            #paga o small e o blind
            self.transaction(player, blind)


    def receives_card(self, player):
        """ distribui as cartas para os jogadores
        """
        player.cards = self.draw(self.deck, 2)

    def betting(self, position_bet):
        """ funcao que controla a rodada de apostas 
        """
        import pdb;pdb.set_trace()
        action = []
        blind = self.bigblind
        round_check = False
        def player_action(player, actions_player, blind):
            """ processa a acao do player """
            action, value = actions_player
            if action == 'fold': player.active = False
            elif action == 'check': value_transaction = self.transaction(player, blind)
            elif action == 'raise': value_transaction = self.transaction(player, value)
            elif action == 'bet': value_transaction = self.transaction(player, bind)
            else: raise 'Precisa escolher uma jogada'
            return value_transaction

        def check():
            """ checa se o round acabou """
            round_check = True
            for player in itertools.ifilter(lambda x: x.active, self.players):
                if player.paid < blind and not player.allin:
                    round_check = False

        while round_check == False:
           
            if position_bet == 1 and len(self.players)>2: players = self.players[2:]
            elif position_bet == 1 and len(self.players)<=2: players = self.players
            else: players = self.players
            for player in itertools.ifilter(lambda x: x.active, players):
                player_action(player, player.do(blind, action), blind)
                
            #fez a primeira rodada de apostas e agora cobra do smallblind e do blind
            if self.players[0].active: player_action(player, player.do(blind, action), blind) #vez do smallblind
            elif self.players[1].active: player_action(player, player.do(blind, action), blind)
                
        #verifica se esta tudo pago, senao repete rodada de apostas
            round_check = check()


    def pay(self):
        """ define o vencedor e paga o dinheiro para ele """
        #limpa a variavel best_hand
        for player in self.players: player.best_hand=''
        #add as cartas no flop do jogador (7 cartas)
        map(lambda player: player.cards.extend(self.flop), 
            itertools.ifilter(lambda player: player.active, self.players))
        #acha a melhor mão de cada jogador)
        for player in  itertools.ifilter(lambda player: player.active, self.players):
            player.best_hand = poker([o for o in itertools.combinations(player.cards,5)])
        #acha o vencedor
        _players = filter(lambda player: player.active, self.players)
        cards = []
        map(lambda player: cards.extend(player.best_hand), self.players)
        win = poker(cards)
        #acha o vencedor e paga ele
        _winners = filter(lambda player: player.best_hand[0] in win, self.players)
        #confere
        for o in _winners:
            o.stack += self.pot/len(_winners)
        self.pot = 0
        #print self.players[0].cards
        #print cartas
        #map(lambda player: cards.append(poker([sorted([o for o in set(itertools.permutations(player.cards,5))], reverse=True)]), )
        #poker(cards)
        #import pdb;pdb.set_trace()
        #win = poker(cards)


    def croupier(self):
        """ executa uma rodada de jogo """
        #embaralha as cartas
        shuffle2a(self.deck)
        #cobra o ant
        map(collect_ant, itertools.ifilter(lambda player: player.active, self.players)) #collect ant
        collect_blind() #collect small and big blind
        map(receives_card, itertools.ifilter(lambda player: player.active, self.players)) #distribuite cards
        #betting(1) #primeira rodada de apostas
        self.flop = draw(self.deck, 3) #mostra flop
        #betting(2) # segunda rodada de apostas
        self.flop.extend(draw(self.deck, 1)) #turn
        #betting(3) #terceira rodada de apostas
        self.flop.extend(draw(self.deck, 1)) #river
        #betting(4) #quarta e ultima rodada de apostas
        pay() #paga os vencedores
        remove_players_break() # remove players que ficaram sem dinheiro


def test():
    """ testa as funcoes """
    jose = Player('jose', 1500)
    joao = Player('joao', 1500)
    juca = Player('juca', 1500)
    game = TexasHoldem([jose, joao, juca], 30, 60,3)
    shuffle2a(game.deck)
    assert len(game.draw(game.deck, 1)) == 1
    map(game.collect_ant, itertools.ifilter(lambda player: player.active, game.players)) #collect ant
    assert game.pot == 9
    map(game.receives_card, itertools.ifilter(lambda player: player.active, game.players)) #distribuite cards
    assert len(game.deck) == 45
    game.collect_blind() #collect blind
    assert game.pot == 99
    game.betting(1)
    game.flop.extend(game.draw(game.deck, 5))
    assert len(game.flop) == 5
    game.flop = ['AS','AC','TD','JS','TS']
    joao.cards = ['AH', 'JH']
    jose.cards = ['4H','4S']
    juca.cards = ['7H','8S']
    game.pay()
    import pdb;pdb.set_trace()
    assert joao.stack == 1536
    map(game.collect_ant, itertools.ifilter(lambda player: player.active, game.players)) #collect ant
    game.collect_blind() #collect blind
    juca.cards = ['7H','8S']
    joao.cards = ['AH', 'JH']
    jose.cards = ['AD','JH']
    game.pay()
    assert joao.stack == 1522
    assert jose.stack == 1483



        
test()