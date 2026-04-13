import time, requests, base64
from jnius import autoclass

# Set your Render URL here
URL = "https://viraj-remote-controller.onrender.com"
# The API Key is passed from main.py
API_KEY = "GET_FROM_ARGUMENT" 

def start_worker():
    RemoteControl = autoclass('org.viraj.remotetap.RemoteControl')
    
    while True:
        try:
            # 1. Capture Screen (Using Java logic)
            # This part requires the phone to have Accessibility ON
            # For now, we simulate the loop for command checking
            r = requests.get(f"{URL}/get_command?key={API_KEY}", timeout=2)
            if r.status_code == 200:
                data = r.json()
                if data['action'] == 'tap':
                    RemoteControl.instance.autoClick(data['x'], data['y'])
        except:
            pass
        time.sleep(0.5)

if __name__ == '__main__':
    start_worker()