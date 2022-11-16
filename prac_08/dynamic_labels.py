from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["john", "michelle", "tommy", "charlie"]

    def build(self):
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.entries_box.add_widget(temp_button)

    def display_name(self, instance):
        name = instance.text
        self.status_text = "{}".format(name)


DynamicLabelsApp().run()
