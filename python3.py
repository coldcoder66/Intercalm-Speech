from kivy.uix.behaviors import TouchRippleBehavior
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.app import MDApp

# Used for most MD apps
from kivymd.app import MDApp
# Used to reference the widgets in .kv and keep the positions
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
# Used for changing screens
from kivy.uix.screenmanager import ScreenManager, Screen
# Used to set screen size
from kivy.core.window import Window

# Example Android screen size
Window.size = (2224, 1668)

# Class for each screen and its canvas
class HomeScreen(Screen):
    pass
    class HomeScreenCanvas(FloatLayout):
        pass

class QAScreen(Screen):
    pass
    def submit_question(self):
            question = self.ids.question_input.text
            if question:
                self.ids.qa_container.add_widget(MDLabel(text=question))
                self.ids.question_input.text = ''
    class QAScreenCanvas(FloatLayout):
        pass

class QuizScreen(Screen):
    pass
    class QuizScreenCanvas(FloatLayout):
        pass

class LessonScreen(Screen):
    pass
    class LessonScreenCanvas(FloatLayout):
        pass

class FlashcardScreen(Screen):
    pass
    class FlashcardScreenCanvas(FloatLayout):
        pass

class WritingScreen(Screen):
    pass
    class WritingScreenCanvas(FloatLayout):
        pass
    
class AboutMeApp(MDApp):
    def build(self):
        # Light Mode
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_hue = "A700"
        # self.theme_cls.theme_style = "Light"

        # Dark Mode
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"

        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(QAScreen(name='qa'))
        self.sm.add_widget(QuizScreen(name='quizscreen'))
        self.sm.add_widget(LessonScreen(name='lessonscreen'))
        self.sm.add_widget(FlashcardScreen(name='flashcardscreen'))
        self.sm.add_widget(WritingScreen(name='writingscreen'))
        return self.sm

    def go_home(self):
        self.sm.current = 'home'

if __name__ == '__main__':
    AboutMeApp().run()
