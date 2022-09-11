Dependencies needed:
- flask
- flask_sqlalchemy
- flask_marshmallow


Recommended folder structure:
- Project
    - Routes (the various routes are stored; relevant functions from ApiFunctions are imported)
        - <api_name>Routes.py
    - ApiFunctions (functions called in the various routes; data model of relevant entity is imported)
        - <api_name>Functions.py
    - Models (Entity models are found here; the db and marshmellow instances are imported)
        - <model_name>.py
    - Tests (This is where you test the individual APIs)
        - <api_name>Test.py
    - main.py (main code where you import the content from api folder)
    - .gitignore
    - config.py (all the setup will happen there; SQLAlchemy and App initialisation)
    - main.py (where you actually run the code; you import the routes from the Routes folder)

To run the main API, type the following in your terminal:
- python main.py

To run the test cases, type the following in your terminal:
- cd Tests (to go to the path of the Tests folder)
- python <api_name>Test.py (to test the specific API; based on its name)

