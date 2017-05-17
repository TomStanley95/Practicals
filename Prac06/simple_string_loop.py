__author__ = 'Tom Stanley'


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

DAYS_OF_THE_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class DaysOfTheWeek(App):
    status_text = StringProperty()

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def build(self):
        self.title = "Days of the Week"
        self.root = Builder.load_file('simple_string_loop.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        # for day in self.days_of_the_week:
        for day in DAYS_OF_THE_WEEK:
            temp_label = Label(text=day)
            self.root.ids.entriesBox.add_widget(temp_label)

DaysOfTheWeek().run()
