import json


def sobrescrever(arquivo, content):
	with open(arquivo,'r') as f:
		dados = json.load(f)#isso não tem proposito algum mas tá funcionando assim mesmo, 
		#então não vou arriscar tirar kkkk
	with open(arquivo, 'w') as f:
		json.dump(content, f, indent=4)
	#return print("DADO ATUALIZADO!")


def adicionar(arquivo, content):
	with open(arquivo,'r') as f:
		dados = json.load(f)
	with open(arquivo, 'w') as f:
		dados.append(content)
		json.dump(dados, f, indent=4)
	return print("NOVO DADO ADICIONADO!!!")


def ler(arquivo):
	try:
		with open(arquivo) as f:
			dados = json.load(f)
	except:
		print("Error ao tentar carregar os dados.")
	else:
		return dados

def pegarpeixe(arquivo, tipo, usuario):
	with open(arquivo) as f:
		dados = json.load(f)
	for casa in range(0, len(dados)):
		if dados[casa]["id"] == usuario:
			dados[casa][tipo] += 1
			sobrescrever("dados/inventario.json", dados)


def existe(arquivo, user):
	'''
		checando se o usuario já existe.
		esse algoritimo é definido pra presupor que o usuario existe. Ele tenta falcear essa possibilidade,
		testanto toda hora se a variavel continua verdadeira, se em algum momento o estado da variavel
		mudar, então o resultado final será falso.	
	'''
	existe = True
	dados = ler(arquivo)
	for casa in range(0, len(dados)):
		if user == dados[casa]['id']:
			existe = True
			break
		else: 
			existe = False

	if existe == False:
		content = {"id": user,"peixe-c": 0,"peixe-u": 0,"peixe-r": 0,"peixe-l": 0}
		adicionar(arquivo, content)
		existe = True