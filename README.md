PRO-NUMERIC-360 – Calculatrice Python
Ce dépôt contient le projet de calculatrice développé en Python par notre équipe.

Membres
Mariam : Interface graphique

Yohane : Interface Graphique (travail en cohorte avec Mariam)
Lenox : Opérations de base (+, -, ×, ÷, =, C)

Souaré : Opérations de base (travail en cohorte avec Lenox)

Aïcha : Opérations avancées (puissance, racine carrée, pourcentage...etc)

Yohane : Coordination, tests et packaging

Objectif
Créer une calculatrice fonctionnelle avec une interface graphique et la partager sous forme d’exécutable.

Utilisation
Avec Python installé : exécutez calculatrice.py (nécessite Tkinter, inclus par défaut).

Sans Python : téléchargez l’exécutable depuis la section Releases de ce dépôt.

Organisation du dépôt
main : version finale du projet.

Branches temporaires : feature/interface, feature/calculs-base, feature/calculs-avances (supprimées après fusion).

Issues : utilisées pour suivre les tâches.

Comment contribuer (pour les membres de l’équipe)
Créez une branche à partir de main.

Codez dans calculatrice.py.

Commitez vos modifications.

Le superviseur crée une pull request et fusionne.

Technologies
Python 3

Tkinter (inclus par défaut)

PyInstaller (pour l’exécutable)

Pytest (pour les tests unitaires)

Numpy (optionnel pour calculs avancés)

Fichier requirements.txt
Code
# Dépendances nécessaires pour PRO-NUMERIC-360

pyinstaller==6.3.0   # Génération d'exécutable
pytest==8.0.0        # Tests unitaires
numpy==1.26.0        # Calculs avancés (optionnel)
Projet réalisé dans le cadre d’un exercice collaboratif.
