#Importar o App, Builder (Conecta tela com codigo em py)
#Criar o aplicativo
#Criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests
from kivy.uix.togglebutton import ToggleButton

GUI = Builder.load_file('screen.kv')

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids['moeda1'].text = f'Bitcoin R$ {self.pegar_cotacao("BTC")}'
        self.root.ids['moeda2'].text = f'Dogecoin R$ {self.pegar_cotacao("DOGE")}'
        self.root.ids['moeda3'].text = f'Dolar R$ {self.pegar_cotacao("USD")}'
        self.root.ids['moeda4'].text = f'Euro R$ {self.pegar_cotacao("EUR")}'
        self.root.ids['moeda5'].text = f'Litecoin R$ {self.pegar_cotacao("LTC")}'

    def pegar_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao

MeuAplicativo().run()