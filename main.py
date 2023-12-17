from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (310,580)

class MainScreen(Screen):
    def verify_credentials(self, password):
        if password == "user":  
            self.manager.current = 'menu'
        else:
            close_but = MDFlatButton(text='try again',on_release=self.close_dialog)  #button inside dialog box
            self.dialog = MDDialog(title='incorrect passward',
                                   pos_hint= {'center_x': 0.5,'center_y': 0.4},
                                   buttons=[close_but])
            self.dialog.open()
    def close_dialog(self, *args):
        self.dialog.dismiss()
class MenuScreen(Screen):
    pass
class AboutScreen(Screen):
    pass
class OwnerScreen(Screen):
    pass

class Savera(MDApp):
    def build(self):
        screen = ScreenManager()
        self.theme_cls.primary_palette=("Yellow")           #color of the text and icon
        self.theme_cls.primary_hue=("A700")                 #hue of the text
        self.theme_cls.theme_style=("Dark")
        screen.add_widget(Builder.load_file("main.kv"))
        screen.add_widget(Builder.load_file("menu.kv"))
        screen.add_widget(Builder.load_file("about.kv"))
        screen.add_widget(Builder.load_file("owner.kv"))
        return screen

if __name__ == '__main__':
    Savera().run()