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

## Screenshots

### Login Page
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/22ea4b9f-3ad7-4190-bcdc-977d46b2d9f3)


### Register Page
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/92b379cb-432e-4dab-94c9-8b88199b6c05)


### Main Page
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/881b2cbe-73b1-403e-9f93-0b1f42281a0c)


### Change Password Page
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/7f066453-8879-404a-ae12-fbdd2c215c9b)


### Reset Password Page
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/eba07c94-3429-4734-8128-4eaf79abee49)
![image](https://github.com/thisisemre/BasicLoginPage/assets/106868668/036a18fc-d239-44fa-9fa3-6d6a28457f77)



## Contributing

Contributions to this project are encouraged! If you have any suggestions, feature requests, or bug reports, feel free to open an issue or submit a pull request.
