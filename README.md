# Django Authentication System

This project implements a user authentication system using Django. It includes features like login, signup, forgot password, change password, and a dashboard with profile access. 

## Features

- **User Authentication**: Login and signup with email or username.
- **Password Management**: Forgot password functionality with email reset, and change password for authenticated users.
- **Profile Management**: View profile details like username, email, and date joined.
- **Access Control**: Restrict access to certain pages for authenticated users only.
- **Logout Functionality**: Easily log out from the system.

## Installation

### Prerequisites
- Python 3.8 or later
- Django 4.x
- SMTP access for sending emails

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/abhayg951/WhatBytes.git
    cd WhatBytes
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

---

## Email Configuration for Forgot Password

To enable the forgot password feature, add the following email settings to your `settings.py` file:

### Development (Console Backend)
For development, you can use Django's console backend to print emails to the console:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Production (SMTP Backend)
For production, configure your SMTP server:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Change this based on your email provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password_or_app_specific_password'
```

Replace `your_email@example.com` and `your_password_or_app_specific_password` with your actual email credentials.

---

## Folder Structure

```
<repository-name>/
├── myapp/                # Django app directory
│   ├── templates/        # HTML templates
│   ├── views.py          # Views for handling requests
│   ├── models.py         # Database models
│   └── urls.py           # URL patterns
├── manage.py             # Django's command-line utility
├── settings.py           # Project settings
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## Demo Video

[Watch Demo Video](https://loom.com)  
This video demonstrates the features and explains the implementation details.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
