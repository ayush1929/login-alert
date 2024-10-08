# Login Alert Script

This script is designed to notify you via email whenever someone logs into your laptop. It captures an image using the webcam and sends it along with the login timestamp to a specified email address. This can be particularly useful for monitoring unauthorized access or keeping a record of logins on shared devices.

## Features
- **Login Detection**: Automatically logs the time and date when someone logs in.
- **Image Capture**: Captures an image using the laptop's webcam.
- **Email Notification**: Sends an email notification with the captured image attached.

## Prerequisites

- **Python**: Ensure Python is installed on your system. The script is compatible with Python 3.x versions.
- **Python Packages**: The following packages need to be installed:

```bash
pip install opencv-python-headless numpy python-dotenv
```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ayush1929/login-alert.git
   cd login-alert
   ```

2. **Create a Gmail App Password**:
   - Go to your [Google Account](https://myaccount.google.com/).
   - Navigate to **Security** > **App passwords**.
   - Generate an app password for "Mail" on "Windows Computer".
   - Save this password, as you'll need it in the next step.

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project directory:
     ```bash
     touch .env
     ```
   - Open the `.env` file and add the following:
     ```env
     EMAIL_USERNAME=your-email@gmail.com
     EMAIL_PASSWORD=your-app-password
     ```
   - Replace `your-email@gmail.com` with your Gmail address and `your-app-password` with the password you generated in the previous step.

4. **Modify the Receiver Email**:
   - Open [`login_check.py`](login_check.py).
   - Replace `'your-email@example.com'` with the email address where you want to receive login alerts:
     ```python
     receiver_email = 'your-email@example.com'
     ```

5. **Define the Log and Image Directory**:
   - By default, the script saves logs and images in `C:\login-alert\logs and images`. You can change this directory by modifying the `LOG_DIR` variable in the script:
     ```python
     LOG_DIR = "C:\\your-preferred-directory\\logs and images"
     ```

## Running the Script Automatically

To ensure that the script runs automatically whenever your laptop starts, you have two options:

### Option 1: Place the Script in the Startup Folder
- Copy or create a shortcut of the [`login_check.py`](login_check.py) file in the Windows Startup folder.
- To access the Startup folder, press `Win + R`, type `shell:startup`, and hit Enter.
- Place the script or its shortcut in this folder.

### Option 2: Set Up a Task Scheduler
- Open Task Scheduler by searching for it in the Start menu.
- Create a new task and set it to trigger on login.
- Set the action to run the [`login_check.py`](login_check.py) script.

## Usage

To run the script manually, simply execute it with Python:

```bash
python login_check.py
```

When someone logs in to your laptop, the script will:
1. Capture an image using the webcam.
2. Log the login time and date.
3. Send an email notification with the captured image and login details.

## Customization

You can further customize the script by modifying the following:

- **Email Subject**: Change the subject line of the email by editing the `msg['Subject']` line in [`login_check.py`](login_check.py).
- **Logging**: Add more details to the log by modifying the `log_login()` function.
- **Notification**: Change the email body content or add additional attachments if needed.

## Example Output

### Console Output
When the script runs, you can expect to see the following messages in the console:

```
Login logged at 15 August 2024, 10:23:45 AM
Email sent successfully.
```

### Email Notification
The email you receive will contain the following:

- **Subject**: `Login Detected: 15 August 2024, 10:23:45 AM`
- **Body**:
    ```
    A login was detected on 15 August 2024, 10:23:45 AM.

    Please find the attached image that was captured during the login event.

    Image Filename: user_20240815_102345.png

    Have a good day,
    Security System.
    ```
- **Attachment**: An image captured by the webcam at the time of login.

## Troubleshooting

- **Webcam Issues**: If the webcam fails to initialize, ensure that it’s not being used by another application, and check that the correct drivers are installed.
- **Email Not Sent**: If the email fails to send, verify that the environment variables (`EMAIL_USERNAME` and `EMAIL_PASSWORD`) are set correctly, and ensure that your laptop is connected to the internet.
- **Permission Errors**: Ensure that the script has the necessary permissions to access the webcam and the directories where logs and images are saved.

## Important Notes

- Ensure your laptop is connected to the internet when the script runs, or the email notification will fail.
- The script uses environment variables for storing sensitive information like your Gmail username and app password. This is a secure practice that prevents hardcoding credentials in the script.

## License

This project is licensed under the [MIT License](LICENSE). See the [`LICENSE`](LICENSE) file for more details.

