from kivymd.app import MDApp
import sys
# Used for most MD apps
from kivymd.app import MDApp
# Used to reference the widgets in .kv and keep the positions
# Used for changing screens
from kivy.uix.screenmanager import ScreenManager, NoTransition
# Used to set screen size
from kivy.core.window import Window

# Used to find the path of data files
from kivy.resources import resource_add_path

# Used to load multiple kivy files
from kivy.lang import Builder

import os

from screens.flashcard_screen import FlashcardScreen
from screens.home_screen import HomeScreen
from screens.lesson_screen import LessonScreen
from screens.lesson_screen_one import LessonScreenone
from screens.lesson_screen_overview import Lessonscreenoverview
from screens.login_screen import LoginScreen
from screens.qa_screen import QAScreen
from screens.quiz_screen import QuizScreen
from screens.writing_screen import WritingScreen


#Load the kv files
import glob
kv_files = glob.glob('kv/*.kv')
for kv_file in kv_files:
    Builder.load_file(kv_file)

class IntercalmSpeechApp(MDApp):
    def build(self):
        # Light Mode
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_hue = "A700"
        # self.theme_cls.theme_style = "Light"

        # Dark Mode
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"

        Window.fullscreen='auto'

        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(QAScreen(name='qa'))
        self.sm.add_widget(QuizScreen(name='quizscreen'))
        self.sm.add_widget(LessonScreen(name='lessonscreen'))
        self.sm.add_widget(FlashcardScreen(name='flashcardscreen'))
        self.sm.add_widget(WritingScreen(name='writingscreen'))
        self.sm.add_widget(LessonScreenone(name='lessonscreenone'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(Lessonscreenoverview(name='lessonscreenoverview'))
        return self.sm

    def go_home(self):
        self.sm.current = 'home'

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    IntercalmSpeechApp().run()