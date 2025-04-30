from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
import os
from kivy.uix.floatlayout import FloatLayout

class LessonScreenone(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set path for video file
        video_file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "videos", 'shrekrizz.mp4')

        layout = BoxLayout(orientation="vertical")
        video = VideoPlayer(source=video_file_path, state="play", options={"allow_stretch": True}, size_hint=(1, 1))
        layout.add_widget(video)
        self.add_widget(layout)

    class LessonScreenoneCanvas(FloatLayout):
        pass