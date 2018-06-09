from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
class MyApp(App):
	def build(self):
		fl = FloatLayout(size =	(300,300))
		s=Scatter()
		s.add_widget(fl)
		fl.add_widget(Button(text="frst bttn", font_size=30,on_press=self.btn_press,size_hint=(.5,.25),pos=(0,0)))
		
		return s
	def btn_press(self,instance):
		print('Najal')
		instance.text='Gg'
	
	
if True:
	MyApp().run()