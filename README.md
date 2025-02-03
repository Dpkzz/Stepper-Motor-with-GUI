# # Stepper Motor Control with Raspberry Pi & Tkinter  

This project provides a graphical user interface (GUI) using Tkinter to control a **28BYJ-48 stepper motor** connected to a Raspberry Pi. It allows users to set the **RPM**, **start/stop the motor**, and change the **rotation direction** (clockwise or counterclockwise).  

## Features  

✔ Start and stop the stepper motor  
✔ Set RPM via a user input field  
✔ Prevent RPM values beyond the limit (displays an alert if RPM > 20)  
✔ Change rotation direction (clockwise or counterclockwise)  
✔ Exit the GUI using the `Escape` key  
✔ Runs in **fullscreen mode**  

## Hardware Requirements  

- **Raspberry Pi** (any model with GPIO support)  
- **28BYJ-48 Stepper Motor**  
- **ULN2003 Stepper Motor Driver**  
- **Power Supply (5V)**  

## Software Requirements  

- **Python 3**  
- **RPi.GPIO** library (`pip install RPi.GPIO`)  
- **Tkinter** (included with Python)  

## GPIO Pin Configuration  

| Motor Pin | Raspberry Pi GPIO |  
|-----------|------------------|  
| IN1       | GPIO 14 (BCM)     |  
| IN2       | GPIO 15 (BCM)     |  
| IN3       | GPIO 18 (BCM)     |  
| IN4       | GPIO 23 (BCM)     |  

## Installation & Setup  

1. Install required libraries:  
   pip install RPi.GPIO
2. Run the file
3. Use the GUI to enter an RPM value and control the motor.
   
## How It Works
The RPM is set using an input field.
The Start Motor button begins rotation based on the set RPM.
The Stop Motor button halts the rotation.
The Clockwise & Anticlockwise buttons change the motor direction.
If an RPM greater than 20 is entered, the motor stops, and an alert appears.
Pressing the Escape key (Esc) closes the application.
