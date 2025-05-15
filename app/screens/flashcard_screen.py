from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivymd.uix.button import MDFloatingActionButton

class FlashcardScreen(Screen):

    def add_flashcard(self):
        flashcard_text = self.input_box.text
        if flashcard_text:
            # Add the container to the flashcards layout
            self.flashcards_layout.add_widget(Flashcard(text=flashcard_text))

            # Clear the input box after adding the flashcard
            self.input_box.text = ""

    def open_color_picker(self):
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
                    # Access the flashcard button (first child in the BoxLayout)
                    flashcard_box = child.children[-1]  # Correctly access the flashcard button
                    if isinstance(flashcard_box, MDFlatButton):
                        flashcard_box.md_bg_color = value

        # Bind the color picker to the on_color callback
        color_picker.bind(color=on_color)

        # Open the popup
        self.color_picker_popup.open()

class Flashcard(BoxLayout):

    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
    
    def toggle_highlight(self):
        """
        Toggles the highlight of the flashcard.
        """
        # Toggle the highlight by adding or removing a translucent yellow overlay in front of the text
        if hasattr(self.flashcard_box, 'highlight_rect'):
            # Remove the highlight if it already exists
            self.flashcard_box.canvas.after.remove(self.flashcard_box.highlight_canvas)
            self.flashcard_box.canvas.after.remove(self.flashcard_box.highlight_rect)
            del self.flashcard_box.highlight_canvas
            del self.flashcard_box.highlight_rect
        else:
            # Add a translucent yellow overlay in front of the text
            with self.flashcard_box.canvas.after:
                self.flashcard_box.highlight_canvas = Color(1, 1, 0, 0.5)  # Yellow with 50% opacity
                self.flashcard_box.highlight_rect = Rectangle(
                    pos=(self.flashcard_box.x + 10, self.flashcard_box.y + (self.flashcard_box.height / 4)),
                    size=(self.flashcard_box.width - 20, self.flashcard_box.height / 2)
                )
        # Bind to update the rectangle's position and size when the widget changes
        self.flashcard_box.bind(pos=self.update_highlight, size=self.update_highlight)

    def update_highlight(self, instance, *args):
        # Update the position and size of the highlight rectangle
        if hasattr(instance, 'highlight_rect'):
            instance.highlight_rect.pos = (instance.x + 10, instance.y + (instance.height / 4))
            instance.highlight_rect.size = (instance.width - 20, instance.height / 2)
    
    def remove_flashcard(self):
        """
        Removes the flashcard from the widget tree
        """
        # Remove the flashcard from its parent layout
        self.parent.remove_widget(self)