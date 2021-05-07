'''
Camera Example
'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        from os import getcwd
        self.cwd = getcwd() + "/"
        path = self.cwd
        #    return
        from android.permissions import Permission, request_permissions
        request_permissions(Permission.CAMERA)
        global name_trans
        global name_fx
        import os
        camera=self.ids['camera']
        print (camera.resolution)
        camera.resolution=[640,480]

class TestCamera(App):
    def build(self):
        return CameraClick()

TestCamera().run()
