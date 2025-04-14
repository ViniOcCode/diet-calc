ALLOWED_GOALS = {"manutenção", "maintenance", "cutting", "bulking"}
ALLOWED_ACTIVITIES = {1.2, 1.375, 1.55, 1.725, 1.9}
ALLOWED_AGES = range(1, 120)
ALLOWED_WEIGHT = range(20, 300)

class Person:
    """

    This represents all values of a person
    
    Attributes:
        weight (float): Person's weight.
        height (int): Person's height.
        age (int): Age of the person.
        gender (str): Gender of the person; m to male, f to female.
        activity (float): Activity level of the person. 
        goal (str): Goal of the person; 'cutting', 'bulking' or 'maintenance'.
    """
    def __init__(self, *args, activity=None, weight=None, height=None, age=None, gender=None, goal="manutenção"):

        if None in [activity, weight, height, age, gender]:
            raise ValueError("All fields need values.")   

        self.activity = activity
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.goal = goal

        self._validating()

    def _validating(self):
        if self.age not in ALLOWED_AGES:
            raise ValueError("Age value is not allowed.")

        if self.goal not in ALLOWED_GOALS:
            raise ValueError("Given goal is not allowed.")

        if self.activity not in ALLOWED_ACTIVITIES:
            raise ValueError("Activity value is not allowed.")

        if self.weight not in ALLOWED_WEIGHT:
            raise ValueError("Weight value is not allowed.")
            
    def bmr_calc(self):
        """
        Calculates the basal metabolic rate (BMR) of the person.

        returns:
            int: The calculated BMR
        """

        if self.gender.lower() == 'm':
            return round(self.activity * (66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)))
        elif self.gender.lower() == 'f':
            return round(self.activity * (655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)))
        else:
            raise ValueError("Given gender is not compatible yet.")

    def water_calc(self):
        """
        Calculates the average water required of the person.

        returns:
            int: The calculated mls of water required.
        """

        if 17 >= self.age:
            return self.weight * 40, 2
        elif 18 <= self.age <= 55:
            return self.weight * 35
        elif 56 <= self.age <= 65:
            return self.weight * 30
        else:
            return self.weight * 25
    
    def bmi_calc(self):
        bmi = self.weight/(self.height * self.height)   

        if bmi < 18.5:
            return bmi, "Underweight"
        elif 18.6 < bmi < 24.9:
            return bmi, "Healthy weight"
        elif 25 < bmi < 29.9:
            return bmi, "Overweight"
        elif bmi > 30:
            if 30 < bmi < 34.5:
                return bmi, "Obesity class 1"
            elif 35 < bmi < 39.9:
                return bmi, "Obesity class 2"
            else:
                return bmi, "Obesity class 3"
    
    def macros_calc(self):
        base = self.bmr_calc()
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

        return base, protein, fat, carbs

    def summary(self):
        """
        Shows all the person's needs and adjust the BRM depending on the goal.

        returns:
            dict: returns a dict with nutrients (proteins, fat and carbs), water and brm needed.
        """
        base, protein, fat, carbs = self.macros_calc()

        return { 
            "nutrients": {
                "proteins": round(protein, 2),
                "fat": round(fat, 2),
                "carbs": round(carbs, 2)
            },
            "bmr_goal": base,
            "water": self.water_calc(),
            "bmr_base": self.bmr_calc(),
            "bmi": self.bmi_calc()
        }