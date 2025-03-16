from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class Vaultica(Widget):
    title_text = StringProperty("Initial entry")

    def fetch_data(self):
        return "Mocked data"

    def update_label(self):
        self.title_text = self.fetch_data()

class VaulticaApp(App):

    def build(self):
        return Vaultica()

    


if __name__ == '__main__':
    VaulticaApp().run()
