
class Maquina():
	rotores = []
	double_step = False

	#Inicializando os rotores
	def __init__(self, rotores):
		self.rotores = [Rotor(rotor[0], rotor[1], rotor[2]) for rotor in rotores]

	#Setando as posicoes iniciais dos 3 rotores	
	def set_rotores(self, posicoes):
		if len(posicoes) != len(self.rotores):
			print "erro, nao bate com o numero de rotores"
		else:
			[rotor.set_posicoes(posicoes[i]) for i, rotor in enumerate(self.rotores)]
		return

	#Encriptando um unico caracter utilizando os rotores definidos nesta classe
	def encrypt_char(self, c):
		for i, rotor in enumerate(self.rotores[::-1]):
			if i is 0:
				c = rotor.encripta_frente(c)
			else:
				diferenca = (alfabeto.index(self.rotores[::-1][i-1].posicao) - alfabeto.index(self.rotores[::-1][i].posicao)) % 26
				c = rotor.encripta_frente(alfabeto[alfabeto.index(c) - diferenca])
			print c
		diferenca = alfabeto.index(self.rotores[0].posicao)
		print c
		for i, rotor in enumerate(self.rotores):
			if i is 0:
				c = rotor.encripta_tras(c)
			else:
				diferenca = (alfabeto.index(self.rotores[i-1].posicao) - alfabeto.index(self.rotores[i].posicao)) % 26
				print diferenca
				c = rotor.encripta_tras(alfabeto[alfabeto.index(c) - diferenca])

			print c
		return c

	def status(self):
		return self.rotores[0].posicao + self.rotores[1].posicao + self.rotores[2].posicao

	#Definindo quando resetar os rotores no momento da virada
	def step(self):
		if self.double_step:
			self.rotores[1].step()
			self.rotores[0].step()
			self.double_step = False
		if self.rotores[2].step():
			self.rotores[1].step()
			if self.rotores[1].virada():
				self.double_step = True

	#Encriptando uma string inteira
	def encrypt(self, s):
		out = ''
		for c in s:
			self.step()
			out += self.encrypt_char(c)
		return out

		
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

	#seta de acordo com a posicao atual no rotor e faz as permutacoes necessarias
	def seta_posicao(self, posicao):
		troca_posicao = alfabeto.index(posicao) - alfabeto.index(self.posicao)
		self.posicao = posicao
		self.permutacoes = self.permutacoes[troca_posicao:] + self.permutacoes[:troca_posicao]

	#Faz a virada se chegar na posicao (1 volta)
	def virada(self):
		return True if self.virada == self.posicao else False


	#Faz um passo do rotor modulo 26
	def passo(self):
		virada = self.virada()
		self.permutacoes = self.permutacoes[1:] + self.permutacoes[:1]
		self.posicao = alfabeto[(alfabeto.index(self.posicao) + 1) % 26]
		if virada:
			return True
		else:
			return False

	def encripta_frente(self, c):
		return self.permutacoes[alfabeto.index(c)]

	def encripta_tras(self, c):
		return alfabeto[self.permutacoes.index(c)]
