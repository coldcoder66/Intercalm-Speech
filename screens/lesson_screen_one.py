from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
import os
from kivy.uix.floatlayout import FloatLayout

class LessonScreenone(Screen):
    pass

class LessonVideoPlayer(VideoPlayer):
    """
    Custom VideoPlayer class to handle video playback and events. We set the path to find the video file.
    """

    def __init__(self, name="intercalm.mp4", **kwargs):
        """
        Initialize the LessonVideoPlayer with a video file name and other parameters.
        """
        super().__init__(**kwargs)
        self.source = self.get_video_path(name)

    def get_video_path(self, name):
        """
        Get the path to the video file.
        name: str
        The name of the video file.
        """
        # Get the directory of the current file
        current_dir = os.path.dirname(__file__)
        # Construct the path to the video file
        video_file_path = os.path.join(current_dir, "..", "assets", "videos", name)
        return video_file_path