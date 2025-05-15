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
from screens.help_screen import HelpScreen
from screens.settings_screen import SettingsScreen

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class IntercalmSpeechApp(MDApp):
    def build(self) -> ScreenManager:
        """
        Build the and set the theme and screen manager. Returns a
        Widget instance that is the root of the widget tree.
        """
        # Light Mode
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Light"
        Window.fullscreen = 'auto'

        # Show the welcome popup
        # self.show_welcome_popup()

        # Create the dropdown menu
        self.menu_items = [
            {
                "text": "Settings",
                "on_release": lambda: self.change_screen("settings"),
            },
            {
                "text": "Help",
                "on_release": lambda: self.change_screen("help"),
            },
        ]
        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )

        return super(IntercalmSpeechApp, self).build()

    # def show_welcome_popup(self):
    #     """Display a welcome popup when the app starts."""
    #     close_button = MDFlatButton(
    #         text="CLOSE",
    #         on_release=lambda x: self.dialog.dismiss()
    #     )
    #     self.dialog = MDDialog(
    #         title="Welcome!",
    #         text="Welcome to Intercalm Speech!",
    #         buttons=[close_button],
    #     )
    #     self.dialog.open()

    def open_menu(self, button: MDRaisedButton):
        """Open the dropdown menu."""
        self.menu.caller = button
        self.menu.open()

    def change_screen(self, screen_name: str):
        """Change to the selected screen."""
        self.menu.dismiss()
        # Add logic to navigate to the selected screen
        print(f"Navigating to {screen_name}")
        self.root.current = screen_name

if __name__ == '__main__':
    IntercalmSpeechApp().run()