import subprocess
from clean import output_giver  # Assuming clean has TheOutputGiver properly implemented
import time

class Brightness:
    current_brightness = None  # Track current brightness to avoid redundant calls

    @staticmethod
    def setbright(value):
        # Ensure the value is between 0 and 96000, and scale it to 0-100% brightness
        percentage_value = (value / 96000) * 100
        percentage_value = min(max(percentage_value, 0), 100)  # Clamp value between 0 and 100%
        
        # Check if the brightness has changed more than 1% to avoid unnecessary updates
        if Brightness.current_brightness is None or abs(percentage_value - Brightness.current_brightness) >= 1:
            Brightness.current_brightness = percentage_value
            print(f"Setting brightness to: {percentage_value:.2f}%")
            
            # Use the subprocess to set the brightness
            subprocess.run(['brightnessctl', 'set', f'{percentage_value:.2f}%'], check=True)
        else:
            print(f"Brightness is already near {percentage_value:.2f}%, skipping update.")

# Initialize generator from TheOutputGiver class
Generator = output_giver.looper()

# Continuously fetch values from the generator and adjust brightness
for x in Generator:
    # Avoid unnecessary delays
    Brightness.setbright(x)
