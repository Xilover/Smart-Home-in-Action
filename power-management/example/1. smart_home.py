'''
Here’s an example of Python code that simulates a basic smart home power management system. This code includes features like occupancy detection, time-based scheduling, and energy monitoring.
'''

```python
import time
from datetime import datetime, timedelta

class SmartHome:
    def __init__(self):
        self.devices = {}
        self.occupancy = False
        self.energy_usage = 0

    def add_device(self, name, power_rating):
        self.devices[name] = {'power_rating': power_rating, 'status': 'off'}
    
    def set_occupancy(self, status):
        self.occupancy = status
        self.manage_power()

    def manage_power(self):
        if not self.occupancy:
            for device in self.devices:
                self.turn_off_device(device)
        else:
            for device in self.devices:
                self.turn_on_device(device)

    def turn_on_device(self, device):
        if self.devices[device]['status'] == 'off':
            self.devices[device]['status'] = 'on'
            self.energy_usage += self.devices[device]['power_rating']
            print(f"{device} turned on. Current energy usage: {self.energy_usage} W")

    def turn_off_device(self, device):
        if self.devices[device]['status'] == 'on':
            self.devices[device]['status'] = 'off'
            self.energy_usage -= self.devices[device]['power_rating']
            print(f"{device} turned off. Current energy usage: {self.energy_usage} W")

    def schedule_device(self, device, start_time, end_time):
        current_time = datetime.now().time()
        if start_time <= current_time <= end_time:
            self.turn_on_device(device)
        else:
            self.turn_off_device(device)

    def monitor_energy(self):
        print(f"Total energy usage: {self.energy_usage} W")
        for device, info in self.devices.items():
            print(f"{device}: {'On' if info['status'] == 'on' else 'Off'}")

# Example usage
smart_home = SmartHome()
smart_home.add_device("Living Room Light", 60)  # 60W
smart_home.add_device("Thermostat", 150)         # 150W

# Simulate occupancy changes
smart_home.set_occupancy(True)  # House is occupied
time.sleep(1)
smart_home.set_occupancy(False) # House is unoccupied

# Schedule the living room light to turn on at 6 PM and off at 10 PM
start_time = (datetime.now() + timedelta(seconds=5)).time()  # 5 seconds from now
end_time = (datetime.now() + timedelta(seconds=15)).time()    # 15 seconds from now
smart_home.schedule_device("Living Room Light", start_time, end_time)

# Monitor energy usage
smart_home.monitor_energy()
```

'''
+Explanation:
- SmartHome Class: Manages devices, occupancy status, and energy usage.
- add_device: Adds devices with their power ratings.
- set_occupancy: Changes occupancy status and manages power accordingly.
- manage_power: Turns devices on or off based on occupancy.
- turn_on_device/turn_off_device: Controls device status and updates energy usage.
- schedule_device: Turns devices on/off based on a specified time range.
- monitor_energy: Displays current energy usage and device statuses.

This code can be expanded with more features like integration with actual sensors, user interfaces, and data logging for a complete smart home experience.
'''
