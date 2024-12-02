class Drink:
    """A class for drink:
    That stores a 'base' 
    And the 'flavors' that haver been added"""

    _valid_bases = {"water", "sbrite", "pokecola", "Mr. Salt", "hill fog", "leaf wine"} 
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}     

    # Needed a size and cost for each drink
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15,
    }

    # Initializer for GETTERS:
    def __init__(self, size):       # added size
        self._base = None
        self._flavors = set()   # -> 'set()' helps avoid duplicates for flavors
        self.size = None            # set the size and cost to 0
        self._cost = 0.0 
        self.set_size(size)         # sets the cost to the appropriate size

    # GETTERS to grab the different aspects for the drink:
    def get_base(self):
        return self._base
    
    # returns a 'list' for usr access
    def get_flavors(self):
        return list(self._flavors) 
    
    # Keeps a tracker for number of flavors added 
    def get_num_flavors(self):      
        return len(self._flavors)
    
    # Get the total
    def get_total(self):
        return self._cost
    
    # Get the size
    def get_size(self):
        return self.size
    
    # set the base:
    def set_base(self, base):
        if base in self._valid_bases: # Validates the base
            self._base = base
        else:
            raise ValueError(f"Invalid base: {base}. Choose a different base from {self._valid_bases}.")
        
    def add_flavor(self, flavor):       
        if flavor in self._valid_flavors:
            if flavor not in self._flavors: # Only charges for 1 instance of the same flavor 
                self._cost += 0.15
            self._flavors.add(flavor)       # Checks for a valid flavor, then adds to list (helps with duplication)
        else: 
            raise ValueError(f"Invalid flavor: {flavor}. Choose a different flavor from {self._valid_flavors}.")

    # set the falvors:    
    def set_flavors(self, flavors):
        if all(flavor in self._valid_flavors for flavor in flavors):
            new_flavors = set(flavors) - self._flavors
            self._cost += 0.15 * len(new_flavors)   # adds additional cost for flavors not already added 
            self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in self._valid_flavors]
            raise ValueError(f"Invalid flavors: {invalid_flavors}. Choose a different flavor from {self._valid_flavors}.")

    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self.size = size # Assign the size 
            # Calculate the total cost with size base cost + flavor costs
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size}. Choose a different size from {list(self._size_costs.keys())}.")


class Order: 
    """class to contain our order items"""

    # tax rate
    _tax_rate = 0.0725

    # Initialize the class
    def __init__(self):
        self._items = []    # Create a list as a starting point 

    # GETTERS for the items and total of items
    def get_items(self):
        return self._items
    
    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(drink.get_total() for drink in self._items)

    def get_tax(self):
        return self.get_total() * (1 + self._tax_rate)
    
    # Receipt Data
    def get_receipt(self):
        receipt_data = {
            "number_drinks": self.get_num_items(),
            "drinks": [],
            "subtotal": self.get_total(),
            "tax": self.get_total() * self._tax_rate,
            "grand_total": self.get_tax()
        }
        # compares the list and counts the number of items ordered
        for i, drink in enumerate(self._items):     
            drink_data = {
                "Number_drinks": i + 1,
                "base": drink.get_base(),
                "size": drink.get_size(),
                "flavors": drink.get_flavors(),
                "total_cost": drink.get_total()
            }
            receipt_data["drinks"].append(drink_data)
        #    base = drink.get_base()
        #    flavors = ", ".join(drink.get_flavors())
        #    receipt += f"{i + 1}: base - {base}, Flavors - {flavors}\n"
        return receipt_data
    
    # Add drink items to list:
    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError("You can only add drinks to this order.")
        
    # Remove drink items to list:
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid, cannot remove")
        