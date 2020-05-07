import json


def sobrescrever(arquivo, content):
	with open(arquivo,'r') as f:
		dados = json.load(f)#carregando os dados do arquivo e salvando na variavel dados
	with open(arquivo, 'w') as f:
		json.dump(content, f, indent=4)
	return print("dados atualizados com sucesso!!!")


def adicionar(arquivo, content):
	with open(arquivo,'r') as f:
		dados = json.load(f)
	with open(arquivo, 'w') as f:
		dados.append(content)
		json.dump(dados, f, indent=4)
	return print("dados escritos com sucesso!!!")


def ler(arquivo):
	try:
		with open(arquivo) as f:
			dados = json.load(f)
	except:
		print("tô conseguindo carregar os dados não porra")
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
		else: 
			existe = False

	if existe == False:
		content = {"id": user,"peixe-c": 0,"peixe-u": 0,"peixe-r": 0,"peixe-l": 0}
		dados.append(content)
		adicionar(arquivo, content)
		existe = True
	else:
		dados = ler(arquivo)
	return dados