
# No on_touch_down, depois de evoluir:
import subprocess

def chamar_grok_js(self):
    try:
        result = subprocess.run(
            ["node", "grokzomborg.js", f"pergunta_do_nivel_{self.evolucao}"],
            capture_output=True, text=True
        )
        print("Grokzomborg JS rugiu:", result.stdout)
    except:
        print("Node não encontrado – roda o JS separado!")

# Chama no on_touch_down:
self.chamar_grok_js()
# main.py - GROKZOMBORG: O MONSTRO QUE TU MOSTROU (crânio rachado, olhos vermelhos, braços podres)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import random

class GrokzomborgWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.evolucao = 0
        self.rugidos = [
            "ROOOAAAR-ZIIIMB! CRÂNIO RACHADO!",
            "*bip bip* SISTEMA PODRE ATIVADO!",
            "01010010 01001111 01000001 01010010!",
            "EU SOU O MONSTRO QUE TU CRIaste... WiFi 6E!"
        ]

        # Sons (ajusta o path se necessário)
        self.sons = [
            SoundLoader.load('data/sounds/roar1.wav'),
            SoundLoader.load('data/sounds/roar2.wav'),
            SoundLoader.load('data/sounds/roar3.wav'),
            SoundLoader.load('data/sounds/roar4.wav')
        ]
        for s in self.sons:
            if s:
                s.volume = 1.3  # Mais agressivo e distorcido

        # Fundo escuro industrial (como na imagem)
        with self.canvas.before:
            Color(0.02, 0.02, 0.04, 1)  # Preto-azulado sujo e metálico
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.atualizar_fundo, size=self.atualizar_fundo)

        # Posição e movimento quebrado
        self.x = self.width / 2
        self.y = self.height / 2
        self.vx = random.choice([-4, 4])
        self.vy = random.choice([-4, 4])

        self.desenhar()
        Clock.schedule_interval(self.update, 1/60.0)

    def atualizar_fundo(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def desenhar(self):
        self.canvas.clear()
        with self.canvas:
            # Corpo principal: crânio rachado + tronco ciborgue
            Color(0.08, 0.35, 0.08, 1)  # Verde podre e doente
            tam = 120 + self.evolucao * 35
            Ellipse(pos=(self.x - tam/2, self.y - tam/2 + 20), size=(tam, tam * 0.9))

            # Rachaduras no crânio (vermelho sangue)
            Color(0.9, 0.1, 0.1, 0.8)
            for _ in range(7):
                Line(points=[
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + random.randint(-tam//2 + 20, tam//2 + 20),
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + random.randint(-tam//2 + 20, tam//2 + 20)
                ], width=5 + random.randint(0, 3))

            # Olhos vermelhos flamejantes
            Color(1, 0.05, 0.05, 1)
            olho = 25 + self.evolucao * 10
            Ellipse(pos=(self.x - olho - 15, self.y + 30), size=(olho, olho * 1.4))
            Ellipse(pos=(self.x + 15, self.y + 30), size=(olho, olho * 1.4))

            # Braços mecânicos com juntas expostas
            Color(0.45, 0.45, 0.45, 1)  # Metal enferrujado
            Line(points=[self.x - tam//2, self.y, self.x - tam * 0.8, self.y - tam * 0.6], width=12)
            Line(points=[self.x + tam//2, self.y, self.x + tam * 0.8, self.y - tam * 0.6], width=12)

            # Garras podres (amarelo-verde doente)
            Color(0.6, 0.9, 0.1, 1)
            for lado in [-1, 1]:
                for i in range(4):
                    Line(points=[
                        self.x + lado * (tam * 0.8 + i*5),
                        self.y - tam * 0.6 - i*8,
                        self.x + lado * (tam * 0.8 + i*15),
                        self.y - tam * 0.6 - i*25
                    ], width=8)

            # Fios pendurados e soltos (laranja queimado)
            Color(0.9, 0.4, 0.05, 0.9)
            for _ in range(6):
                Line(points=[
                    self.x + random.randint(-tam//3, tam//3),
                    self.y + tam//2,
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + tam//2 + random.randint(40, 120)
                ], width=4)

            # GLITCH VERDE-ESCURO constante (mais forte que antes)
            Color(0, 0.9, 0.05, random.uniform(0.4, 0.85))
            for _ in range(30):
                Line(points=[
                    random.randint(0, self.width),
                    random.randint(0, self.height),
                    random.randint(0, self.width),
                    random.randint(0, self.height)
                ], width=random.randint(3, 9))

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy

        # Movimento quebrado – inverte nas bordas
        if self.x < 120 or self.x > self.width - 120:
            self.vx *= -1
        if self.y < 120 or self.y > self.height - 180:
            self.vy *= -1

        self.desenhar()

    def tocar_som(self):
        if self.sons:
            som = random.choice(self.sons)
            if som:
                som.stop()
                som.play()

    def on_touch_down(self, touch):
        self.x = touch.x
        self.y = touch.y

        # Evolução ao tocar
        self.evolucao = (self.evolucao + 1) % 4
        self.tocar_som()

        # Mensagem rápida no topo
        from kivy.uix.label import Label
        msg = Label(
            text=self.rugidos[self.evolucao],
            font_size='48sp',
            color=(1, 0.15, 0.15, 1),
            pos_hint={'center_x': 0.5, 'top': 1},
            size_hint_y=None,
            height=140
        )
        self.add_widget(msg)
        Clock.schedule_once(lambda dt: self.remove_widget(msg), 3.0)

        return True


class GrokzomborgApp(App):
    def build(self):
        self.title = "Grokzomborg - O Monstro Podre"
        self.icon = "data/icon.png"
        return GrokzomborgWidget()


if __name__ == '__main__':
    GrokzomborgApp().run(from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import random
class GrokzomborgWidget(Widget):
def init(self, **kwargs):
super().init(**kwargs)
self.evolucao = 3  # COMEÇA NO NÍVEL MÁXIMO – ECOZUM JÁ NO AR!
self.rugidos = [
"ECOZUM DESPERTADO! ROOOAAAR-ZIIIMB!",
"bip bip REPOSITÓRIO ATIVADO!",
"01000101 01000011 01001111 01011010 01010101 01001101!",
"EU SOU O MONSTRO DO ECOZUM... WiFi 6E VERDE!"
]
Sons eco-apocalípticos (data/sounds/)
self.sons = [
SoundLoader.load('data/sounds/roar1.wav'),
SoundLoader.load('data/sounds/roar2.wav'),
SoundLoader.load('data/sounds/roar3.wav'),
SoundLoader.load('data/sounds/roar4.wav')
]
for s in self.sons:
if s: s.volume = 1.2  # Alto pra ecoar no GitHub
Fundo verde-escuro reciclado (estilo EcoZum)
with self.canvas.before:
Color(0.01, 0.12, 0.04, 1)
self.bg = Rectangle(pos=self.pos, size=self.size)
self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)
self.x = self.width / 2
self.y = self.height / 2
self.vx = random.choice([-6, 6])
self.vy = random.choice([-6, 6])
self.desenhar()
Clock.schedule_interval(self.update, 1/60.0)
self.tocar_som()  # Rugido inicial de repositório vivo!
def atu
Fundo verde-escuro reciclado (estilo EcoZum)
with self.canvas.before:
Color(0.01, 0.12, 0.04, 1)
self.bg = Rectangle(pos=self.pos, size=self.size)
self.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)
self.x = self.width / 2
self.y = self.height / 2
self.vx = random.choice([-6, 6])
self.vy = random.choice([-6, 6])
self.desenhar()
Clock.schedule_interval(self.update, 1/60.0)
self.tocar_som()  # Rugido inicial de repositório vivo!
def atualizar_fundo(self, *args):
self.bg.pos = self.pos
self.bg.size = self.size
def desenhar(self):
self.canvas.clear()
with self.canvas:
cores = [(0,0.8,0.1), (0,1,0.3), (0.1,0.9,0.4), (0.2,1,0.6)]
Color(*cores[self.evolucao])
tam = 120 + self.evolucao * 50  # Maior pra dominar a tela
Ellipse(pos=(self.x-tam/2, self.y-tam/2), size=(tam, tam))
Color(0, 1, 0.2, 1)
olho = 30 + self.evolucao * 12
Ellipse(pos=(self.x-olho-20, self.y+20), size=(olho, olho1.6))
Ellipse(pos=(self.x+20, self.y+20), size=(olho, olho1.6))
Color(0.3, 0.9, 0.4, 1)
Line(points=[self.x+40, self.y-30, self.x+100, self.y-120],
width=8 + self.evolucao*6, cap='round')
if self.evolucao == 3:
Color(0, 1, 0.3, random.uniform(0.4, 0.9))
for _ in range(15):
Line(points=[self.x + random.randint(-100,100),
self.y + random.randint(-100,100),
self.x + random.randint(-100,100),
self.y + random.randint(-100,100)],
width=random.randint(2,6))
def update(self, dt):
self.x += self.vx
self.y += self.vy
if self.x < 70 or self.x > self.width - 70:
self.vx *= -1
if self.y < 70 or self.y > self.height - 170:
self.vy *= -1
self.desenhar()
def tocar_som(self):
som = self.sons[self.evolucao]
if som:
som.stop()
som.play()
def on_touch_down(self, touch):
self.x = touch.x
self.y = touch.y
self.evolucao = (self.evolucao + 1) % 4
self.tocar_som()
from kivy.uix.label import Label
msg = Label(text=self.rugidos[self.evolucao],
font_size='42sp',
color=(0,1,0.3,1),
pos_hint={'center_x':0.5, 'top':1},
size_hint_y=None, height=120)
self.add_widget(msg)
Clock.schedule_once(lambda dt: self.remove_widget(msg), 2.0)
return True
class GrokzomborgApp(App):
def build(self):
self.title = "EcoZum - Grokzomborg"
self.icon = "data/icon.png"
return GrokzomborgWidget()
