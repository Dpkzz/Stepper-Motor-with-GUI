import RPi.GPIO as GPIO
import time
import tkinter as tk

# GPIO pin setup
in1 = 14
in2 = 15
in3 = 18
in4 = 23

# Initial RPM and direction
rpm = 0
direction = False  # True for clockwise, False for counter-clockwise
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# Initialize the motor pins
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

motor_pins = [in1, in2, in3, in4]
motor_step_counter = 0

# Stepper motor sequence
step_sequence = [[1, 0, 0, 1],
                 [1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 1]]


def show_alert():  # Accept a message parameter
    # Create a Toplevel window
    stop_motor()
    alert = tk.Toplevel()
    alert.title("ALERT")
    alert.geometry("300x100")
    alert.resizable(False, False)

    # Center the window on the screen
    screen_width = alert.winfo_screenwidth()
    screen_height = alert.winfo_screenheight()
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (100 // 2)
    alert.geometry(f"300x100+{x}+{y}")

    # Add a message label
    label = tk.Label(alert, text="entered values beyond limit", font=('Arial', 14), padx=20, pady=20)
    label.pack()

    # Schedule the window to close after 'duration' milliseconds
    alert.after(2000, alert.destroy)  # Use the provided duration

def anticlcokwise():
	global direction
	direction  = False
# Function to clean up GPIO

def clcokwise():
	global direction
	direction  = True
# Function to clean up GPIO


def cleanup():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()
def fun(event):
	root.destroy()
# Function to start the motor
def start_motor():
    global running
    running = True
    rotate_motor()

# Function to stop the motor
def stop_motor():
    global running
    running = False

# Function to rotate the motor
def rotate_motor():
    global motor_step_counter
    if rpm > 20:
        show_alert()  # Show alert if RPM is greater than 25
        return  # Exit the function if RPM exceeds 25

    step_sleep = 60.0 / (rpm * 4096)
    while running:
        for pin in range(4):
            GPIO.output(motor_pins[pin], step_sequence[motor_step_counter][pin])

        if direction:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            motor_step_counter = (motor_step_counter + 1) % 8

        time.sleep(step_sleep)
        root.update()

# Function to update the RPM based on user input
def update_rpm():
    global rpm, direction
    try:
        rpm = int(rpm_entry.get())
        print(rpm)
        rpm_label.config(text=f"Current RPM: {rpm}")
        start_motor()
        
    except ValueError:
        show_alert("Please enter a valid integer for RPM", 1000)




# Create the Tkinter GUI
root = tk.Tk()
root.title("Stepper Motor Control")

# RPM display
rpm_label = tk.Label(root, text=f"Current RPM: {rpm}", font=("Arial", 14))
rpm_label.pack(pady=10)

# RPM entry
rpm_entry = tk.Entry(root, font=("Arial", 14))
rpm_entry.pack(pady=10)

# Button to update RPM
update_button = tk.Button(root, text="Update RPM", font=("Arial", 14), command=update_rpm)
update_button.pack(pady=10)

# Start and Stop buttons
start_button = tk.Button(root, text="Start Motor", font=("Arial", 14), command=start_motor)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Motor", font=("Arial", 14), command=stop_motor)
stop_button.pack(pady=10)

anticlk = tk.Button(root, text="Anticlock Wise Direction", font=("Arial", 14), command=clcokwise)
anticlk.pack(pady=10)


clk = tk.Button(root, text="Clock Wise Direction",font=("Arial", 14), command=anticlcokwise)
clk.pack(pady=10)



root.geometry('500x500')
# Handle cleanup on exit
root.protocol("WM_DELETE_WINDOW", cleanup)
root.attributes("-fullscreen",True)
root.bind("<Escape>",fun)
#root.bind("<Enter>",update_rpm)
# Start the Tkinter event loop
root.mainloop()
