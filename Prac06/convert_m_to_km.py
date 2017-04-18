__author__ = 'Tom Stanley'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMiles(App):
    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_m_to_km.kv')
        Window.size = (300, 300)
        return self.root

    def handle_increment(self, increment):
        new_value = float(self.root.ids.input_number.text) + int(increment)
        self.root.ids.input_number.text = str(new_value)

    def convert_miles(self):
        miles = float(self.root.ids.input_number.text)
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(km)



ConvertMiles().run()
