from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

#text, font_size, hint_text, multiline

class myapp(App):
    def build(self):
        layout_utama = BoxLayout(orientation="vertical")
        label1 = Label(text="Aplikasi", font_size=50)
        entry1 = TextInput(hint_text="Percobaan", font_size=50)
        button1 = Button(text="Tombol", font_size=50)
        layout_utama.add_widget(label1)
        layout_utama.add_widget(entry1)
        layout_utama.add_widget(button1)

        return layout_utama

        #return Label(text="Aplikasiku", font_size=38)
        #return Button(text="Tekan", font_size=38)
        #return TextInput(hint_text="Masukkan data di sini")


myapp().run() 