## Activate the virtual env in bash

`. selenium-python-2/Scripts/activate`

## Install Pytest

`pip install -U pytest`

## Check Pytest Version

`pytest --version`

1. create tests folder
2. create test_TC0_login_valid.py
3. create TestLoginValid class
4. create test_TC0_login_valid method

## Run tests

`pytest`

5. mark the test

> @pytest.mark.smoke
> @pytest.mark.login

## Select the tests -> Run only the tests with marker

`pytest -m smoke`
`pytest -m login`


## Print the captured data on tests with marker

`pytest -s -m smoke`
`pytest -s -m login`


## Register the marks

> create pytest.ini
> [pytest]
> markers =
>    smoke: smoke tests
>    login: login tests


## Install pytest-html 

`pip install pytest-html`

> Create a new folder - reports

## Run tests with specific marker and generate the html report 

> --html=path
> --html=folder/file_name.html

`pytest -m invalid --html=reports/report.html`

## Create conftest file in tests folder

> move the fixture to conftest so all the modules can use it

> add the fixture - driver - to the methods parameters
> def test_TC0_login_valid(self, driver)
> def test_TC01_1_username_invalid(self, driver)
> def test_TC01_2_password_invalid(self,driver)

## Install pytest-xdist to run tests in parallel

`pip install pytest-xdist`

> run the tests -> n=number_of_tests_to_run_in_parallel
`pytest -n=2`

> run the 5 exceptions tests in parallel
`pyest -m exceptions -n=5`