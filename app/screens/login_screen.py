from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout

class LoginScreen(Screen):

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