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

from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.lang import Builder

Builder.load_string('''
#:import NavDrawer libs.uix.baseclass.navdrawer.NavDrawer
#:import License libs.uix.baseclass.license.License
#:import BaseScreen libs.uix.baseclass.basescreen.BaseScreen
#:import GuideIntro libs.uix.baseclass.guide.GuideIntro
#:import GuideVpnProvider libs.uix.baseclass.guide.GuideVpnProvider
#:import GuideVpnCredentials libs.uix.baseclass.guide.GuideVpnCredentials
#:import GuideVpnLocation libs.uix.baseclass.guide.GuideVpnLocation
#:import GuideRouterName libs.uix.baseclass.guide.GuideRouterName
#:import GuideConnectWiFi libs.uix.baseclass.guide.GuideConnectWiFi
#:import GuideLogin libs.uix.baseclass.guide.GuideLogin
#:import GuideConfigure libs.uix.baseclass.guide.GuideConfigure
#:import About libs.uix.baseclass.about.About

<StartScreen>

    MDToolbar:
        id: action_bar
        background_color: app.theme_cls.primary_color
        title: app.title
        left_action_items: [ ['menu', lambda x: nav_drawer.toggle_nav_drawer()], ]
        right_action_items: [ ['linux', lambda x: print('linux')], ['help', lambda x: print('help')], ]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"top": 1}

    ScreenManager:
        id: manager
        size_hint_y: None
        height: root.height - action_bar.height

        BaseScreen:
            id: base_screen

        GuideIntro:
            id: guide_intro

        GuideVpnProvider:
            id: guide_vpn_provider

        GuideVpnCredentials:
            id: guide_vpn_credentials

        GuideVpnLocation:
            id: guide_vpn_location

        GuideRouterName:
            id: guide_router_name

        GuideConnectWiFi:
            id: guide_connect_wifi

        GuideLogin:
            id: guide_login

        GuideConfigure:
            id: guide_configure

        License:
            id: license

        About:
            id: about

    MDNavigationDrawer:
        id: nav_drawer

        NavDrawer:
''')

class StartScreen(NavigationLayout):
    pass
