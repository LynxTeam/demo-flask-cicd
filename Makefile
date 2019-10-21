build:prepare run

#Une cible "prepare" qui fasse l'installation des dépendances du projet
prepare:
	pipenv install

#Une cible "test" qui test la quelité du projet
test:
	pipenv run pylint hf.py
