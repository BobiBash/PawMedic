# PawMedic

A Django-based platform connecting pet owners with veterinarians. Pet owners can manage their pets, browse vet profiles, and book appointments. Vets can manage their schedules and publish their profiles. Background tasks handle email notifications and slot cleanup via Celery.

Built as a final project for the SoftUni Django Advanced course.

---

## Features

**For pet owners**
- Register and verify account via email confirmation
- Log in with username or email
- Create, edit, and delete pets
- Browse and favourite published vet profiles
- Book appointments from available time slots
- Participate in the community forum

**For vets**
- Extended vet profile with photo, bio, and publish/unpublish toggle
- Manage available appointment slots
- Forum participation and tag management (via vet group permissions)

**Platform**
- Custom user model with owner and vet roles, group-assigned on registration
- Signal-driven Celery email notification on appointment creation
- Daily Celery Beat task to clean up expired appointment slots
- DRF-powered vet search endpoint
- Cloudinary media storage
- Tailwind CSS styling

---

## Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3.12+ |
| Framework | Django 6.0.3 |
| Database | PostgreSQL |
| Task queue | Celery + Redis |
| API | Django REST Framework |
| Media storage | Cloudinary |
| Styling | Tailwind CSS |

---

## Project layout

```
Softuni-Django-advanced-project/
├── PawMedic/           # Settings, root URLs, Celery bootstrap
├── accounts/           # Users, vet profiles, auth, groups, password reset
├── appointments/       # Scheduling, booking, cleanup task
├── common/             # Home, about, issue reporting
├── forum/              # Posts, comments, tags
├── notifications/      # Signal-driven email tasks
├── pets/               # Pet CRUD
├── vets/               # Vet directory and search API
├── templates/          # Global templates
├── static/             # Compiled frontend assets
├── assets/             # Tailwind source
├── media/              # Local media (development only)
├── populate_db.py      # Seed script
├── requirements.txt
└── manage.py
```

---

## Quick start

### 1. Clone and set up a virtual environment

```bash
git clone <repo-url>
cd Softuni-Django-advanced-project

# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

```env
SECRET_KEY=your_django_secret_key

DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_PORT=5432

REDIS_URL=redis://localhost:6379/0

EMAIL_HOST_USER=your_gmail_address
EMAIL_HOST_PASSWORD=your_gmail_app_password

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Create the database

```sql
CREATE DATABASE pawmedic_db;
```

### 5. Apply migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

App is available at `http://127.0.0.1:8000/`.

---

## Background services

Redis must be running before starting the Celery worker or beat scheduler.

**Start the worker:**
```bash
celery -A PawMedic worker --loglevel=info
```

**Start the beat scheduler** (runs the daily slot cleanup):
```bash
celery -A PawMedic beat --loglevel=info
```

---

## Seed data

To populate the database with sample records:

```bash
python populate_db.py
```

---

## API

### Vet search

```
GET /vets/api/vets/?search=<term>
```

Returns published vets matching the search term. Requires a non-empty `search` parameter. Results are paginated (page size 5).

**Example response:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "slug": "john-smith",
      "vet_id": 3,
      "first_name": "John",
      "last_name": "Smith"
    }
  ]
}
```

---

## Roles and permissions

Two groups are created automatically after migration: `Vets` and `Pet Owners`. Users are assigned to a group on registration based on their role field.

| Permission | Pet Owners | Vets |
|---|---|---|
| Pet CRUD | ✓ | view only |
| Appointment booking | ✓ | |
| Appointment slot management | | ✓ |
| Vet profile management | | ✓ |
| Forum CRUD | ✓ | ✓ |
| Forum tag management | | ✓ |
| Issue report review | superuser / manual grant | superuser / manual grant |

---

## Data model overview

| Model | Description |
|---|---|
| `PawMedicUser` | Custom auth user with unique email, phone, and role |
| `VetProfile` | One-to-one extension of a vet user |
| `FavoriteVet` | Owner-to-vet favourite relationship |
| `Pet` | Pet owned by a user |
| `AppointmentSlot` | Available schedule slot attached to a vet profile |
| `Appointment` | Booking linking a slot, user, and pet |
| `ForumPost`, `Comment`, `Tag` | Forum models |
| `ReportedIssues` | User-submitted platform issue reports |
| `EmailConfirmation` | Registration confirmation token |

---

## Testing

The test suite requires a running local PostgreSQL instance.

```bash
python manage.py test
```

The project currently has 24 discovered tests across the app modules. Note: `test.py` in the project root is a scratch file and is not part of the test suite.

---

## Routes

| Path | Description |
|---|---|
| `/` | Home page |
| `/about/` | About page |
| `/accounts/` | Registration, login, profile, password reset, favourites |
| `/pets/` | Pet CRUD |
| `/vets/` | Vet directory, detail pages, search, API |
| `/appointments/` | Appointments and vet schedule management |
| `/forum/` | Posts, comments, tags |

---

## License

Developed as part of the SoftUni Django Advanced course.