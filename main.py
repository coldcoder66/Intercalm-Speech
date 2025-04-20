from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.scrollview import ScrollView
import sys
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
# Used for most MD apps
from kivymd.app import MDApp
# Used to reference the widgets in .kv and keep the positions
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
# Used for changing screens
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
# Used to set screen size
from kivy.core.window import Window

# Used to find the path of data files
from kivy.resources import resource_add_path, resource_find

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
        self.flashcards_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.8, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            spacing=60  # Add spacing between flashcards
        )
        self.layout.add_widget(self.flashcards_layout)

        # Button to add flashcard
        self.add_button = MDRaisedButton(text="Add Flashcard",
                                         size_hint=(0.4, 0.1),
                                         pos_hint={"center_x": 0.5, "center_y": 0.2})
        self.add_button.bind(on_press=self.add_flashcard)
        self.layout.add_widget(self.add_button)
        # Button to customize flashcard color
        self.color_button = MDRaisedButton(text="Customize Color",
                                           size_hint=(0.4, 0.1),
                                           pos_hint={"center_x": 0.5, "center_y": 0.1})
        self.color_button.bind(on_press=self.open_color_picker)
        self.layout.add_widget(self.color_button)

        self.add_widget(self.layout)

    def add_flashcard(self, instance):
        flashcard_text = self.input_box.text
        if flashcard_text:
            # Create a container for the flashcard and the highlight button
            flashcard_container = BoxLayout(
                orientation='horizontal',
                size_hint=(1, None),
                height=50,
                spacing=10  # Add spacing between the flashcard and the button
            )

            # Create the flashcard button
            flashcard_box = MDFlatButton(
                text=flashcard_text,
                size_hint=(0.8, None),  # Take 80% of the widthq
                height=40,
                md_bg_color=[0.737, 0.843, 0.953, 1],  # Default background color
                theme_text_color="Custom",
                text_color=[0.235, 0.337, 0.435, 1]
            )

            # Create the "Highlight" button
            highlight_button = MDRaisedButton(
                text="Highlight",
                size_hint=(0.2, None),  # Take 20% of the width
                height=40
            )
            highlight_button.bind(on_press=lambda x: self.highlight_flashcard(flashcard_box))

            # Add the flashcard and the highlight button to the container
            flashcard_container.add_widget(flashcard_box)
            flashcard_container.add_widget(highlight_button)

            # Add the container to the flashcards layout
            self.flashcards_layout.add_widget(flashcard_container)

            # Clear the input box after adding the flashcard
            self.input_box.text = ""

    def highlight_flashcard(self, flashcard_box):
        # Toggle the highlight by adding or removing a translucent yellow overlay in front of the text
        if hasattr(flashcard_box, 'highlight_rect'):
            # Remove the highlight if it already exists
            flashcard_box.canvas.after.remove(flashcard_box.highlight_canvas)
            flashcard_box.canvas.after.remove(flashcard_box.highlight_rect)
            del flashcard_box.highlight_canvas
            del flashcard_box.highlight_rect
        else:
            # Add a translucent yellow overlay in front of the text
            with flashcard_box.canvas.after:
                flashcard_box.highlight_canvas = Color(1, 1, 0, 0.5)  # Yellow with 50% opacity
                flashcard_box.highlight_rect = Rectangle(
                    pos=(flashcard_box.x + 10, flashcard_box.y + (flashcard_box.height / 4)),
                    size=(flashcard_box.width - 20, flashcard_box.height / 2)
                )

            # Bind to update the rectangle's position and size when the widget chqanges
            flashcard_box.bind(pos=self.update_highlight, size=self.update_highlight)

    def update_highlight(self, instance, value):
        # Update the position and size of the highlight rectangle
        if hasattr(instance, 'highlight_rect'):
            instance.highlight_rect.pos = (instance.x + 10, instance.y + (instance.height / 4))
            instance.highlight_rect.size = (instance.width - 20, instance.height / 2)

    def open_color_picker(self, instance):
        # Create a layout for the popup content
        popup_content = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the ColorPicker
        color_picker = ColorPicker()
        popup_content.add_widget(color_picker)

        # Add a "Close" button to the popup
        close_button = MDRaisedButton(
            text="Close",
            size_hint=(1, None),
            height=40
        )
        close_button.bind(on_press=lambda x: self.color_picker_popup.dismiss())
        popup_content.add_widget(close_button)

        # Create the popup
        self.color_picker_popup = Popup(
            title="Pick a Color",
            content=popup_content,  # Set the popup content to the layout
            size_hint=(0.8, 0.8),
            auto_dismiss=False  # Prevent the popup from being dismissed automatically
        )

        def on_color(instance, value):
            # Apply the selected color to all flashcards
            for child in self.flashcards_layout.children:
                if isinstance(child, BoxLayout):
                    flashcard_box = child.children[1]  # Access the flashcard button
                    flashcard_box.md_bg_color = value

        # Bind the color picker to the on_color callback
        color_picker.bind(color=on_color)

        # Open the popup
        self.color_picker_popup.open()
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
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    IntercalmSpeechApp().run()