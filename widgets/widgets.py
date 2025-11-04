from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ColorProperty
from kivy.utils import get_color_from_hex as hex

class ToDoItemView(BoxLayout):
    title = StringProperty("<title_placeholder>")
    completed = StringProperty("<completed_placeholder>")    
    completed_ind_color = ColorProperty(hex("#DD9292"))
    