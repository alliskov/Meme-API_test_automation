# API-Test-Automation-Python
Prepare test environment:
1. Install allure reports: https://allurereport.org/docs/install/
2. Install requirements: pip install -r requirements.txt

Run tests:
- pytest --alluredir=allure-results
  (use pytest -vs for detailed information)

Run allure server:
- allure serve 

Save allure report:
- allure generate -c allure-results/ -o allure-reports