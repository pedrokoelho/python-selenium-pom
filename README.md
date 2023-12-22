## CREATE A VIRTUAL ENV

`python -m venv selenium-python-2`

### Activate the virtual env in bash

`. selenium-python-2/Scripts/activate`

### Deactivate the virtual env in bash

`deactivate`


> https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/


## Install a Selenium library

`pip install selenium`


### 1. Start the session

`driver = webdriver.Chrome()`

### 2. Import the webdriver from Selenium

`from selenium import webdriver`

### 3. Navigate to page

`driver.get('url')`