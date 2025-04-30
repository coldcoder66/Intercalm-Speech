from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel

class QAScreen(Screen):

    def submit_question(self):
        question = self.ids.question_input.text
        if question:
            self.ids.qa_container.add_widget(MDLabel(text=question))
            self.ids.question_input.text = ''

    class QAScreenCanvas(FloatLayout):
        pass