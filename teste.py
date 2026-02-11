from flask import Flask
import requests

app = Flask(__name__)


@app.route('/subtraindo/<int:numero>', methods = ['GET'])
def subtraindo(numero):
    return {
        "nome": f'{numero}'
    }



@app.route('/nota_aluno/<float:nota>', methods = ['GET'])
def situacao(nota):
    if nota >= 10 and nota <=20:
       return 'Aprovado'
    elif nota > 5 and nota <= 9.5:
        return 'Exame'
    elif nota <= 5:
        return 'Reprovado'
    

@app.route('/intervalo/', methods = ['GET'])
def listando():
    lista = [1,2,3,4,5]
    #return f'{lista} o total de tudo é {sum(lista)} <br> o valor máximo é {max(lista)} e o minimo é {min(lista)} <br>',
    for number in lista:
        if number % 2 == 0:
            return f'{number} <br>'