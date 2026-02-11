
import requests

link = "http://127.0.0.1:5000/intervalo/"
lista = [5,5]
eviando = {'primeira' : lista}
resposta = requests.get(link, params= eviando)
    



