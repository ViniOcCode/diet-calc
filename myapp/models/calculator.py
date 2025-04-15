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
        Calculates the basal metabolic rate (BMR) of the person using Mifflin-St Jeor Equation.

        returns:
            int: The calculated BMR
        """
        # Mifflin-St Jeor Equation
        if self.gender.lower() == 'm':
            return round((10 * self.weight + 6.25 * self.height - 5 * self.age) + 5)
        elif self.gender.lower() == 'f':
            return round((10 * self.weight + 6.25 * self.height - 5 * self.age) + -151)
        else:
            raise ValueError("Given gender is not compatible yet.")

    def water_calc(self):
        """
        Calculates the average water required of the person.

        returns:
            int: The calculated mls of water required.
        """

        if 17 >= self.age:
            return self.weight * 40
        elif 18 <= self.age <= 55:
            return self.weight * 35
        elif 56 <= self.age <= 65:
            return self.weight * 30
        else:
            return self.weight * 25
    
    def bmi_calc(self):
        height = self.height / 100 
        bmi = round(self.weight/(height * height))

        if bmi < 18.5:
            return bmi, "Muito magro"
        elif 18.6 < bmi < 24.9:
            return bmi, "Peso ideal"
        elif 25 < bmi < 29.9:
            return bmi, "Sobrepeso"
        elif bmi > 30:
            if 30 < bmi < 34.5:
                return bmi, "Obesidade Nível 1"
            elif 35 < bmi < 39.9:
                return bmi, "Obesidade Nível 2"
            else:
                return bmi, "Obesidade Nível 3"
    
    def macros_calc(self):
        goal = self.bmr_calc()
        if self.goal == 'cutting':
            goal -= 600
            protein = self.weight * 2.0
        elif self.goal == 'bulking': 
            goal += 600
            protein = self.weight * 1.8
        else:
            protein = self.weight * 1.6
        
        fat = (goal * 0.25) / 9
        carbs = (goal - (protein * 4 + fat * 9)) / 4

        return goal, protein, fat, carbs

    def summary(self):
        """
        Shows all the person's needs and adjust the BRM depending on the goal.

        returns:
            dict: returns a dict with nutrients (proteins, fat and carbs), water and brm needed.
        """
        goal, protein, fat, carbs = self.macros_calc()

        index, health = self.bmi_calc()

        return { 
            "nutrients": {
                "proteins": round(protein, 2),
                "fat": round(fat, 2),
                "carbs": round(carbs, 2)
            },

            "bmr":{
                "base": self.bmr_calc(),
                "goal": goal
            },

            "water": {
                "ml": self.water_calc(),
                "l": round((self.water_calc() / 1000), 2)
            },
            "bmi": {
                "index": index,
                "health":  health
            }
        }