import kivy
kivy.require('1.1.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class HomeScreen(Screen):
    pass

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
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(AchievementScreen(name='achievement'))
        sm.add_widget(LeaderBoardScreen(name='leader'))
        sm.add_widget(WaterScreen(name='water'))
        sm.add_widget(RecyclingScreen(name='recycling'))
        sm.add_widget(ElectricityScreen(name='electric'))
        sm.add_widget(FuelScreen(name='fuel'))
        return sm

if __name__ == '__main__':
    GreenUpApp().run()
