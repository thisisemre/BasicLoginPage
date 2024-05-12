# Flask User Authentication System

This Flask application provides a robust user authentication system, facilitating user registration, login, password reset, and session management. It leverages Flask-Login for session management and Flask-Bcrypt for password hashing.

## Features

- **User Registration:** New users can easily create an account by providing a unique username, a valid email address, and a secure password.

- **User Login:** Registered users can log in using either their username or email along with their password.

- **Password Reset:** In case a user forgets their password, they can request a password reset. A secure password reset link is sent to their registered email address.

- **Change Password:** Upon receiving the password reset link, users can securely reset their password by providing a new one.

- **Session Management:** User sessions are securely managed using Flask-Login, providing a seamless and secure user experience.

## File Structure

- **app.py:** The main Flask application file containing routes for user authentication (login, registration, password reset) and the main dashboard.

- **forms.py:** This file defines Flask-WTF forms for various user actions like login, registration, password reset request, and password reset.

- **user.py:** Defines the User model and database configurations, handling user-related database operations.

- **mail.py:** Provides functions for sending emails, particularly for sending password reset links.

## Usage

1. **Registration:** Users can register by navigating to the registration page and providing necessary details.

2. **Login:** Registered users can log in using their credentials.

3. **Password Reset Request:** If a user forgets their password, they can request a password reset via email.

4. **Reset Password:** Upon receiving the password reset link, users can set a new password securely.

5. **Logout:** Users can log out of their account securely.

## Contributing

Contributions to this project are encouraged! If you have any suggestions, feature requests, or bug reports, feel free to open an issue or submit a pull request.



Feel free to adjust the formatting or content as needed for your GitHub repository.
