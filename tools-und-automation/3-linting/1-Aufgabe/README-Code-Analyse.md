# Code Analyse

Eine Code Analyse wird auf einem Projekt durchgeführt. 

Für die Code Analyse wird ein Token benötigt, welcher auf dem Web-GUI von SonarQube erstellt werden kann. 
1. Öffne die Webseite von SonarQube [http://localhost:9000](http://localhost:9000)

1. Navigiere zu *Administration* - *Security* (oben) - *Users*
1. Klicke beim gewünschten User in der Spalte *Tokens* auf *Update tokens*
1. Es öffnet sich ein Fenster, in welchem ein Token erstellt werden kann. 


SonarScanner muss mit einem File mit dem Namen `sonar-project.properties` konfiguriert werden. Das File wird im Projektverzeichnis gespeichert. 

{{< tabs groupid="sonar" >}}
{{% tab title="sonar-project.properties" %}}
```bash
# must be unique in a given SonarQube instance
sonar.projectKey=house

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0
 
# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.
 
# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8

# Check code coverage
# sonar.python.coverage.reportPaths=coverage.xml
```
{{% /tab %}}
{{< /tabs >}}


Nun kann im Terminal in einem Projektverzeichnis die Code Analyse gestartet werden. Der Docker Container von SonarScanner führt die Analyse durch. 

{{< tabs groupid="terminal" >}}
{{% tab title="Terminal" %}}
```bash
docker run --rm \
    -e SONAR_HOST_URL="http://sonarqube:9000" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
    -e SONAR_TOKEN="your_token" \
    --network sonar-net \
    -v .:/usr/src \
    -u $(id -u):$(id -g) \
    sonarsource/sonar-scanner-cli
```
{{% /tab %}}
{{< /tabs >}}


## Beispiel

Um die Funktionalität der Code Analyse zu demonstrieren, enthält dieses Projekt ein paar bewusste Unschönheiten. 

Datenstruktur: 
```bash
├── Makefile
├── sonar-project.properties
├── src
│   ├── house.py
│   └── main.py
└── tests
    └── test.py
```

{{< tabs groupid="files" >}}
{{% tab title="house.py" %}}
```python
class House:
    def __init__(self):
        print("New house was builded")
    
    def GetName(self):
        print(self.name)

    def SetName(self, name):
        if(type(name) is not str):
            raise Exception

        self.name = name

    def GetPrice(self):
        print(50 + " CHF")
```
{{% /tab %}}

{{% tab title="main.py" %}}

```python
from house import *

villa = House()
# cottage = House()

villa.set_name("Neverland")
villa.get_name()
```
{{% /tab %}}

{{% tab title="test.py" %}}
```python
import unittest
from src.house import *

class TestHouse(unittest.TestCase):
    def test_create(self):
        house = House()

        self.assertIsInstance(house, House)
       

if __name__ == '__main__':
    unittest.main()
```
{{% /tab %}}

{{% tab title="Makefile" %}}
Da SonarQube eine Auswertung über Test Coverage macht, wird das File `coverage.xml` erzeugt. 

```Makefile
.PHONY: linting

linting: coverage.xml
	docker run --rm \
		-e SONAR_HOST_URL="http://sonarqube:9000" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
		-e SONAR_TOKEN="your_token" \
		--network sonar-net \
		-v .:/usr/src \
		-u $(id -u):$(id -g) \
		sonarsource/sonar-scanner-cli

	rm -f coverage.xml

coverage.xml: src/house.py tests/test.py
	python3 -m coverage run -m unittest discover tests
	python3 -m coverage report
	python3 -m coverage xml -i

	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -f .coverage
```
{{% /tab %}}

{{% tab title="sonar-project.properties" %}}
Das File mit den Daten zum Test Coverage wird mit dem Parameter `reportPaths` angegeben. 

```bash
# must be unique in a given SonarQube instance
sonar.projectKey=house

# --- optional properties ---

# defaults to project key
#sonar.projectName=My project
# defaults to 'not provided'
#sonar.projectVersion=1.0
 
# Path is relative to the sonar-project.properties file. Defaults to .
#sonar.sources=.
 
# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8

# Check code coverage
sonar.python.coverage.reportPaths=coverage.xml
```
{{% /tab %}}
{{< /tabs >}}
