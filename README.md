# Django Blog Website

This is a simple blog website built with Django, a high-level Python web framework.

## Features

* **Blog Post Creation:** Users with appropriate permissions can create new blog posts.
* **Post Display:** Displays a list of blog posts with titles, excerpts, and publication dates.
* **Detailed Post View:** Allows users to view the full content of a blog post.
* **Basic Commenting System:** (Optional, if implemented) Enables users to leave comments on blog posts.
* **Admin Interface:** Django's built-in admin interface for managing posts, users, and other data.
* **Responsive Design:** (If implemented) Ensures the website looks good on various screen sizes.

## Prerequisites

* Python (3.8 or later)
* pip (Python package installer)
* Virtual environment (recommended)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    * **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (If you don't have a requirements.txt, you can install django with `pip install django`)

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user.

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8.  **Access the website:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

9.  **Access the admin interface:**

    Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## Project Structure