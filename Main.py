import os
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition

from MainLogin import LoginProzor
class Login(Screen):
    def SpremiLozinku(self,logintext,passwordtext):
        app=App.get_running_app()

        app.username=logintext
        app.password=passwordtext

        self.manager.transition=SlideTransition(direction='left')
        self.manager.current='connected'

        app.config.read(app.get_application_config())
        app.config.write()

        def resetForm(self):
            self.ids['login'].text=""
            self.ids['password'].text=""

class LoginApp(App):
    username=StringProperty(None)
    password=StringProperty(None)

    def build(self):
        manager=ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(LoginProzor(name='connected'))
        return manager
    def get_application_config(self):
        if not self.username:
            return super(LoginApp,self).get_application_config()
            
        direktorij=f'{self.user_data_dir}/{self.username}'

        if not os.path.exists(direktorij):
            os.makedirs(direktorij)

        return super(LoginApp,self).get_application_config(f'{direktorij}/config.cfg')

if __name__=='__main__':
    LoginApp().run()
