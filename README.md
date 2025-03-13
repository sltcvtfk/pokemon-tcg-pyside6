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
   git clone https://github.com/votre-utilisateur/pokemon-tcg.git
   cd pokemon-tcg
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

```
📂 pokemon-tcg
│── 📂 .vscode             
│── 📂 assets              
│── 📂 font                
│── 📂 img                 # Icônes et images
│── 📂 json                # Fichiers JSON (Pokedex...)
│── 📂 UML
│── 📜 .gitignore          
│── 📜 LICENSE         
│── 📜 README.md           # Documentation       
│── 📜 main.py        
│── 📜 requirements.txt            
```

## Technologies utilisées

- **Python** (PySide6, JSON, Requests)
- **PlantUML** (Diagrammes UML pour la conception)

## Auteurs

- **Votre Nom** (@votre-github)

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

