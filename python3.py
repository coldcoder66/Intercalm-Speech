from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRaisedButton, MDFlatButton
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
    def __init__(self, **kwargs):
        super(FlashcardScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()

        # Initial TextInput for user to enter text
        self.input_box = TextInput(hint_text="Enter your flashcard text here",
                                   size_hint=(0.8, 0.1),
                                   pos_hint={"center_x": 0.5, "center_y": 0.7},
                                   multiline=True)
        self.layout.add_widget(self.input_box)

        # Layout to display multiple flashcards
        self.flashcards_layout = BoxLayout(orientation='vertical',
                                           size_hint=(0.8, 0.6),
                                           pos_hint={"center_x": 0.5, "center_y": 0.6},
                                           spacing=10)
        self.layout.add_widget(self.flashcards_layout)

        # Button to add flashcard
        self.add_button = MDRaisedButton(text="Add Flashcard",
                                         size_hint=(0.4, 0.1),
                                         pos_hint={"center_x": 0.5, "center_y": 0.2})
        self.add_button.bind(on_press=self.add_flashcard)
        self.layout.add_widget(self.add_button)

        self.add_widget(self.layout)

    def add_flashcard(self, instance):
        flashcard_text = self.input_box.text
        if flashcard_text:
            flashcard_box = MDFlatButton(text=flashcard_text,
                                         size_hint=(1, None),
                                         height=40,
                                         md_bg_color=[0.737, 0.843, 0.953, 1],
                                         theme_text_color="Custom",
                                         text_color= [0.235, 0.337, 0.435, 1])
            self.flashcards_layout.add_widget(flashcard_box)
            self.input_box.text = ""
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
