"""
Create a class for property

"""


class Property:

    def __init__(self):
        self.locality: str = None
        self.subtype_of_property: str = None
        self.price: int = None
        self.type_of_sale: str = None
        self.number_of_rooms: int = None
        self.Area: int = None
        self.fully_equipped_kitchen: bool = False
        self.furnished: bool = False
        self.open_fire: bool = False
        self.has_terrace: bool = False
        self.has_garden: bool = False
        self.surface_land: int = None
        self.surface_plot_land: int = None
        self.number_of_facades: int = None
        self.has_pool: bool = False
        self.state_building: str = None

    def showPrice(self):
        print(self.price)
        
