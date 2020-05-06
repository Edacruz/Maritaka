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

def pegarpeixe(tipo):
	for casa in range(0, len(dados)):				
		if dados[casa]["id"] == ctx.author.id:
			dados[casa][tipo] += 1
			fish.sobrescrever("dados/inventario.json", dados)
