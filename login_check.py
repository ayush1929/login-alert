import cv2
import datetime
import os
import time
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email credentials and settings
sender_email = os.getenv('EMAIL_USERNAME')
password = os.getenv('EMAIL_PASSWORD')
receiver_email = 'your-email@example.com'  # Replace with the actual receiver's email address

# Check if environment variables are loaded
if not sender_email or not password:
    print("Error: EMAIL_USERNAME or EMAIL_PASSWORD environment variables are not set.")
    exit(1)

# Define the directory where logs and images will be saved
LOG_DIR = "C:\\Users\\AYUSH\\OneDrive\\Desktop\\GitHub\\login-alert\\logs and images"  # Change this path to your preferred directory
LOG_FILE = os.path.join(LOG_DIR, "login_log.txt")
IMAGE_DIR = os.path.join(LOG_DIR, "images")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)


def capture_image():
    """Capture an image from the webcam and save it."""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None, None
    
    # Allow the camera to warm up
    time.sleep(1)  # Warm-up period

    # Capture an initial frame to assess light level
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read image from webcam.")
        cap.release()
        return None, None


    # Capture the final frame with adjusted settings
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read image from webcam.")
        cap.release()
        return None, None
    
    # Save the image with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = os.path.join(IMAGE_DIR, f"user_{timestamp}.png")
    cv2.imwrite(image_filename, frame)
    
    cap.release()
    return image_filename, timestamp

def log_login(timestamp):
    """Log the login time."""
    formatted_time = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")  # Format: Day Month Year, Hour:Minute:Second AM/PM
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"Login detected at {formatted_time}\n")
    
    print(f"Login logged at {formatted_time}")

def send_email(image_filename, timestamp):
    """Send an email with the captured image and login details."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Login Detected: {timestamp}"
    
    formatted_timestamp = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
    body = (
        f"A login was detected on {formatted_timestamp}.\n\n"
        f"Please find the attached image that was captured during the login event.\n\n"
        f"Image Filename: {os.path.basename(image_filename)}\n\n"
        "Have a good day,\n"
        "Security System."
    )
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with open(image_filename, 'rb') as img_file:
            img = MIMEImage(img_file.read(), name=os.path.basename(image_filename))
            msg.attach(img)
        
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")
    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    formatted_timestamp = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
    log_login(formatted_timestamp)
    image_filename, timestamp = capture_image()
    if image_filename:
        send_email(image_filename, formatted_timestamp)
