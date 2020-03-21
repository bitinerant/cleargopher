# -*- coding: utf-8 -*-
#

import webbrowser
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
<About>:
    name: 'about'

    FloatLayout:

        Image:
            source: 'icon.png'
            opacity: .4

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(0), dp(10)

            Widget:
            Widget:

            Label:
                id: label
                font_size: '14sp'
                bold: True
                color: 0, 0, 0, 1
                markup: True
                halign: 'center'
                on_ref_press: root.open_url(*args)

            Widget:
            Widget:
''')

class About(Screen):
    def open_url(self, instance, url):
        webbrowser.open(url)
