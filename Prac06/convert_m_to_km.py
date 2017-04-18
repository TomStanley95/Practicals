__author__ = 'Tom Stanley'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertMiles(App):
    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_m_to_km.kv')
        Window.size = (500, 300)
        return self.root

    def handle_increment(self, increment):
        new_value = self.get_valid_miles() + increment
        self.root.ids.input_number.text = str(new_value)
        self.convert_miles()

    def convert_miles(self):
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = "{} miles is {}".format(self.root.ids.input_number.text, km)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertMiles().run()
