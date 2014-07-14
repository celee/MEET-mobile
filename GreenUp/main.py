import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    error = ObjectProperty(None)

    def button_clicked(instance):
        if password.text == "hi":
            self.manager.switch_to(HomeScreen(username=self.username))
        else:
            error.text = "Username and password do not match. Try again."


class HomeScreen(Screen):
    username=''
    userDisplayName=''

    def __init__(self,username):
        self.username = username
        self.userDisplayName = username

class SettingsScreen(Screen):
    pass
        
class ProfileScreen(Screen):
    pass
        
class AchievementScreen(Screen):
    pass
        
class LeaderBoardScreen(Screen):
    pass
        
class WaterBoardScreen(Screen):
    pass
        
class RecyclingScreen(Screen):
    pass
        
class ElectricityScreen(Screen):
    pass
        
class FuelScreen(Screen):
    pass

class GreenUpApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        # sm.add_widget(SettingsScreen(name='settings'))
        # sm.add_widget(ProfileScreen(name='profile'))
        # sm.add_widget(AchievementScreen(name='achievement'))
        # sm.add_widget(LeaderBoardScreen(name='leader'))
        # sm.add_widget(WaterScreen(name='water'))
        # sm.add_widget(RecyclingScreen(name='recycling'))
        # sm.add_widget(ElectricityScreen(name='electric'))
        # sm.add_widget(FuelScreen(name='fuel'))
        return sm

if __name__ == '__main__':
    GreenUpApp().run()
