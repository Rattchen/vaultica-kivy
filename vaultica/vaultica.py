from kivy.app import App
from kivy.uix.widget import Widget


class Vaultica(Widget):
    pass


class VaulticaApp(App):
    def build(self):
        return Vaultica()


if __name__ == '__main__':
    VaulticaApp().run()
