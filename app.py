import kivy
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from views.views import *
from widgets.widgets import *

Builder.load_file("views/master_list_view.kv")
Builder.load_file("views/add_new_task_view.kv")
Builder.load_file("views/edit_task_view.kv")
Builder.load_file("views/delete_warning_view.kv")
Builder.load_file("widgets/ToDoItemView.kv")
Builder.load_file("screen_manager.kv")
Builder.load_file("style.kv")

window_scale = 1
Window.size = (412 * window_scale, 917 * window_scale)

class ToDoScreenManager(ScreenManager):
    pass

class ToDoApp(App):
    def build(self):
        return ToDoScreenManager()

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
