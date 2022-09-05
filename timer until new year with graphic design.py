from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Line, Color
from kivy.uix.boxlayout import BoxLayout

from datetime import datetime


class Background(BoxLayout):
    def __init__(self):
        super(Background, self).__init__()
        self.width = Window.size[0]
        self.height = Window.size[1]
        self.add_gradient()

    def add_gradient(self, ms = 0, s = 0):
        self.canvas.before.clear()
        
        linem = int((ms + s * 1000) / 59999 * self.height)
        linem2 = int((59999 - ms - s * 1000) / 59999 * self.height)
        line = int(ms / 999 * self.width)
        line2 = int((999 - ms) / 999 * self.width)

        brightness = int(self.width / 32)

        for sep in range(linem - brightness, linem + brightness + 1):
            self.canvas.before.add(Color(rgba=(1, 1, 1, (1 - abs(linem - sep) / brightness) / 1.5)))
            self.canvas.before.add(Line(points=[0, sep, self.width, sep], width=1))

        for sep in range(linem2 - brightness, linem2 + brightness + 1):
            self.canvas.before.add(Color(rgba=(1, 1, 1, (1 - abs(linem2 - sep) / brightness) / 1.5)))
            self.canvas.before.add(Line(points=[0, sep, self.width, sep], width=1))

        for sep in range(line - brightness, line + brightness + 1):
            self.canvas.before.add(Color(rgba=(1, 1, 0, (1 - abs(line - sep) / brightness) / 1.5)))
            self.canvas.before.add(Line(points=[sep, 0, sep, self.height], width=1))

        for sep in range(line2 - brightness, line2 + brightness + 1):
            self.canvas.before.add(Color(rgba=(1, 1, 0, (1 - abs(line2 - sep) / brightness) / 1.5)))
            self.canvas.before.add(Line(points=[sep, 0, sep, self.height], width=1))


class TimerApp(App):
    def build(self):
        self.bg = Background()

        self.label = Label(markup = True, font_size = 50)
        self.date = datetime(2023, 1, 1)
        Clock.schedule_interval(self.main_loop, .01)

        self.bg.add_widget(self.label)

        return self.bg
    
    def main_loop(self, *args):
        d = self.date - datetime.now()

        self.bg.add_gradient(d.microseconds // 1000, d.seconds % 60)

        self.label.text = f"{d.days} д. | {d.seconds // 3600 if len(str(d.seconds // 3600)) > 1 else '0' + str(d.seconds // 3600)}:{d.seconds % 3600 // 60 if len(str(d.seconds % 3600 // 60)) == 2 else '0' + str(d.seconds % 3600 // 60)}:{d.seconds % 60 if len(str(d.seconds % 60)) == 2 else '0' + str(d.seconds % 60)}.[color=ff3333]{d.microseconds // 1000 if len(str(d.microseconds // 1000)) == 3 else '0' + str(d.microseconds // 1000) if len(str(d.microseconds // 1000)) == 2 else '00' + str(d.microseconds // 1000)}[/color]"

if __name__ == "__main__":
    TimerApp().run()