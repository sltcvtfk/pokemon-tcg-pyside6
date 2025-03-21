from assets.constante import *
import json

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    
class Pokemon(): 
    def __init__(self, pokedex_id: int):
        """

        Args:
            pokedex_id (int): L'ID du Pokémon dans le Pokédex
        """
        self.pokedex_id = int(pokedex_id)
        
    def height(self):
        """
            Returns:
                int: Taille du pokemon
        """
        return res[self.pokedex_id-1]["profile"]["height"]
    
    def weight(self):
        """
            Returns:
                int: Poids du pokemon
        """
        
        return res[self.pokedex_id-1]["profile"]["weight"]
        
    def species(self):
        """
            Returns:
                str: L'espèce du pokemon (en anglais)
        """
        return res[self.pokedex_id-1]["species"]
    
    def english_name(self):
        """
            Returns:
                str: Le nom anglais du pokemon
        """
        return res[self.pokedex_id-1]["name"]["english"]

    def french_name(self):
        """
            Returns:
                str: Le nom français du pokemon
        """
        return res[self.pokedex_id-1]["name"]["french"]
    
    def hp(self):
        """
        Returns:
            int: Points de vie du pokemon
        """
        return res[self.pokedex_id-1]["base"]["HP"]
    
    def description(self): 
        """
            Returns:
                str: Description du pokemon (en anglais)
        """
        return res[self.pokedex_id-1]["description"]
    
    def his_type(self):
        """
            Returns:
                str: Type du pokemon
        """
        return TYPE_DICT[res[self.pokedex_id-1]["type"][0]]
    
    def weakness(self):
        """
        Returns:
            str: Type de faiblesse du pokemon
        """
        return WEAKNESS_TYPE_DICT[TYPE_DICT[res[self.pokedex_id-1]["type"][0]]]
    
    def generation(self):
        """
            Returns:
                int: Génération du pokemon
        """
        for i, (start, end) in enumerate(GENERATION):
            if self.pokedex_id >= start and self.pokedex_id <= end:
                return i+1     
    
    def evolution(self):
        """
            Returns:
                int: L'ID du pokemon suivant dans l'évolution
        """
        if len(res[self.pokedex_id-1]["evolution"]) != 0:
            if "next" in res[self.pokedex_id-1]["evolution"]:
                return res[self.pokedex_id-1]["evolution"]["next"][0][0]
            else:
                return None
        else:
            return None
    
    def pre_evolution(self):
        """
            Returns:
                int: L'ID du pokemon précédent dans l'évolution
        """
        if len(res[self.pokedex_id-1]["evolution"]) != 0:
            if "prev" in res[self.pokedex_id-1]["evolution"]:
                return res[self.pokedex_id-1]["evolution"]["prev"][0]
            else:
                return None
        else:
            return None
        
    def pre_pre_evo(self):
        """ 
            Returns: 
                int: L'ID du pokemon précédent dans l'évolution de l'évolution
        """
        prev = int(self.pre_evolution())-1
        if "prev" in res[prev]["evolution"]:
            return res[prev]["evolution"]["prev"][0]
        else:
            return None
    
    def image_links(self):
        """
            Returns:
                Dict: Lien vers les images du pokemon
        """
        return {
            "sprite": res[self.pokedex_id-1]["image"]["sprite"],
            "hires": res[self.pokedex_id-1]["image"]["hires"],
            "thumbnail": res[self.pokedex_id-1]["image"]["thumbnail"]
        }
        
    def __repr__(self):
        return f"{self.english_name()} ({self.french_name()})\nPV: {self.hp()}\nType: {self.his_type()}\nWeakness: {self.weakness()}\nGeneration: {self.generation()}"
