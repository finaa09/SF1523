from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from kivy.lang import Builder


class Coal(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file('ayo/kv/coal.kv')
        super().__init__(*args, **kwargs)

    def open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value):
        self.ids.date_field.text = str(value)

    def on_cancel(self, instance, value):
        self.ids.date_field.text = "Canceled"

    
    


    