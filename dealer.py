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

class TexasHoldem(object):
	"""
	uma rodada de poker

	"""
	deck = ''
	
	players = [] #dealer is first position
	flop = ""
	pot = 0
	ant = 0
	smallblind = 0
	bigblind = 0

	def __init __():
		"""
		"""
		pass

	### devolve cartas do deck
	def draw(n):
        return [self.deck.pop(0) for i in xrange(0, n)]

	def collect_ant:(player):
		""" coleta os valores do ant e coloca no pote """
		if player.pot > ant: 
			player.pot =- ant
			self.pot += ant
			player.allin = False
		elif player.pot > 0 and player.pot < ant:
			self.pot = player.pot
			player.pot = 0
			player.allin = True

	def collect_blind:(players):
		""" coleta os valores do ant e coloca no pote """
	    for pos, player in enumerate(self.players):    	
	    	if pos == 0: blind = self.smallblind
	    	elif pos == 1: blind = self.bigblind
	    	else: blind = 0
	    	#paga o small e o blind
			if player.pot > blind: 
				player.pot =- blind
				self.pot += blind
				player.paid = blind
				player.allin = False
			elif player.pot > 0 and player.pot < blind:
				self.pot = player.blind
				player.pot = 0
				player.paid = blind
				player.allin = True


	def receives_card(player):
		""" distribui as cartas para os jogadores
		"""
		player.cards = draw(2)

	def betting():
		""" funcao que controla a rodada de apostas 

		"""
		blind = self.blind
		while True:
			for player in itertools.ifilter(lambda x: x.active, self.players):
				player.do_action()


	def do_action(jogador):
		""" acao a ser adotada pelo jogador 
		call
		bet
		check
		fold
		"""
		action, value = jogador.do()
		if action == 'call':
		if action == 'bet':
		if action == 'check':
		if action == 'fold':


	def winners():
		""" define o vencedor e paga o dinheiro para ele """
		pass

	def pay():
		""" paga os vencedores """
		pass

	def crupie():
		""" executa uma rodada de jogo """
		#collect ant
		map(collect_ant, itertools.ifilter(lambda player: player.active, self.players))]
		#collect small and big blind
		collect_blind()
		#distribuite cards
		map(receives_card, itertools.ifilter(lambda player: player.active, self.players))
		#primeira rodada de apostas
		betting(1)
		#mostra flop
		self.cards = draw(3)
		# segunda rodada de apostas
		betting(2)
		#turn
		self.cards.extend(draw(1))
		#terceira rodada de apostas
		betting(3)
		#river
		self.cards.extend(draw(1))
		#quarta e ultima rodada de apostas
		betting(4)
		#define quem sao os vencedores
		winner = winners()
		#paga os vencedores
		pay()
		remove_players_break()

		
