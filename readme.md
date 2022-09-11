Dependencies needed:
- flask
- flask_sqlalchemy
- flask_marshmallow


Recommended folder structure:
- Project
    - ApiFunctions
        - <api_name>Functions.py
    - Models
        -<model_name>.py
    - main.py (main code where you import the content from api folder)
    - Tests
        - <api_name>Test.py
    - .gitignore
    - config.py (all the setup will happen there; SQLAlchemy and App
    - main.py (where you actually run the code)


