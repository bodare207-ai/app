import random, string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from android.permissions import request_permissions, Permission

class VirajRemoteApp(App):
    def build(self):
        self.api_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="VIRAJ REMOTE SYSTEM", font_size='24sp', color=(0,1,0,1)))
        
        self.key_label = Label(text=f"API KEY: {self.api_key}", font_size='30sp')
        layout.add_widget(self.key_label)
        
        perm_btn = Button(text="1. GRANT PERMISSIONS", size_hint_y=None, height=100)
        perm_btn.bind(on_press=self.ask_perm)
        layout.add_widget(perm_btn)
        
        start_btn = Button(text="2. START & HIDE", size_hint_y=None, height=100, background_color=(0,1,0,1))
        start_btn.bind(on_press=self.run_hidden)
        layout.add_widget(start_btn)
        
        return layout

    def ask_perm(self, instance):
        request_permissions([Permission.INTERNET, Permission.FOREGROUND_SERVICE])

    def run_hidden(self, instance):
        from android import mActivity
        from jnius import autoclass
        service = autoclass('org.viraj.remotetap.ServiceRemoteservice')
        service.start(mActivity, self.api_key)
        # Minimize the app
        mActivity.moveTaskToBack(True)

if __name__ == '__main__':
    VirajRemoteApp().run()