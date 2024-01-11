import os
import time
# import pygame
b = True
if b:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    OUT_PIN = 23
    IN_PIN = 24
    GPIO.setup(OUT_PIN, GPIO.OUT)
    GPIO.setup(IN_PIN, GPIO.IN)
import requests
def get_public_ip():
    """Get the public IP address of this machine."""
    response = requests.get('https://api.ipify.org')
    return response.text

# Example usage:
# public_ip = get_public_ip()
# print(f"The public IP address of this machine is: {public_ip}")

ip = get_public_ip()
# Initialize Pygame
# pygame.init()

# Set up the display
# window_size = (400, 400)
# screen = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Pygame Window with White Square")

# Define the square properties
# square_size = (50, 50)
# square_color = (255, 255, 255)  # White color
# square_position = (window_size[0] // 2 - square_size[0] // 2, window_size[1] // 2 - square_size[1] // 2)
data = []
# Create a Timer class to track time elapsed
class Timer:
    def __init__(self):
        self.start_time = None  # Time when the timer was started

    def start(self):
        """Start the timer."""
        self.start_time = time.perf_counter()

    def elapsed(self):
        """Return the elapsed time since the timer was started."""
        if self.start_time is None:
            raise ValueError("Timer must be started with .start() method.")
        return time.perf_counter() - self.start_time

    def reset (self):
        """Reset the timer."""
        self.start_time = None
# Initialize the timer instance
timer = Timer()
triggered = False
def down():
    # Code to be executed when mouse button is pressed
    if b:
        GPIO.output(OUT_PIN, GPIO.HIGH)
    strin = f"d {timer.elapsed()};"
    print(strin)
    data.append(strin)


def up():
    # Code to be executed when mouse button is released
    if b:
        GPIO.output(OUT_PIN, GPIO.LOW)
    strin = f"u {timer.elapsed()};"
    print(strin)
    data.append(strin)

def sP():
    current_time = time.perf_counter()
    print(data)
    with open(os.getcwd() + f'/{current_time}.txt', 'w') as f:
        f.writelines(data)
    for i in data:
        data.pop()

# Game loop
running = True
timer.start()
prev = 0
try:
    while running:
        input =  GPIO.input(IN_PIN)
        if input == 1 and input != prev:
            down()
            timer.reset()
            timer.start()
            triggered = False
            prev = input
        elif input == 0 and input != prev:
            up()
            timer.reset()
            timer.start()
            triggered = False
            prev = input

        if timer.elapsed() > 5 and not triggered and data[data.__len__() - 1].split(" ")[0] != "d":
            sP()
            triggered = True
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program was terminated by the user.")
