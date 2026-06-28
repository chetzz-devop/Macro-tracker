# Macro Tracker

A lightweight Django web application for tracking food macros and logging personal nutrition intake.

## Overview

This project provides a simple macro tracking dashboard where authenticated users can log foods, view their consumed items, and remove entries. The app uses Django models, views, templates, and SQLite for storage.

## Features

- Food item database with macro values for carbs, fats, proteins, and calories
- User-specific food consumption logs
- Automatic dashboard aggregation of total carbs, fats, proteins, and calories
- Daily energy progress gauge that updates from logged calorie totals
- Secure POST handling for authenticated users
- Delete ability for consumed food entries with class-based view support
- Responsive UI built with plain HTML and modern CSS styling
- Admin panel registration for `Food` and `Consumer` models

## Business Logic

- Aggregates user food entries on page load to compute total macros and calories
- Updates macro summary cards and calorie progress bar dynamically in the UI
- Stores history per authenticated user using the `Consumer` model to link food logs to users

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS

## Project Structure

- `mysite/manage.py` - Django management entry point
- `mysite/mysite/settings.py` - Django settings and project configuration
- `mysite/myapp/models.py` - `Food` and `Consumer` database models
- `mysite/myapp/views.py` - app views for logging and deleting food entries
- `mysite/myapp/urls.py` - app URL routes
- `mysite/myapp/templates/myapp/index.html` - main frontend dashboard
- `mysite/myapp/admin.py` - admin registration for models
## Screen Shots 
Only Authorized Users can Access
<img width="1847" height="857" alt="Screenshot 2026-06-28 194525" src="https://github.com/user-attachments/assets/b27b7a86-b7d0-4a28-a793-a9605458dbb0" />

Items TO track Calories
<img width="1912" height="967" alt="Screenshot 2026-06-28 194728" src="https://github.com/user-attachments/assets/f968d6cb-7967-44b1-9172-3f8a01161aeb" />

Total macros calculation
<img width="1860" height="721" alt="image" src="https://github.com/user-attachments/assets/23de7668-a490-41c5-9d88-cdf097eeef4c" />

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install Django
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the app in your browser:
   - App: `http://127.0.0.1:8000/food/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Usage

- Add food items through the admin panel.
- Log food consumption from the dashboard when signed in.
- Remove logged food entries from the dashboard.

## Notes

- `DEBUG` is enabled for development in `mysite/mysite/settings.py`.
- This project is intended as a lightweight example and may require hardening before production use.
