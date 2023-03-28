from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.lang import Builder

class Nar1(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("ayo/kv/nar1.kv")
        super().__init__(*args, **kwargs)

    def calculate(self, cs_h2oad, cw_h2oad, heat_h2oad, h2oad):
        if cs_h2oad.text != "" and cw_h2oad.text != "" and heat_h2oad.text != "" and h2oad.text != "":
            a = float(cs_h2oad.text)
            b = float(cw_h2oad.text)
            c = float(heat_h2oad.text)
            d = float(((c-a)/(a-b))*100)
            self.root.ids.h2oad.text = f"{d}"
            