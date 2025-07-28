import json
import os
from model.conta import ContaBancaria

# Caminhos para salvar os arquivos na pasta "data"
BASE_DIR = os.path.dirname(__file__)
CAMINHO_CONTAS = os.path.join(BASE_DIR, 'contas.json')

def salvar(contas): # Salva as contas em contas.json
    contas_dict = [conta.to_dict() for conta in contas]
    try:
        with open(CAMINHO_CONTAS, 'w') as arq:
            json.dump(contas_dict, arq, indent=4)
    except Exception as e:
        print(f"Ocorreu um erro ao salvar!\nError: {e}")

def carregar(): # Carrega as contas salvas em json
    contas = []
    try:
        with open(CAMINHO_CONTAS, 'r') as arq:
            contas.extend([ContaBancaria.from_dict(conta) for conta in json.load(arq)])
    except FileNotFoundError:
        return []
    return contas