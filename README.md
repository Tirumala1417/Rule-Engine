Step 1: Clone or Download the Project
If you haven’t already, clone the project to your local machine:

bash
Copy code
git clone <project-repo-url>
cd rule_engine_project
Step 2: Create a Virtual Environment (Optional but Recommended)
A virtual environment helps isolate project dependencies.

bash
Copy code
# Create a virtual environment named "venv"
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Step 3: Install Required Packages
Use pip to install all required packages. You can install each dependency individually or set up a requirements.txt file:

Method 1: Install Individually
bash
Copy code
pip install Flask SQLAlchemy requests
Method 2: Use a requirements.txt file
Create a file named requirements.txt in the root directory with the following contents:

plaintext
Copy code
Flask
SQLAlchemy
requests
Then install all dependencies at once:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up the Database
If you’re using SQLite (as per the example), initialize the database by creating the tables.

Create an Initialization Script (if not already in the project):

python
Copy code
# initialize_db.py
from src.database.db_connection import engine
from src.database.models import Base

# Create all tables
Base.metadata.create_all(engine)
Run the Initialization Script:

bash
Copy code
python initialize_db.py
This creates the rules.db SQLite database file with the necessary tables.

Step 5: Run the Application
Run the Flask app from the src directory:

bash
Copy code
cd src
python main.py
The server should now be running at http://127.0.0.1:5000/.
