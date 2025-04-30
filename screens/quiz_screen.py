from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

class QuizScreen(Screen):

    class QuizScreenCanvas(FloatLayout):
        def on_raindrop_select(self, instance):
            instance.md_bg_color = [0, 1, 0, 1]  # Glowing border effect

        def submit_answer(self):
            # Logic to go to next question and update interface
            pass