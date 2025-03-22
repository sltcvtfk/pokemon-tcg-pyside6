# Pokemon TCG

## Description

Ce projet est une application graphique basée sur PySide6 permettant de simuler l'ouverture de boosters de cartes Pokémon et d'afficher un Pokédex interactif.

## Fonctionnalités

- **Affichage du Pokédex** : Recherche de Pokémon par nom, type, génération ou ID.
- **Ouverture de boosters** : Simulation de l'ouverture d'un booster contenant plusieurs cartes Pokémon.
- **Interface utilisateur** : Navigation fluide entre les différentes scènes via une barre d'outils.

## Installation

### Prérequis

- Python 3.8+
- PySide6
- Requests
- JSON (intégré à Python)

### Étapes d'installation

1. Clonez ce dépôt :
   ```sh
   git clone https://github.com/sltcvtfk/pokemon-tcg-pyside6git
   cd pokemon-tcg-pyside6
   ```
2. Installez les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

## Utilisation

Lancez l'application avec la commande :

```sh
python main.py
```

## Architecture du Projet

![image](https://github.com/user-attachments/assets/9a849f30-9be5-4d4e-b2b4-4ac4045b001b)

```
📂 pokemon-tcg       
│── 📂 assets              # Dossier des autres fichiers Python
│── 📂 font                # Police d'écriture
│── 📂 img                 # Icônes et images
│── 📂 json                # Fichiers JSON (Pokedex...)
│── 📂 UML                 # Diagrammes de classe
│── 📜 .gitignore          # Fichier ignoré lors des commits
│── 📜 LICENSE             # Fichier de la LICENSE utilisé
│── 📜 README.md           # Documentation       
│── 📜 main.py             # Fichier Python principal
│── 📜 requirements.txt    # Dépendances obligatoires           
```




## Technologies utilisées

- **Python** (PySide6, JSON, Requests)
- **PlantUML** (Diagrammes UML pour la conception)
- **GitHub** (Partage du projet)

## Informations supplémentaires

- **pokemon.json** Correction d'un problème avec le nom de certains pokémons
   - [Problème 1 (Pull Request Merged)](https://github.com/Purukitto/pokemon-data.json/pull/27/files)
   - [Problème 2 (Pull Request Open)](https://github.com/Purukitto/pokemon-data.json/pull/28/files)

## Auteurs et avancée du projet
![image](https://github.com/user-attachments/assets/22a21f22-6e72-403d-bcb1-084e4c5cc2d3)

-<span style="color:red">
**STAN SALOMON** 
</span> || [**@sltcvtfk**](https://github.com/sltcvtfk)

**Tâches** :  Je me suis occupé surtout de la partie graphique, avec la MainWindow, la scène Booster, avec l'affichage des cartes, avec le nom du pokémon, son type, ses "HP", sa taille, son poids, sa faiblesse, et sa sous évolution, s'il en avait une. et "Pokédex". J'ai aussi fait la Toolbar. J'ai aussi fait la partie back-end, avec l'ajout des pokémons dans le pokédex de l'utilisateur à chaque ouverte de booster.

-<span style="color:orange">
**EVAN CHAMAND**
</span> || [**@EvanLeGoat**](https://github.com/EvanLeGoat) 

**Tâches** : Je me suis occupé de la documention(Plant_UML, Gantt_UML, README.md, etc ...), j'ai fait un peu de code aussi en rapport avec la base de données pour la liaison au mais celà n'a pas été utilisé <span style="color:orange">
**Main**
</span>.

-<span style="color:green">
**ROMAIN ARDOISE** 
</span> || [**@ShizuutA**](https://github.com/ShizuutA)

**Tâches** : Je me suis occupé de la barre de recherche, de la connexion et du mode admin, de la modification de pokemon présent dans le pokedex en mode admin

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
