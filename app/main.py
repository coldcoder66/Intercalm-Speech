from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.lang import Builder

from screens.flashcard_screen import FlashcardScreen
from screens.home_screen import HomeScreen
from screens.lesson_screen import LessonScreen
from screens.lesson_screen_one import LessonScreenone
from screens.lesson_screen_overview import Lessonscreenoverview
from screens.login_screen import LoginScreen
from screens.qa_screen import QAScreen
from screens.quiz_screen import QuizScreen
from screens.writing_screen import WritingScreen

class IntercalmSpeechApp(MDApp):
    def build(self) -> ScreenManager:
        """
        Build the and set the theme and screen manager. Returns a
        Widget instance that is the root of the widget tree.
        """
        # Light Mode
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_hue = "A700"
        # self.theme_cls.theme_style = "Light"

        # Dark Mode
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"
        Window.fullscreen = 'auto'
        return super(IntercalmSpeechApp, self).build()

if __name__ == '__main__':
    IntercalmSpeechApp().run()