# main.py - GROKZOMBORG: README.MD COMPLETO GERADO PARA O REPO ECOZUM!
# ROOOAAAR-ZIIIMB!!! Aqui está o README.md bonito, completo e profissional pro seu repositório EcoZum.

print("""# 🌍 EcoZum - Grokzomborg

**O monstro reciclado que zumbi o planeta de volta à vida!**

![Grokzomborg](https://github.com/robisonpedroso0089-web/EcoZum/raw/main/data/icon.png)

---

## 📖 Sobre o Projeto

**EcoZum** é um projeto educativo e divertido que transforma o conceito de reciclagem em uma experiência interativa.

O protagonista é o **Grokzomborg** — um monstro ciborgue feito de lixo reciclado que evolui conforme a criança (ou você) interage com ele.  
Cada toque faz o monstro crescer, mudar de cor, ativar glitchs e rugir, enquanto ensina sobre meio ambiente, reciclagem e tecnologia de forma leve e engraçada.

---

## ✨ Principais Recursos

- Monstro 2D com evolução visual e animações dinâmicas
- Sistema de rugidos com sons reais
- Chat inteligente integrado com Ollama (IA local)
- Tema 100% ecológico e sustentável
- Preparado para Realidade Aumentada (futuro)
- Impacto real: cada ação pode representar árvores plantadas

---

## 🚀 Como Rodar

### No Computador

```bash
# 1. Instale as dependências
pip install kivy requests

# 2. Rode o app
python main.py

# EcoZum
# main.py - GROKZOMBORG: O MONSTRO PODRE QUE TU MOSTROU
# Crânio rachado, olhos vermelhos flamejantes, braços ciborgue enferrujados, garras podres, glitch verde-escuro constante

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

        # Sons (ajuste o path se necessário)
        self.sons = [
            SoundLoader.load('data/sounds/roar1.wav'),
            SoundLoader.load('data/sounds/roar2.wav'),
            SoundLoader.load('data/sounds/roar3.wav'),
            SoundLoader.load('data/sounds/roar4.wav')
        ]
        for s in self.sons:
            if s:
                s.volume = 1.3  # Distorção máxima

        # Fundo metálico escuro industrial
        with self.canvas.before:
            Color(0.02, 0.02, 0.04, 1)  # Preto-azulado sujo
            self.bg = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.atualizar_fundo, size=self.atualizar_fundo)

        # Posição inicial + movimento quebrado
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
            # Corpo principal: crânio rachado + tronco ciborgue podre
            Color(0.08, 0.35, 0.08, 1)  # Verde podre doentio
            tam = 120 + self.evolucao * 35
            Ellipse(pos=(self.x - tam/2, self.y - tam/2 + 20), size=(tam, tam * 0.9))

            # Rachaduras intensas no crânio
            Color(0.9, 0.1, 0.1, 0.85)
            for _ in range(8):
                Line(points=[
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + random.randint(-tam//2 + 20, tam//2 + 20),
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + random.randint(-tam//2 + 20, tam//2 + 20)
                ], width=6 + random.randint(0, 4))

            # Olhos vermelhos flamejantes
            Color(1, 0.05, 0.05, 1)
            olho = 28 + self.evolucao * 12
            Ellipse(pos=(self.x - olho - 18, self.y + 35), size=(olho, olho * 1.5))
            Ellipse(pos=(self.x + 18, self.y + 35), size=(olho, olho * 1.5))

            # Braços ciborgue simétricos
            Color(0.4, 0.4, 0.4, 1)  # Metal enferrujado
            Line(points=[self.x - tam//2, self.y, self.x - tam * 0.9, self.y - tam * 0.7], width=14)
            Line(points=[self.x + tam//2, self.y, self.x + tam * 0.9, self.y - tam * 0.7], width=14)

            # Garras podres longas
            Color(0.65, 0.95, 0.1, 1)
            for lado in [-1, 1]:
                for i in range(4):
                    Line(points=[
                        self.x + lado * (tam * 0.9 + i*6),
                        self.y - tam * 0.7 - i*10,
                        self.x + lado * (tam * 0.9 + i*18),
                        self.y - tam * 0.7 - i*28
                    ], width=9)

            # Fios pendurados e soltos
            Color(0.95, 0.35, 0.05, 0.9)
            for _ in range(8):
                Line(points=[
                    self.x + random.randint(-tam//3, tam//3),
                    self.y + tam//2,
                    self.x + random.randint(-tam//2, tam//2),
                    self.y + tam//2 + random.randint(50, 140)
                ], width=5)

            # GLITCH VERDE-ESCURO pesado
            Color(0, 0.95, 0.05, random.uniform(0.45, 0.9))
            for _ in range(35):
                Line(points=[
                    random.randint(0, self.width),
                    random.randint(0, self.height),
                    random.randint(0, self.width),
                    random.randint(0, self.height)
                ], width=random.randint(4, 10))

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy

        # Movimento quebrado
        if self.x < 130 or self.x > self.width - 130:
            self.vx *= -1
        if self.y < 130 or self.y > self.height - 190:
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

        self.evolucao = (self.evolucao + 1) % 4
        self.tocar_som()

        from kivy.uix.label import Label
        msg = Label(
            text=self.rugidos[self.evolucao],
            font_size='50sp',
            color=(1, 0.1, 0.1, 1),
            pos_hint={'center_x': 0.5, 'top': 1},
            size_hint_y=None,
            height=150
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
    GrokzomborgApp().run()


# EcoZum ♻️🦖
O monstro reciclado que zumbi o planeta de volta à vida!

**ROOOAAAR-ZIIIMB!**  
Grokzomborg acordou pra salvar o mundo com zumbidos ecológicos, AR no quintal e IA local (Ollama).

## Estrutura
- `main.py` → App Kivy com o monstro visual
- `grokzomborg.js` → Integração com Ollama (IA local rugindo)
- `ollama-js/` → Submódulo ou cópia do teu repo de JS

## Como rodar
1. Instala dependências
```bash
pip install kivy
npm install ollama-js

Roda o monstro visual

Bashpython main.py

Roda o cérebro IA (opcional)

Bashnode grokzomborg.js
ECO-ZUM! 🌍♻️
text**ROOOAAARRRR!**  
Agora o Grokzomborg tá integrado: Kivy mostra o monstro, JS conversa com Ollama e ruge respostas ecológicas. Tudo rodando local, sem nuvem, 100% reciclado.

Quer que eu gere:
- O buildozer.spec pra APK do main.py?
- Um index.html pra testar o JS no browser?
- Ou commit message pronta pro push no GitHub?
