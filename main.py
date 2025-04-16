from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.scrollview import ScrollView

# Used for most MD apps
from kivymd.app import MDApp
# Used to reference the widgets in .kv and keep the positions
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
# Used for changing screens
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
# Used to set screen size
from kivy.core.window import Window

import os

# Class for each screen and its canvas
class HomeScreen(Screen):

    class HomeScreenCanvas(FloatLayout):
        pass

class QAScreen(Screen):

    def submit_question(self):
            question = self.ids.question_input.text
            if question:
                self.ids.qa_container.add_widget(MDLabel(text=question))
                self.ids.question_input.text = ''

    class QAScreenCanvas(FloatLayout):
        pass

class QuizScreen(Screen):

    class QuizScreenCanvas(FloatLayout):
        def on_raindrop_select(self, instance):
            instance.md_bg_color = [0, 1, 0, 1]  # Glowing border effect

        def submit_answer(self):
            # Logic to go to next question and update interface
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

class LoginScreen(Screen):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.username_input = TextInput(
            hint_text="Username",
            multiline=False,
            size_hint=(0.6, 0),  # Adjust width and height
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Center horizontally
        )

        self.password_input = TextInput(
            hint_text="Password",
            password=True,
            size_hint=(0.6, 0),  # Adjust width and height
            pos_hint={"center_x": 0.5, "center_y": 0.5}  # Center horizontally
        )

        login_button = MDRaisedButton(text="Login", on_press=self.validate_login)

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if username == "admin" and password == "1234":  # Example credentials
            print("Login successful!")  # You can navigate to another screen here
        else:
            print("Invalid credentials")
    class LoginScreenCanvas(FloatLayout):
        pass


class LessonScreenone(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set path for video file
        video_file_path = os.path.join(os.path.dirname(__file__), 'shrekrizz.mp4')

        layout = BoxLayout(orientation="vertical")
        video = VideoPlayer(source=video_file_path, state="play", options={"allow_stretch": True}, size_hint=(1, 1))
        layout.add_widget(video)
        self.add_widget(layout)

    class LessonScreenoneCanvas(FloatLayout):
        pass

class Lessonscreenoverview(Screen):
    pass
    class LessonscreenoverviewCanvas(FloatLayout):
        pass

    
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
    IntercalmSpeechApp().run()