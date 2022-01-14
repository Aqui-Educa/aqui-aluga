from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

locacaoFile = '../db/locacao.csv'

@app.route('/locacao/inserir', methods=['POST'])
def inserirLocacao():
    locacao = json.loads(request.data)
    inserirLocacoesCsv(locacao)
    return { 'message': 'Cadastro de locação com sucesso' }


@app.route('/locacao/listar', methods=['GET'])
def listarLocacao():
    locacoes = listarLocacaoCsv()
    return json.dumps(locacoes)

#para a exclusão, é necessário reconstruir toda a planilha
#pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
#ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/locacao/deletar/<nroLinha>', methods=['DELETE'])
def deletarLocacao(nroLinha):
    locacoes = listarLocacaoCsv()
    novasLocacoes = []       

    i = 0
    for locacao in locacoes:        
        if int(nroLinha) != i:
            novasLocacoes.append(locacao)
        i = i + 1

    reinserirLocacaoCsv(novasLocacoes)
    return { 'message': 'Locação deletada com sucesso' }


def listarLocacaoCsv():
    locacoes = []
    with open(locacaoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                locacoes.append({ 
                    'agencia': linha[0], 
                    'dataRetirada': linha[1], 
                    'horario': linha[2],
                    'categoria': linha[3], 
                    'cupom': linha[4], 
                    'comentario': linha[5],  
                })
                print(locacoes)
            count += 1

    return locacoes


def inserirLocacoesCsv(locacao):
    novaLinha = [locacao["agencia"], locacao["dataRetirada"], locacao["horario"], locacao["categoria"], locacao["cupom"], locacao["comentario"]]
    with open(locacaoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

        # var agencia = document.getElementById("agencia").value
        # var dataRetirada = document.getElementById("dataRetirada").value
        # var horario = document.getElementById("horario").value
        # var categoria = document.getElementById("categoria").value
        # var cupom = document.getElementById("cupom").value
        # var comentario = document.getElementById("comentario").value

def reinserirLocacaoCsv(locacoes):
    linhas = []
    linhas.append(["agencia", "dataRetirada", "horario", "categoria", "cupom", "comentario"]) #é necessário inserir novamente o cabeçalho da planilha

    for locacao in locacoes:
        novaLinha = [locacao["agencia"], locacao["dataRetirada"], locacao["horario"], locacao["categoria"], locacao["cupom"], locacao["comentario"]]
        linhas.append(novaLinha)

    with open(locacaoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()