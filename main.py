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
