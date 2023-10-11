from S1E9 import Character

class Family(Character):
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)

    def die(self):
         self.is_alive = False

    def __str__(self):
        # return self.__dict__
        return self.__repr__()
    
    def __repr__(self):
        # return f"Baratheon({self.first_name, self.is_alive})"
        return f"Vector: {tuple(self.__dict__.values())}" 

class Baratheon(Family):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

    def die(self):
        self.is_alive = False

class Lannister(Family):
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = self.__class__.__name__
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

    def die(self):
        super().die()

    @classmethod
    def create_lannister(cls, first_name, is_alive = True):
        return cls(first_name, is_alive)