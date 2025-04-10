class Person:
    """

    This represents all values of a person
    
    Attributes:
        weight (float): Person's weight.
        height (int): Person's height.
        year (int): Birth year of the person.
        sex (str): Sex of the person; m to male, f to female.
        activity (float): Activity level of the person. 
        goal (str): Goal of the person; 'cutting', 'bulking' or 'maintenance'.
    """
    def __init__(self, *args, activity=None, weight=None, height=None, year=None, sex=None, goal="manutenção"):
        if None in [activity, weight, height, year, sex]:
            raise ValueError("Todos os campos precisam ser preenchidos!")   

        self.activity = activity
        self.weight = weight
        self.height = height
        self.year = year
        self.sex = sex
        self.goal = goal

    def tmb_calc(self):
        """
        Calculates the basal metabolic rate (BMR) of the person.

        returns:
            int: The calculated BMR

        """
        if self.sex.lower()== 'm':
            return round(self.activity * (66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.year)))
        else:
            return round(self.activity * (655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.year)))

    def water_calc(self):
        """
        Calculates the average water required of the person.

        returns:
            int: The calculated mls of water required.

        """
        if 17 >= self.year:
            return self.weight * 40, 2
        elif 18 <= self.year <= 55:
            return self.weight * 35
        elif 56 <= self.year <= 65:
            return self.weight * 30
        else:
            return self.weight * 25
    
    def summary(self):
        """
        Calculate the sum of all the person's needs and adjust the BRM depending on the goal.

        returns:
            dict: returns a dict with nutrients (proteins, fat and carbs), water and brm needed.

        """
        base = self.tmb_calc()
        if self.goal == 'cutting':
            base -= 600
            protein = self.weight * 2.0
        elif self.goal == 'bulking': 
            base += 600
            protein = self.weight * 1.8
        else:
            protein = self.weight * 1.6
        
        fat = (base * 0.25) / 9
        carbs = (base - (protein * 4 + fat * 9)) / 4

        return { 
            "nutrients": {
                "proteins": round(protein, 2),
                "fat": round(fat, 2),
                "carbs": round(carbs, 2)
            },
            "water": self.water_calc(),
            "tmb": base
        }