from kivy.app import App
from kivy.uix.screenmanager import Screen,SlideTransition

class LoginProzor(Screen):
    def forma(self):
        self.manager.transition=SlideTransition(direction='right')
        self.manager.current='login'
        self.manager.get_screen('login').resetForm()