## Referral System

This project implements a referral system using Django and Django REST Framework (DRF). It allows users to register and optionally provide a referral code during signup. Users who successfully refer others earn points as a reward.

**Features:**

- User registration with email, password, and optional referral code.
- User details endpoint (authenticated access).
- Referrals endpoint (authenticated access) to list users who registered using the current user's referral code (paginated).

**Requirements:**

- Python (version 3.9 or later recommended)
- pip (package installer)
- poetry (Dependency management)

**Installation:**

1. Clone this repository.

```
git clone https://github.com/ashwinam/Magicpitch-Backend-Assessment.git
```

2. Create a virtual environment:

   ```bash
   pip install poetry
   ```

3. Install dependencies:

   ```bash
   poetry shell
   poetry install
   ```

4. Apply database migrations:

   ```bash
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
   ```

5. Create a superuser for initial administrative access:

   ```bash
   python manage.py createsuperuser
   ```

**Running the Project:**

1. Start the development server:

   ```bash
   poetry run python manage.py runserver
   ```

This will start the server on `http://127.0.0.1:8000/` by default.

**API Endpoints:**

**User Registration (POST):**

- Endpoint: `/auth/users/`
- Accepts JSON data with the following fields:
  - `name` (required)
  - `email` (required)
  - `password` (required)
  - `referral_code` (optional)
- Returns a JSON response with user ID and a success message.
- Awards a point to the referrer (if a valid referral code is provided).

**User Details (GET):**

- Endpoint: `/auth/users/me/`
- Requires Authorization header with a valid JWT token.
- Returns a JSON response containing the user's details (name, email, referral code, registration timestamp).

**Referrals (GET):**

- Endpoint: `/referrals/`
- Requires Authorization header with a valid JWT token.
- Returns a paginated list of users who registered using the current user's referral code, including timestamps.

**Api Documentation**

```
http://127.0.0.1:8000/swagger/
```
