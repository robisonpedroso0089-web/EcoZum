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
