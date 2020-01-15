# BDD API REST Template Project

BDD Behave API TUI-DX

### Getting Started
In this project I make a template with the behave framework (BDD) to manage the tests cases, and use the mashmallow library to validate the responses

We query two public endpoints hosted at: https://jsonplaceholder.typicode.com/todos
The template uses a Behave Scenario for the Get operation and a Scenario Outline for the GetId operation

Behave it's a BDD framework based on Gherkins Language, the advantage to BDD test cases being written in a common language is that details of how the application behaves can be easily understood by all

The ‘Given-When-Then’ formula for writing BDD test cases for a user story, which can be defined as:

* Given a certain scenario
* When an action takes place
* Then this should be the outcome.

The test cycle start with the creation of the feature file in Gherkins natural language, ideally by a stakeholder or a PO profile

Then the QA engineer work in the Step definition methods, that are known as "glue code"; this is because they "glue" the step definition phrases to the code that actually does the work.
Behave its the python-bdd framework use to translate from natural language to python code

* Feature File -> Step File -> Model(POO) File -> Validate Response (marshmallow library)

### Prerequisites

install last python 3.x release: 
```
https://www.python.org/downloads/release/
```

install python dependencies:
```
pip install -r requirements.txt
```


### How To Use
```
* In the features files we define the test cases in natural language (Gherkins)
* In the step file we define the "glue" code to transform natural language to python code
* In the model file we define the behaviour of the service:
    ** urls
    ** HTTP operation Verb
    ** Headers, Body
    ** Response validate function
* In the response model file we define format and structure of the response
```

    
### Structure
```
project root
    features/
        service/
            template.feature
            steps/
                service.steps.py
            model/
                service_response_model.py
                service.py
    helpers/
        utils.py
    libs/
        micro_services/
            base_micro_service.py
    logs/
    
```

### Running the tests from root folder

```
behave features/template/<feature_file>.feature
```

### Allure reports
```
Install allure commandline
behave -f allure_behave.formatter:AllureFormatter -o reports
```
To generate the report:
```
allure serve reports
```

### Authors

* Miguel Angel Aragon



### Resources

* https://behave.readthedocs.io/en/latest/
* https://marshmallow.readthedocs.io/en/stable/
* https://docs.qameta.io/allure/

