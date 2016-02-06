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


class TexasHoldem(object):
    """
    uma rodada de poker

    """
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    
    players = [] #dealer is first position
    flop = ""
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

    ### devolve cartas do deck
    def draw(self, deck, n): 
        return [deck.pop(0) for i in xrange(0, n)]

    def collect_ant(self, player):
        """ coleta os valores do ant e coloca no pote """
        if player.stack > self.ant: 
            player.stack -= self.ant
            self.pot += self.ant
            player.allin = False
        elif player.stack > 0 and player.stack < self.ant:
            self.pot = player.stack
            player.stack = 0
            player.allin = True
            player_handpot = self.pot

    def collect_blind(self):
        """ coleta os valores do ant e coloca no pote """
        for pos, player in enumerate(self.players):
            if pos == 0: blind = self.smallblind
            elif pos == 1: blind = self.bigblind
            else: blind = 0
            #paga o small e o blind
            if player.stack > blind: 
                player.stack -= blind
                self.pot += blind
                player.paid = blind
                player.allin = False
            elif player.stack > 0 and player.stack < blind:
                self.pot += player.blind
                player.stack = 0
                player.paid = blind
                player.allin = True
                player_handpot = self.pot


    def receives_card(self, player):
        """ distribui as cartas para os jogadores
        """
        player.cards = self.draw(self.deck, 2)

    def betting():
        """ funcao que controla a rodada de apostas 
        """
        import pdb;pdb.set_trace()
        blind = self.blind
        while True:
            for player in itertools.ifilter(lambda x: x.active, self.players):
                player.do_action()

    def do_action(self, jogador):
        """ acao a ser adotada pelo jogador 
        call
        bet
        check
        fold
        """
        action, value = jogador.do()
        if action == 'call':
            pass
        if action == 'bet':
            pass
        if action == 'check':
            pass
        if action == 'fold':
            pass


    def winners(self):
        """ define o vencedor e paga o dinheiro para ele """
        pass

    def pay(self):
        """ paga os vencedores """
        pass

    def croupier(self):
        """ executa uma rodada de jogo """
        #embaralha as cartas
        map(collect_ant, itertools.ifilter(lambda player: player.active, self.player)) #collect ant
        collect_blind() #collect small and big blind
        map(receives_card, itertools.ifilter(lambda player: player.active, self.players)) #distribuite cards
        betting(1) #primeira rodada de apostas
        self.cards = draw(self.deck, 3) #mostra flop
        betting(2) # segunda rodada de apostas
        self.cards.extend(draw(self.deck, 1)) #turn
        betting(3) #terceira rodada de apostas
        self.cards.extend(draw(self.deck, 1)) #river
        betting(4) #quarta e ultima rodada de apostas
        winner = winners() #define quem sao os vencedores
        pay() #paga os vencedores
        remove_players_break() # remove players que ficaram sem dinheiro


def test():
    """ testa as funcoes """
    jose = Player('jose', 1500)
    joao = Player('joao', 1500)
    juca = Player('juca', 1500)
    game = TexasHoldem([jose, joao, juca], 30,60,3)
    assert len(game.draw(game.deck, 1)) == 1
    map(game.collect_ant, itertools.ifilter(lambda player: player.active, game.players)) #collect ant
    assert game.pot == 9
    map(game.receives_card, itertools.ifilter(lambda player: player.active, game.players)) #distribuite cards
    assert len(game.deck) == 45
    game.collect_blind()
    assert game.pot == 99
    game.betting(1)

        
test()