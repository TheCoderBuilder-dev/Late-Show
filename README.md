# Late Show API

Welcome to the **Late Show** API – a backend system built with Flask that manages TV show episodes, guest appearances, and ratings. Powered by Flask, SQLAlchemy, and REST principles.

---

## Project Structure

```

lateshow-brian-mwirigi/
├── app/
│   ├── **init**.py
│   ├── models.py
│   └── routes.py
├── instance/
│   └── app.db
├── migrations/
├── guests.csv
├── requirements.txt
├── run.py
├── seed.py
├── challenge-4-lateshow\.postman\_collection.json
└── README.md

````

---

## Tech Stack

- **Python 3.12+**
- **Flask**
- **Flask SQLAlchemy**
- **Flask Migrate**
- **SQLite** (as the database)
- **Postman** (for testing endpoints)

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/lateshow-brian-mwirigi.git
cd lateshow-brian-mwirigi
````

### 2. Create Virtual Environment

```bash
pipenv install
pipenv shell
```

### 3. Run Migrations

```bash
flask db init
flask db migrate -m "Initial"
flask db upgrade
```

### 4. Seed the Database

```bash
python seed.py
```

### 5. Start the Server

```bash
python run.py
```

Server runs at:
`http://localhost:5555`

---

## 🔌 API Endpoints

### `GET /episodes`

Returns all episodes.

### `GET /episodes/<id>`

Returns episode details including guest appearances.

### `GET /guests`

Returns all guests.

### `POST /appearances`

Creates a new appearance entry with `rating`, `episode_id`, and `guest_id`.

---

## Validations

* `rating` must be between `1` and `5` (inclusive).
* `episode_id` and `guest_id` must refer to existing records.
* Appearances can't be created for missing guests or episodes.

---

## Testing with Postman

Import the file:
`challenge-4-lateshow.postman_collection.json`

Then test:

* `GET /episodes`
* `GET /guests`
* `GET /episodes/<id>`
* `POST /appearances`

---

## Author

**Brian Mwirigi**
Phase 4 Student @ Moringa School
GitHub: [@TheCoderBuilder-dev](https://github.com/TheCoderBuilder-dev)

