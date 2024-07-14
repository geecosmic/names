from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


KV = """
ScreenManager:

   

    Screen:
        name:"scr1"
        
        BoxLayout:
        
            orientation: 'vertical'

            canvas.before:
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    source: "pex14.jpg"

            MDTopAppBar:
                # id: top_bar
                title: "KABBALISTIC 72 NAMES OF GOD"
                # left_action_items: [["menu", lambda x: app.menu_open()]]  # Hamburger icon


    # --------for menu alignment----------------------------------------------------------- 
            FloatLayout:
                size_hint_y: None
                # height: dp(48)FloatLayout:
                size_hint_y: None
                # height: dp(48)
                    
                MDTextField:
                    id: top_bar
                    size_hint: None, None
                    size: "4dp", "4dp"
                    pos_hint: {"center_x": .0, "center_y": .0}

    # -----------------------------------------------------------------------------
            

                MDIconButton:
                    id: btsearch
                    icon: "magnify"
                    theme_bg_color: "Custom"
                    md_bg_color: "brown"
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    size_hint: None, None
                    size: "60dp", "60dp"
                    pos_hint: {"center_x": .545, "center_y": .49}
                    on_press:
                        if input.text == '' : pass
                        elif int(input.text) > 72: pass
                        else: carousel.index = (int(input.text) - 1)
                    on_release: input.text = ''

                MDTextField:
                    id: input
                    max_text_length: 2
                    hint_text: '1 - 72'
                    color: (1,1,1,1)
                    size_hint: None, None
                    size: "35dp", "35dp"
                    color_mode: 'custom'
                    helper_text_mode: "persistent"
                    line_color_normal: app.theme_cls.accent_color
                    input_filter: "int"
                    pos_hint: {"center_x": .456, "center_y": .5}

                

                MDIconButton:
                    id:fwd
                    icon: "arrow-left-bold-outline"
                    on_release:carousel.load_next()
                    # size_hint: (0.3,1)
                    # background_color: (1,0,0,1)
                    font_size:30
                    text_color: "yellow"
                    # size_hint: (0.3,1)
                    pos_hint: {"center_x": .29, "center_y": .5} 

                MDIconButton:
                    icon: "arrow-right-bold-outline"
                    id:back
                    # text: '<-'
                    on_release:carousel.load_previous()

                    # background_color: (1,0,0,1)
                    font_size:30
                    text_color: "yellow"
                    # size_hint: (0.3,1)
                    pos_hint: {"center_x": .7, "center_y": .5}

            MyCarousel:
                id: carousel
                size_hint_y: 0.8


            FloatLayout:
                size_hint_y: None
                height:dp(38)
                spacing:'3dp'    

                MDRoundFlatButton:
                    id:autoscan
                    text: 'Auto Scan'

                    # background_color: (1,0,0,1)
                    font_size:23
                    text_color: "yellow"
                    # size_hint: (0.3,1)
                    # pos_hint: {"center_x": .5, "center_y": 1}
                    pos_hint: {'x':0.415 , 'y':0.52 }

                    on_press:carousel.move() 
                    on_release:autoscan.opacity=0
                    on_release:pause.disabled=False
                    on_release:pause.opacity=1
                    on_release:fwd.opacity=0
                    on_release:back.opacity=0
                    on_release:input.opacity=0
                    on_release:btsearch.opacity=0
                    
                


                MDRoundFlatButton:
                    id:pause
                    text: 'Pause'
                    font_size:23
                    text_color: "yellow"
                    # pos_hint: {"center_x": .5, "center_y": 1}
                    pos_hint: {'x':0.427 , 'y':0.52 }

                    on_press:carousel.stop() 
                    
                    on_release:pause.disabled=True
                    on_release:pause.opacity=0
                    on_release:autoscan.opacity=1
                    on_release:autoscan.disabled=False
                    on_release:fwd.opacity=1
                    on_release:back.opacity=1
                    on_release:input.opacity=1
                    on_release:btsearch.opacity=1

        
                MDIconButton:
                    icon: "refresh-circle"
                    font_size:30
                    text_color: "yellow"
                    pos_hint: {'x':0.65 , 'y':0.52 }

                    on_release:carousel.index=0

                MDIconButton:                
                    icon:"menu"
                    font_size:30
                    text_color: "white"
                    pos_hint: {'x':0.243 , 'y':0.53 }
                    on_release: root.current = "scr2"
        

    Screen:
        name: "scr2"
        
        BoxLayout:
            orientation:'vertical'     

            ScrollView:
                
                BoxLayout:
                    orientation:'vertical' 
                    spacing:40
                    size_hint_y:None 
                    adaptive_height:True
                    height:self.minimum_height  
    
                    id:layout_1        

                    canvas.before:   
                        Color:
                            rgba:(0,0,0,1)
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            
                            # source:"pex4.jpg"
                            radius:[30]           
                            

                    Label:
                        text: "" 
                    Label:
                        text: "THE KABBALISTIC  72  NAMES OF  GOD " 
                        font_size:25
                        color:(1,0,0,1) 
                        bold:True  
                    
                    Label:
                        text: ""    
                    Label:
                        text: "1 -TIME TRAVEL / FIXING THE PAST"
                        
                    Label:
                        text: "2 - ENERGY BOOST"
                    Label:
                        text: "3 - MIRACLE MAKING "
                    
                    Label:
                        text: "4-ELIMINIATING NEGATIVE THOUGHTS"
                        
                    Label:
                        text: "5 -HEALING "
                        
                    Label:
                        text: "6 -UNDERSTANDING SUBCONSCIOUS MESSAGES"
                        
                    Label:
                        text: "7 -RESTORING TO THEIR PERFECT STATE"
                        
                    Label:
                        text: "8 -DEFUSING NEGATIVE ENERGY AND STRESS"
                    
                    Label:
                        text: "9 -CONTACTING ANGELS" 
                        
                    Label:
                        text: "10 -PROTECTION FROM EVIL EYE "
                        
                    Label:
                        text: "11 -PURIFYING PLACES AND SPACES"
                        
                    Label:
                        text: "12 -UNCONDITIONAL LOVE "
                        
                    Label:
                        text: "13 -HEAVEN ON EARTH"
                    Label:
                        text: "14 -DEFUSING CONFLICT"
                    Label:
                        text: "15 -FORESIGHT"  
                    Label:
                        text: "16 -DUMPING DEPRESSION "
                    Label:
                        text: "17 -DESTROY YOUR EGO"
                    Label:
                        text: "18 -FERTILITY"
                    Label:
                        text: "19 -DIALING GOD"
                    Label:
                        text: "20 -VICTORY OVER ADDICTION"
                        
                    Label:
                        text: "21 -ERADICATING PLAGUE "  
                    
                    Label:
                        text: "22 -STOP FATAL ATTRACTION"
                        
                    Label:
                        text: "23 -SHARING THE FLAME"
                    Label:
                        text: "24 -UNDOING CHAOS "
                    Label:
                        text: "25 -SPEAK YOUR MIND"
                    Label:
                        text: "26 -ORDER FROM CHAOS "
                    Label:
                        text: "27 -SILENT PARTNER "
                    Label:
                        text: "28 -ATTRACTING 'THE ONE'"
                    Label:
                        text: "29 -REMOVING HATRED"
                        
                    Label:
                        text: "30 -MENDING BROKEN RELATIONSHIPS"
                        
                    Label:
                        text: "31 -PERSEVERANCE/ FINISH WHAT YOU START"
                    
                    Label:
                        text: "32 -BANISHING TRAUMATIC MEMORIES"
                        
                    Label:
                        text: "33 -REMOVING OBSTACLES"  
                    Label:
                        text: "34 -CHANGING POINT OF VIEW"
                    Label:
                        text: "35 -SEXUAL ENERGY"
                    Label:
                        text: "36 -OVERCOMING FEARS"
                        
                    Label:
                        text: "37 -SEEING THE BIG PICTURE"
                    
                    Label:
                        text: "38 -CREATING CIRCUITRY"
                    
                    Label:
                        text: "39 -FINDING THE GOOD IN THE BAD" 
                        
                    Label:
                        text: "40 -SPEAKING THE RIGHT WORDS"
                    
                    Label:
                        text: "41 -SELF ESTEEM"
                    Label:
                        text: "42 -SEEING THE TRUTH"
                        
                    Label:
                        text: "43 -LEVITATION/MAKING THE IMPOSSIBLE,POSSIBLE"
                        
                    Label:
                        text: "44 -SWEETENING JUDGEMENT"
                    Label:
                        text: "45 -POWER OF PROSPERITY"
                    Label:
                        text: "46 -CERTAINTY"
                    Label:
                        text: "47 -WORLD PEACE"
                    Label:
                        text: "48 -UNITY"
                    Label:
                        text: "49 -HAPPINESS"
                    Label:
                        text: "50 -GOING THE EXTRA MILE"  
                    Label:
                        text: "51 -REMOVING GUILT"
                    Label:
                        text: "52 -PASSION"
                    Label:
                        text: "53 -GIVING WITHOUT AGENDA"
                    Label:
                        text: "54 -HOLDING IN TO THE GOOD "
                    Label:
                        text: "55 -THOUGHT INTO ACTION"
                    Label:
                        text: "56 -DISPELLING ANGER"
                    Label:
                        text: "57 -LISTENING TO THE SOUL"
                    Label:
                        text: "58 -LETTING GO"  
                    Label:
                        text: "59 -CONNECTING TO THE LIGHT"
                    Label:
                        text: "60 -FREEDOM"
                    Label:
                        text: "61 -PURIFYING WATER"
                        
                    Label:
                        text: "62 -PARENT, TEACHER, NOT PREACHER"
                        
                    Label:
                        text: "63 -APPRECIATION"
                    Label:
                        text: "64 -CASTING YOURSELS IN FAVOURABLE LIGHT"
                    
                    Label:
                        text: "65 -HUMILITY"
                    Label:
                        text: "66 -ACCOUNTABLITY"  
                    Label:
                        text: "67 -REMOVING EXPECTATIONS"
                    Label:
                        text: "68 -CONTACTING DEPARTED SOULS" 
                    Label:
                        text: "69 -FINDING A DIRECTION "
                    Label:
                        text: "70 -CREATING ORDER "
                    Label:
                        text: "71 -SEEING THE FUTURE/ PROPHETIC THINKING"    
                    Label:
                        text: "72 -SPIRITUAL CLEANSING"
                    Label:
                        text: ""    


            Button:                
                text: "Back To Scan"
                size_hint: (1,0.08)
                # pos_hint: {'x':0 , 'y':0.0 }
                on_release: root.current = "scr1" 
                background_color:(0.2,0.4,1,1)       
            






           
"""

class MyCarousel(Carousel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.direction = "right"
        for i in range(1, 73):
            src = f"names1/{i}-removebg-preview.png"
            image = AsyncImage(source=src, allow_stretch=True)
            self.add_widget(image)
        self.event = None

    def move(self):
        self.event = Clock.schedule_interval(self.load_next, 2)

    def stop(self):
        if self.event:
            self.event.cancel()

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_palette = "Blue"


        return Builder.load_string(KV)
    
        

    def on_start(self):
        self.root.ids.pause.disabled = True
        self.root.ids.pause.opacity=0


        self.menu_items = [
            {"text": "Automove", "on_release": lambda x="Automove": self.menu_callback(x)},
            {"text": "Stop", "on_release": lambda x="Stop": self.menu_callback(x)},
        ]
        top_bar = self.root.ids.top_bar
        self.menu = MDDropdownMenu(
            caller=top_bar,
            items=self.menu_items,
            width_mult=4
        )

    def menu_open(self):
        self.menu.open()

    def menu_callback(self, text_item):
        if text_item == "Automove":
            self.automove()
        elif text_item == "Stop":
            self.stop()
         

        

    def automove(self):
        carousel = self.root.ids.carousel
        if carousel:
            carousel.move()
            print("Automove called.")
        else:
            print("Carousel widget not found.")

    def stop(self):
        carousel = self.root.ids.carousel
        if carousel:
            carousel.stop()
            print("Stop called.")
        else:
            print("Carousel widget not found.")

if __name__ == "__main__":
    MyApp().run()
