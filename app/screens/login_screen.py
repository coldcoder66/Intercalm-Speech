from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # # FloatLayout to center the BoxLayout
        # root_layout = FloatLayout()

        # # BoxLayout for input fields
        # layout = BoxLayout(
        #     orientation='vertical',
        #     spacing=30,
        #     size_hint=(0.6, 0.4),  # Adjust width and height
        #     pos_hint={"center_x": 0.5, "center_y": 0.5}  # Center the BoxLayout
        # )

        # self.username_input = TextInput(
        #     hint_text="Username",
        #     multiline=False,
        #     size_hint=(1, .3),  # Full width of BoxLayout
        #     height=40  # Fixed height
        # )

        # self.password_input = TextInput(
        #     hint_text="Password",
        #     password=True,
        #     size_hint=(1, 0.3),  # Full width of BoxLayout
        #     height=40  # Fixed height
        # )

        # # Add input fields to the BoxLayout
        # layout.add_widget(self.username_input)
        # layout.add_widget(self.password_input)

        # # Add the BoxLayout to the FloatLayout
        # root_layout.add_widget(layout)

        # Login button positioned at the bottom-left corner
        # login_button = MDRaisedButton(
        #     text="Login",
        #     size_hint=(None, None),
        #     size=(120, 50),  # Fixed size
        #     pos_hint={"x": 0.02, "y": 0.02},  # Bottom-left corner
        #     on_press=self.validate_login
        # )

        # # Add the login button to the FloatLayout
        # root_layout.add_widget(login_button)

        # # Add the FloatLayout to the screen
        # self.add_widget(root_layout)

    def validate_login(self):
        username = self.username_input.text
        password = self.password_input.text
        if username == "admin" and password == "1234":  # Example credentials
            print("Login successful!")  # You can navigate to another screen here
        else:
            print("Invalid credentials")

    class LoginScreenCanvas(FloatLayout):
        pass