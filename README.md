# Superhero Challenge API
This is a Flask-based RESTful API that manages data about superheroes, their powers, and their relationships. It supports full CRUD functionality for powers, and relational logic for associating heroes with powers through strength ratings.

# Project Structure

Superhero_challenge/
│
├── app/
│   ├── __init__.py        # initialize app and database
│   ├── models.py          
│   ├── routes.py          # All API endpoints
│
├── instance/
│   └── app.db             
│
├── migrations/            
│
├── run.py                 # for running the app
├── seed.py (optional)     # Optional script to seed sample data
├── challenge-2-superheroes.postman_collection.json
└── README.md              

# Technologies Used
- Flask: Lightweight web framework

- Flask SQLAlchemy: ORM for handling the database

- Flask Migrate: Handles schema migrations

- SQLite: Local database engine

- Postman: API testing and verification

# Setup Instructions
1. Clone the Repository
    git clone <repo_url>
    cd Superhero_challenge

2. Create and Activate Virtual Environment
    python3 -m venv virtual
    source virtual/bin/activate

3. Install Dependencies
    pip install -r requirements.txt

4. Run Migrations
    export FLASK_APP=run.py
    flask db init  
    flask db migrate -m "Initial migration"
    flask db upgrade

5. Run the App
    python run.py

# API Endpoints
✅ GET /heroes
Returns a list of all heroes

Each hero includes: id, name, super_name

✅ GET /heroes/<id>
Returns a single hero and their associated hero powers

If not found, returns { "error": "Hero not found" }

✅ GET /powers
Returns all powers with name and description

✅ GET /powers/<id>
Returns a single power by ID

If not found, returns { "error": "Power not found" }

✅ PATCH /powers/<id>
Updates a power's description

Validates presence of description

Returns updated power or errors

✅ POST /hero_powers
Creates a new HeroPower relation

Accepts: strength, power_id, hero_id

Returns associated hero and power info

Validates strength and foreign key existence

# Testing with Postman
You have been provided a ready-made collection:

Open Postman

Click Import

Upload challenge-2-superheroes.postman_collection.json

Use it to test all endpoints defined above

# Development Notes
Tables must be created using migrations before testing

Seed data (heroes and powers) must be added manually or via script

Use Flask shell or seed file to populate the database for testing


# Author
Yvonne Nyambura

GitHub: (https://github.com/Yvonne-del)