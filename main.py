from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager

class WindowManager(ScreenManager):
    pass

class Test(MDApp):
    def build(self):
        return super().build()
    
if __name__ == "__main__":
    Test().run()