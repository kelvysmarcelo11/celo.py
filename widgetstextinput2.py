from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 

class MinhaApp(App): 
    def build(self): 

     layout_principal = BoxLayout(orientation="vertical") 


     self.input_nome = TextInput(hint_text="Digite seu Nome")
     layout_principal.add_widget(self.input_nome)  


     botao_enviar = Button(text="Enviar", on_press=self.exibir_mensagem) 
     layout_principal.add_widget(botao_enviar) 


     self.label_mensagem = Label()



