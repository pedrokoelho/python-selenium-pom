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