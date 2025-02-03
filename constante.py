from PySide6.QtGui import QFontDatabase, QFont

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



CARTE_DICT = {
    "Fighting": "img/card/Fighting.png",
    "Dragon": "img/card/Dragon.png",
    "Psychic": "img/card/Psychic.png",
    "Electric": "img/card/Electric.png",
    "Fire": "img/card/Fire.png",
    "Dark": "img/card/Dark.png",
    "Water": "img/card/Water.png",
    "Grass": "img/card/Grass.png",
    "Normal": "img/card/Normal.png",
    "Steel": "img/card/Steel.png",
    "Poison": "img/card/Dark.png",
    "Ice": "img/card/Water.png",
    "Rock": "img/card/Fighting.png",
    "Ground": "img/card/Fighting.png",
    "Fairy": "img/card/Psychic.png",
    "Flying": "img/card/Normal.png",
    "Bug": "img/card/Grass.png",
    "Ghost": "img/card/Psychic.png",
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

POKEDEX = "pokedex.json"

BOOSTER = "img/booster.png"

GILL_SANS_FONT = QFont("GillSansStdBold", 13, QFont.Bold)
HP_FONT = QFont("GillSansStdBold", 6, QFont.Bold)




