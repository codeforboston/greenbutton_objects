CONFIG := $(abspath .xsdata.xml)


black:
	black --check .

isort:
	isort --check .

pydocstyle:
	pydocstyle .

lint: black isort pydocstyle

mypy:
	mypy src

gen_classes:
	cd src && xsdata generate -c $(CONFIG) -p greenbutton_objects.data.espi https://www.naesb.org/espi.xsd
	cd src && xsdata generate -c $(CONFIG) -p greenbutton_objects.data.atom https://greenbuttondata.org/xsd/3_3/atom.xsd

gen_examples:
	python .\tests\test_rules_engine\generate_example_data.py

test:
	pytest .

build:
	pip install -q build
	python -m build

all: lint mypy gen_examples test build
