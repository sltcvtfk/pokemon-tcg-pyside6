from PySide6.QtGui import QFont

GENERATION = [(1,151), (152,251), (252,386), (387,493), (494,649), (650,721), (722,809)]

TYPE_DICT = {
    "Grass": "Grass",
    "Fire": "Fire",
    "Water": "Water",
    "Electric": "Electric",
    "Fighting": "Fighting",
    "Psychic": "Psychic",
    "Dark": "Dark",
    "Steel": "Steel",
    "Dragon": "Dragon",
    "Normal": "Normal",
    "Poison": "Dark",
    "Ice": "Water",
    "Rock": "Fighting",
    "Ground": "Fighting",
    "Fairy": "Psychic",
    "Flying": "Normal",
    "Bug": "Grass",
    "Ghost": "Psychic",
}

FRENCH_TYPE_TO_ENGLISH_DICT = { 
    "eau" : "water",
    "feu" : "fire",
    "plante" : "grass",
    "combat" : "fighting",
    "normal" : "normal",
    "glace" : "ice",
    "insecte" : "bug",
    "poison" : "poison",
    "dragon" : "dragon",
    "acier" : "steel",
    "psy" : "psychic",
    "sol" : "ground",
    "ténèbres" : "dark",
    "roche" : "rock",
    "spectre" : "ghost",
    "fée" : "fairy",
    "vol" : "flying",
    "électrik" : "electric"
}

STAGE1_CARD_DICT = {
    "Fighting": "img/card/stage1/Fighting.png",
    "Dragon": "img/card/stage1/Dragon.png",
    "Psychic": "img/card/stage1/Psychic.png",
    "Electric": "img/card/stage1/Electric.png",
    "Fire": "img/card/stage1/Fire.png",
    "Dark": "img/card/stage1/Dark.png",
    "Water": "img/card/stage1/Water.png",
    "Grass": "img/card/stage1/Grass.png",
    "Normal": "img/card/stage1/Normal.png",
    "Steel": "img/card/stage1/Steel.png",
    "Poison": "img/card/stage1/Dark.png",
    "Ice": "img/card/stage1/Water.png",
    "Rock": "img/card/stage1/Fighting.png",
    "Ground": "img/card/stage1/Fighting.png",
    "Fairy": "img/card/stage1/Psychic.png",
    "Flying": "img/card/stage1/Normal.png",
    "Bug": "img/card/stage1/Grass.png",
    "Ghost": "img/card/stage1/Psychic.png",
}

STAGE2_CARD_DICT = {
    "Fighting": "img/card/stage2/Fighting.png",
    "Dragon": "img/card/stage2/Dragon.png",
    "Psychic": "img/card/stage2/Psychic.png",
    "Electric": "img/card/stage2/Electric.png",
    "Fire": "img/card/stage2/Fire.png",
    "Dark": "img/card/stage2/Dark.png",
    "Water": "img/card/stage2/Water.png",
    "Grass": "img/card/stage2/Grass.png",
    "Normal": "img/card/stage2/Normal.png",
    "Steel": "img/card/stage2/Steel.png",
    "Poison": "img/card/stage2/Dark.png",
    "Ice": "img/card/stage2/Water.png",
    "Rock": "img/card/stage2/Fighting.png",
    "Ground": "img/card/stage2/Fighting.png",
    "Fairy": "img/card/stage2/Psychic.png",
    "Flying": "img/card/stage2/Normal.png",
    "Bug": "img/card/stage2/Grass.png",
    "Ghost": "img/card/stage2/Psychic.png",
}



BASIC_CARD_DICT = {
    "Fighting": "img/card/basic/Fighting.png",
    "Dragon": "img/card/basic/Dragon.png",
    "Psychic": "img/card/basic/Psychic.png",
    "Electric": "img/card/basic/Electric.png",
    "Fire": "img/card/basic/Fire.png",
    "Dark": "img/card/basic/Dark.png",
    "Water": "img/card/basic/Water.png",
    "Grass": "img/card/basic/Grass.png",
    "Normal": "img/card/basic/Normal.png",
    "Steel": "img/card/basic/Steel.png",
    "Poison": "img/card/basic/Dark.png",
    "Ice": "img/card/basic/Water.png",
    "Rock": "img/card/basic/Fighting.png",
    "Ground": "img/card/basic/Fighting.png",
    "Fairy": "img/card/basic/Psychic.png",
    "Flying": "img/card/basic/Normal.png",
    "Bug": "img/card/basic/Grass.png",
    "Ghost": "img/card/basic/Psychic.png",
}

WEAKNESS_TYPE_DICT = {
    "Grass": "Fire",
    "Fire": "Water",
    "Water": "Electric",
    "Electric": "Fighting",
    "Fighting": "Psychic",
    "Psychic": "Dark",
    "Dark": "Fighting",
    "Steel": "Fire",
    "Dragon": "Dragon",
    "Normal": "Fighting"
}

WEAKNESS_IMAGE_DICT = {
    "Grass": "img/type/Fire.png",
    "Fire": "img/type/Water.png",
    "Water": "img/type/Electric.png",
    "Electric": "img/type/Fighting.png",
    "Fighting": "img/type/Psychic.png",
    "Psychic": "img/type/Dark.png",
    "Dark": "img/type/Fighting.png",
    "Steel": "img/type/Fire.png",
    "Dragon": "img/type/Dragon.png",
    "Normal": "img/type/Fighting.png"
}

ATTACK_DICT = {
    "Grass": "Vine Whip",
    "Fire": "Ember",
    "Water": "Water Gun",
    "Electric": "Thunder Shock",
    "Fighting": "Karate Chop",
    "Psychic": "Confusion",
    "Dark": "Bite",
    "Steel": "Iron Tail",
    "Dragon": "Dragon Breath",
    "Normal": "Tackle"
}

FIRST_POKEMON = 1
LAST_POKEMON = 809

POKEDEX = "json/pokedex.json"
BDD = "json/bdd.json"

BOOSTER = "img/booster.png"

GILL_SANS_FONT = QFont("GillSansStdBold", 13, QFont.Bold)
HP_FONT = QFont("GillSansStdBold", 6, QFont.Bold)
EVOLUTION_FONT = QFont("GillSansStdBold", 5)