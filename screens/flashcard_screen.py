from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

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
            # Create a container for the flashcard, highlight button, and delete button
            flashcard_container = BoxLayout(
                orientation='horizontal',
                size_hint=(1, None),
                height=50,
                spacing=10  # Add spacing between the flashcard and the buttons
            )

            # Create the flashcard button
            flashcard_box = MDFlatButton(
                text=flashcard_text,
                size_hint=(0.6, None),  # Take 60% of the width
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

            # Create the "Delete" button
            delete_button = MDRaisedButton(
                text="Delete",
                size_hint=(0.2, None),  # Take 20% of the width
                height=40
            )
            delete_button.bind(on_press=lambda x: self.remove_flashcard(flashcard_container))

            # Add the flashcard, highlight button, and delete button to the container
            flashcard_container.add_widget(flashcard_box)
            flashcard_container.add_widget(highlight_button)
            flashcard_container.add_widget(delete_button)

            # Add the container to the flashcards layout
            self.flashcards_layout.add_widget(flashcard_container)

            # Clear the input box after adding the flashcard
            self.input_box.text = ""

    def remove_flashcard(self, flashcard_container):
        """
        Removes the specified flashcard container from the flashcards layout.
        """
        self.flashcards_layout.remove_widget(flashcard_container)

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

            # Bind to update the rectangle's position and size when the widget changes
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
            text="Apply Color",
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