Parky is a platform that lets homeowners/landowners rent out their unused parking spaces to drivers looking for affordable and reliable parking. To list a parking spot on Parky, you must be the property owner, land title holder, or a leaseholder with written permission to sublet your assigned parking space.

activate venv:
source venv/bin/activate
run:
python manage.py runserver

parky/
├── parky/                     # Main Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Project-wide settings
│   ├── urls.py                # Routes to app-level URLs
│   └── wsgi.py
│
├── apps/                      # All Django apps live here
│   ├── general/               # General pages (home, about, static info)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── general/
│   │           └── home.html
│
│   ├── accounts/              # Authentication, profiles, roles (renter/host)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│
│   ├── listings/              # Parking spot listings
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│
│   ├── bookings/              # Booking system (renter -> spot)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│
│   ├── payments/              # Payment system (Stripe, etc.)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│
│   ├── support/               # Help desk, contact, FAQs, safety info
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│
├── static/                    # Static files (CSS, JS, images)
│   └── css/
│       └── styles.css
│
├── templates/                 # Base/global templates (e.g. base.html)
│   └── base.html
│
├── media/                     # Uploaded images, documents, etc.
├── manage.py
└── requirements.txt           # Python dependencies

Conventions:
Signup Details Format:

Host:
host1
h1@parky.ca
h1@h1@h1

Renter
renter1
r1@parky.ca
r1@r1@r1
