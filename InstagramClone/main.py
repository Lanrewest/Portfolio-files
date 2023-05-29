from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screen.home_page import HomePage



class InstagramApp(MDApp):
    def build(self):
        Window.size = [300, 500]
        self.load_all_kv_files()
        return HomePage()
    
    def load_all_kv_files(self):
        Builder.load_file('libs/screen/home_page.kv')
        Builder.load_file('libs/component/appbar.kv')
        Builder.load_file('libs/component/story_creator.kv')
    
    
if __name__ =="__main__":
    InstagramApp().run()
    