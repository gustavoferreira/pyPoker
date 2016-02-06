class Player(object):
	""" classe que controla o player """
	stack = 0 #valor do pot do jogador
	name = "nome do jogador"
	active = False #se esta ativo ou nao no game
	cards = [] #cartas do jogador
	def __init__(self, nome, buyin):
		""" """
		self.nome = nome
		self.stack = buyin
		self.active = True