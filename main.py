from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.card import MDCard
from kivy.properties import NumericProperty
from kivy.properties import StringProperty, ColorProperty, BooleanProperty,Property
from kivy.lang import Builder

kv = '''
<GoodOne>:
    first:first_lab
    second:second_lab
    signy:sign
    md_bg_color:"#000000"
    orientation:"vertical"
    MDBoxLayout:
        size_hint:1,.3
        MDLabel:
            id:sign
            theme_text_color:"Custom"
            text_color:"white"
            font_style:"H2"
            halign:"center"
            size_hint:.1,1
        MDBoxLayout:
            orientation:"vertical"
            MDLabel:
                id:second_lab
                theme_text_color:"Custom"
                text_color:"white"
                font_style:"H2"
                halign:"right"
            MDLabel:
                id:first_lab
                theme_text_color:"Custom"
                text_color:"white"
                font_style:"H2"
                halign:"right"
    GridLayout:
        size_hint:1,.7
        cols:4
        padding:10
        spacing:10
        WhiteButton:
            text:"AC"
            on_release:root.clean()
        WhiteButton:
            text:"+/-"
        WhiteButton:
            text:"%"
            on_release:root.make_sign(self.text)
        CoolButton:
            text:"/"
            on_release:root.make_sign(self.text)
        GrayButton:
            text:"7"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"8"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"9"
            on_release:root.get_text(self.text)
        CoolButton:
            text:"X"
            on_release:root.make_sign(self.text)
        GrayButton:
            text:"4"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"5"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"6"
            on_release:root.get_text(self.text)
        CoolButton:
            text:"+"
            on_release:root.make_sign(self.text)
        GrayButton:
            text:"1"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"2"
            on_release:root.get_text(self.text)
        GrayButton:
            text:"3"
            on_release:root.get_text(self.text)
        CoolButton:
            text:"-"
            on_release:root.make_sign(self.text)
        GrayButton:
            text:"π"
            
        GrayButton:
            text:"0"
            on_release:root.get_text(self.text)
        GrayButton:
            text:","
        CoolButton:
            text:"="
            on_release:root.equalise()
        
<CalcButton>:
    md_bg_color:"#000000"
    size:80, 80
    radius:[250,]
    MDLabel:
        id:txt
        text:root.text
        halign:"center"
        theme_text_color:"Custom"
        text_color:root.t_color
        font_style:"H3"
        
<WhiteButton@CalcButton>:
    md_bg_color:"#ffffff"
    t_color:"black"
<CoolButton@CalcButton>:
    md_bg_color:"orange"
    t_color:"white"
<GrayButton@CalcButton>:
    md_bg_color:"gray"
    t_color:"white"
'''
Builder.load_string(kv)
class CalcButton(MDCard):
    text = StringProperty()
    t_color = ColorProperty()
    
            
class GoodOne(MDBoxLayout):
    number_1 = NumericProperty()
    number_2 = NumericProperty()
    answer = NumericProperty()
    
    def get_text(self, number):
        first_num = self.first.text+number
        self.first.text = first_num
        
    def make_sign(self, sign):
        self.second.text = self.first.text
        self.first.text = ""
        self.signy.text = sign
        
    def equalise(self):
        answer = 0
        number_1 = int(self.second.text)
        number_2 = int(self.first.text)
        
        if self.signy.text == "+":
            answer = number_1 + number_2
        elif self.signy.text == "-":
            answer = number_1 + number_2
        elif self.signy.text == "/":
            answer = number_1 / number_2
        elif self.signy.text == "X":
            answer = number_1 * number_2
        elif self.signy.text == "%":
            answer = number_1 % number_2
            
        self.second.text = ""
        self.signy.text = ""
        self.first.text = str(answer)
        
    def clean(self):
        if self.first.text == "":
            pass
        else:
            texty = self.first.text
            new_text = texty.rstrip(texty[-1])
            self.first.text = new_text
        
class GoodApp(MDApp):
    def build(self):
        return GoodOne()
        
if __name__=="__main__":
    GoodApp().run()