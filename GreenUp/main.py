import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, StringProperty

from parse_rest.datatypes import Object
from parse_rest.connection import register
from parse_rest.user import User
from parse_rest.core import ParseError

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    error = ObjectProperty(None, rebind=True)
    
    def login_button(self):
        try:
            u = User.login(self.username.text, self.password.text)
            app = kivy.app.App.get_running_app()
            app.user = u
            if not self.manager.has_screen('home'):
                self.manager.add_widget(HomeScreen(name='home'))
            self.manager.current = 'home'
        except ParseError:
            self.error.text = "Login Failed. Try again."
            self.error.color = [1,0,0,1]

    def signup_button(self):
        try:
            u = User.signup(self.username.text, self.password.text)
            u.displayName = u.username
            u.save()
            self.error.text = "User created successfully. Please Login."
            self.error.color = [0,1,0,1]
        except ParseError:
            self.error.text = "Signup Failed. Choose another username."
            self.error.color = [1,0,0,1]

class HomeScreen(Screen):
    userDisplayName = ''
    
    def __init__(self, **kwargs):
        app = kivy.app.App.get_running_app()
        u = app.user
        if not u.is_authenticated():
            self.manager.current = 'home'
        else:
            self.userDisplayName = u.displayName
            # make sure we aren't overriding any important functionality
            super(HomeScreen, self).__init__(**kwargs)
            
    def button_pressed(self, buttonText):
        if buttonText == 'Settings':
            if not self.manager.has_screen('settings'):
                self.manager.add_widget(SettingsScreen(name='settings'))
            self.manager.current = 'settings'
        elif buttonText == 'Profile':
            if not self.manager.has_screen('profile'):
                self.manager.add_widget(ProfileScreen(name='profile'))
            self.manager.current = 'profile'
        elif buttonText == 'Achievements':
            if not self.manager.has_screen('achievements'):
                self.manager.add_widget(AchievementsScreen(name='achievements'))
            self.manager.current = 'achievements'
        elif buttonText == 'Water':
            if not self.manager.has_screen('water'):
                self.manager.add_widget(WaterScreen(name='water'))
            self.manager.current = 'water'
        elif buttonText == 'Recycling':
            if not self.manager.has_screen('recycling'):
                self.manager.add_widget(RecyclingScreen(name='recycling'))
            self.manager.current = 'recycling'
        elif buttonText == 'Electricity':
            if not self.manager.has_screen('electricity'):
                self.manager.add_widget(ElectricityScreen(name='electricity'))
            self.manager.current = 'electricity'
        elif buttonText == 'Fuel':
            if not self.manager.has_screen('fuel'):
                self.manager.add_widget(FuelScreen(name='fuel'))
            self.manager.current = 'fuel'
            
class SettingsScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class ProfileScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class AchievementsScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class LeaderBoardScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class WaterScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class RecyclingScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class ElectricityScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'
        
class FuelScreen(Screen):
    def go_home(self):
        self.manager.current = 'home'

class GreenUpApp(App):
    user = None

    def build(self):
        register('jeV1sPLXL6cq8EsWAK0Zyoac8b97duQWyXYK7sfE','fl6hQ9dv94IbtA0I7kPzSrawL165HqupSjCFdo3D')
        
        # Create the screen manager
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        return sm

    def on_pause(self):
        # Here you can save data if needed
        return True

    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass


if __name__ == '__main__':
    GreenUpApp().run()
