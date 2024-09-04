import os
import subprocess
import time
import ctypes
from datetime import datetime
import schedule as sc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants from environment
WIFI_INTERFACE = os.getenv('WIFI_INTERFACE', 'Wi-Fi')
PING_HOSTNAME = os.getenv('PING_HOSTNAME', 'www.google.com')
PING_TIMEOUT = int(os.getenv('PING_TIMEOUT', 1))

# Interface class to handle Wi-Fi operations (Single Responsibility and Open-Close principles)
class WiFiManager:
    def enable(self):
        subprocess.call(f"netsh interface set interface {WIFI_INTERFACE} enabled")
        print("Turning On the laptop WiFi")

    def disable(self):
        subprocess.call(f"netsh interface set interface {WIFI_INTERFACE} disabled")
        print("Turning Off the laptop WiFi")

# Job that handles Wi-Fi stability checks (also follows Single Responsibility Principle)
class WiFiJob:
    def __init__(self, wifi_manager):
        self.wifi_manager = wifi_manager

    def check_connection(self):
        if subprocess.call(f"ping -n {PING_TIMEOUT} {PING_HOSTNAME}") != 0:
            print("Your Connection is not working")
            self.wifi_manager.disable()
            time.sleep(1)
            self.wifi_manager.enable()
        else:
            print("WiFi is enabled and connected to the internet")

# Admin check via the Factory method pattern
class AdminValidator:
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as e:
            print(f"Error checking admin status: {e}")
            return False

# Main application
def main():
    wifi_manager = WiFiManager()
    job = WiFiJob(wifi_manager)
    admin_validator = AdminValidator()

    if admin_validator.is_admin():
        sc.every(50).seconds.do(job.check_connection)
        while True:
            sc.run_pending()
            time.sleep(1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Entry point
if __name__ == "__main__":
    main()
