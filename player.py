# -*- coding: utf-8 -*-
from random import randint
class Player(object):
	""" classe que controla o player """
	stack = 0 #valor do pot do jogador
	nome = "nome do jogador"
	active = False #se esta ativo ou nao no game
	cards = [] #cartas do jogador
	bet = False #se foi o player que apostou
	paid = 0 #quanto ele pagou
	allin = False #variavel de control se esta allin ou nao
	best_hand = '' #melhor mao do jogador na rodada
	def __init__(self, nome, buyin):
		""" """
		self.nome = nome
		self.stack = buyin
		self.active = True
	def do(self, bind, last_action):
		"""
		"""
		return 'check', 0
		#if last_action == 'bet":
		#	action = ['check', 'fold', 'raise', 'bet'][randint(0,3)]
		#else:
		#action = ['check', 'fold', 'raise', 'bet'][randint(0,3)]