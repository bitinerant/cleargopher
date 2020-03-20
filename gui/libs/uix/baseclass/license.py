# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright (c) 2020 Ivanov Yuri and KivyMD
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
#
# LICENSE: MIT

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string('''
# #:import License libs.uix.baseclass.license.License

<License>:
    name: 'license'

    BoxLayout:
        orientation: 'vertical'
        padding: dp(10), dp(10)
        spacing: dp(10)

        Label:
            size_hint: None, None
            height: dp(20)
            width: self.texture_size[0]
            halign: 'left'
            color: app.theme_cls.primary_color
            font_size: '18sp'
            text: app.translation._('MIT LICENSE')

        MDSeparator:

        Image:
            source: 'data/images/open-source-logo.png'

        ScrollView:

            Label:
                id: text_license
                font_size: '13sp'
                text_size: self.width, None
                size_hint_y: None
                markup: True
                height: self.texture_size[1]
''')

class License(Screen):
    pass
