from assets.constante import *
import json

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    
class Pokemon(): 
    def __init__(self, pokedex_id: int):
        """

        Args:
            pokedex_id (int): Pokedex ID of the pokemon
        """
        self.pokedex_id = pokedex_id
        
    def height(self):
        """
            Returns:
                int: Height of the pokemon
        """
        return res[self.pokedex_id-1]["profile"]["height"]
    
    def weight(self):
        """
            Returns:
                int: Weight of the pokemon
        """
        
        return res[self.pokedex_id-1]["profile"]["weight"]
        
    def species(self):
        """
            Returns:
                str: Species of the pokemon
        """
        return res[self.pokedex_id-1]["species"]
    
    def english_name(self):
        """
            Returns:
                str: English name of the pokemon
        """
        return res[self.pokedex_id-1]["name"]["english"]

    def french_name(self):
        """
            Returns:
                str: French name of the pokemon
        """
        return res[self.pokedex_id-1]["name"]["french"]
    
    def hp(self):
        """
        Returns:
            int: HP of the pokemon
        """
        return res[self.pokedex_id-1]["base"]["HP"]
    
    def description(self): 
        """
            Returns:
                str: Description of the pokemon
        """
        return res[self.pokedex_id-1]["description"]
    
    def his_type(self):
        """
            Returns:
                str: Type of the pokemon
        """
        return TYPE_DICT[res[self.pokedex_id-1]["type"][0]]
    
    def weakness(self):
        """
        Returns:
            str: Weakness of the pokemon
        """
        return WEAKNESS_TYPE_DICT[TYPE_DICT[res[self.pokedex_id-1]["type"][0]]]
    
    def generation(self):
        """
            Returns:
                int: Generation of the pokemon
        """
        for i, (start, end) in enumerate(GENERATION):
            if self.pokedex_id >= start and self.pokedex_id <= end:
                return i+1     
    
    def has_prev_evolution(self):
        """ 
            Returns: 
                bool: True if the pokemon has a previous evolution
        """
        if len(res[self.pokedex_id-1]["evolution"]) != 0:
            if "prev" in res[self.pokedex_id-1]["evolution"]:
                return True
        return False
    
    def prev_evolution(self):
        """
            Returns:
                int: Pokedex ID of the previous evolution
        """
        return int(res[self.pokedex_id-1]["evolution"]["prev"][0])
        
    def prev_evo_has_prev_evo(self):
        """ 
            Returns: 
                bool: True if the previous evolution has a previous evolution
        """
        prev = self.prev_evolution()
        if "prev" in res[prev-1]["evolution"]:
            return True
        return False
        
    def __repr__(self):
        return f"{self.english_name()} ({self.french_name()})\nPV: {self.hp()}\nType: {self.his_type()}\nWeakness: {self.weakness()}\nGeneration: {self.generation()}"
