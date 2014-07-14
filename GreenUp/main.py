import kivy
kivy.require('1.1.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition




#from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#from parse_rest.datatypes import Object
#from parse_rest.connection import register







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
        
class RecyclingBoardScreen(Screen):
    pass
        
class ElectricityBoardScreen(Screen):
    pass
        
class FuelBoardScreen(Screen):
    pass






class MyWidget(Widget):
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    
    def my_callback(instance, value, action, color):
        if action == 1:
            colorData = ColorButton(colorOfButton = color)
            colorData.save()
            print('Saved a new ColorButton with color %s.' % color)
        elif action == 0:
            colorData = ColorButton.Query.filter(colorOfButton = color)
            if colorData.count() >= 1:
                colorData = colorData.limit(1).get()
                colorData.delete()
                print('Deleted a ColorButton with color %s.' % color)
            else:
                print('No ColorButtons with color %s to delete.' % color)

class ColorButton(Object):
    pass
    
class GreenUpApp(App):
    def build(self):
        #register('ns8i6BTFDzQHlx50ZDSXYhnaCLlyTyWnVTJyYkEm','UPXReuTMMmObBOSZ1k1cfggmoapENKOb2H9fxBDm')
        
        # Create the screen manager
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    GreenUpApp().run()
