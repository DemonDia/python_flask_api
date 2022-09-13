# Flask Test 

### Folder structure

```bash 
Project
├── Routes (the various routes are stored; relevant functions from ApiFunctions are imported)
|   ├── <api_name>Routes.py
|
├── ApiFunctions (functions called in the various routes; data model of relevant entity is imported)
|   ├── <api_name>Functions.py
|
├── Models (Entity models are found here; the db and marshmellow instances are imported)
|   ├── <model_name>.py
|
├── Tests (This is where you test the individual APIs)
|   ├── <api_name>Test.py
|
├── main.py (main code where you import the content from api folder)
|
├── .gitignore (this lists the type of files that will NOT be tracked by GitHub)
|
├── config.py (all the setup will happen there; SQLAlchemy and App initialisation)
|
├── main.py (where you actually run the code; you import the routes from the Routes folder)
|
├── requirments.txt (this lists the dependencies required to run the project)
```

**NOTE: the naming convention of <model_name> and <api_name> should be consistent.**

Eg: If your model name is 'Entity', your naming convention should be like:
- Routes: EntityRoutes.py
- ApiFunctions: EntityFunctions.py
- Models: Entity.py
- Tests: EntityTest.py


### Setup (for testing):
1. Clone this repo
2. Open the project in VSC 
3. In your terminal, Type this in CLI: 
```
pip install -r requirements.txt
```

NOTE: this downloads the dependencies stated in the requirements.txt

### Running the project (for testing):
To run the main API, type the following in your terminal:
```
cd Tests
python main.py
```

To run the test cases, type the following in your terminal:
```
cd Tests
python <api_name>Test.py
```
Note: 
- cd Tests: you go to the path of the Tests folder
- python <api_name>Test.py: you run the test script of a given entity (api_name), depending on what you want to test

__NOTE: before you run your test file inside the 'Tests' folder, ensure your main.py is running__

