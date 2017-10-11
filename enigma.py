alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'

class Rotor():
	permutacoes = []
	virada = ''
	posicao = 'A'
	def __init__(self, permutacoes, virada, setup):
		i = alfabeto.index(setup)
		permutacoes = permutacoes[i:] + permutacoes[:i]
		self.permutacoes = [c for c in permutacoes]
		self.virada = virada