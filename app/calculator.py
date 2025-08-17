ALLOWED = {
    "age": (1, 120),
    "height": (40, 220),
    "weight": (10, 300),
    "activities": {1.2, 1.375, 1.55, 1.725, 1.9},
    "goals": {"maintenance", "cutting", "bulking"},
}

GOAL_ALIASES = {
    "manutenção": "maintenance",
    "cutting": "cutting",
    "bulking": "bulking",
}

class ValidationError(Exception):
    pass

class Person:
    def __init__(self, weight, height, age, gender, activity, goal="manutenção"):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender.lower()
        self.activity = activity
        self.goal = GOAL_ALIASES.get(goal, goal)
        self._validate()

    def _validate(self):
        if not (ALLOWED["age"][0] <= self.age <= ALLOWED["age"][1]):
            raise ValidationError("Idade fora do intervalo permitido.")
        if not (ALLOWED["height"][0] <= self.height <= ALLOWED["height"][1]):
            raise ValidationError("Altura fora do intervalo permitido.")
        if not (ALLOWED["weight"][0] <= self.weight <= ALLOWED["weight"][1]):
            raise ValidationError("Peso fora do intervalo permitido.")
        if self.activity not in ALLOWED["activities"]:
            raise ValidationError("Atividade inválida.")
        if self.goal not in ALLOWED["goals"]:
            raise ValidationError("Objetivo inválido.")
        if self.gender not in ("m", "f"):
            raise ValidationError("Sexo inválido; use 'm' ou 'f'.")

    def bmr_calc(self):
        base = 10 * self.weight + 6.25 * self.height - 5 * self.age
        base += 5 if self.gender == "m" else -161
        return round(base * self.activity)

    def water_calc(self):
        if self.age <= 17:
            return round(self.weight * 40)
        elif 18 <= self.age <= 55:
            return round(self.weight * 35)
        elif 56 <= self.age <= 65:
            return round(self.weight * 30)
        else:
            return round(self.weight * 25)

    def bmi_calc(self):
        height_m = self.height / 100
        bmi = round(self.weight / (height_m ** 2), 1)
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            category = "Peso ideal"
        elif 25 <= bmi < 30:
            category = "Sobrepeso"
        elif 30 <= bmi < 35:
            category = "Obesidade Nível 1"
        elif 35 <= bmi < 40:
            category = "Obesidade Nível 2"
        else:
            category = "Obesidade Nível 3"
        return bmi, category

    def macros_calc(self):
        base_bmr = self.bmr_calc()
        goal_cal = base_bmr
        if self.goal == "cutting":
            goal_cal -= 600
        elif self.goal == "bulking":
            goal_cal += 600

        protein = (goal_cal * 0.30) / 4
        fat = (goal_cal * 0.35) / 9
        carbs = (goal_cal * 0.35) / 4

        return {
            "goal": round(goal_cal),
            "proteins": round(protein),
            "fat": round(fat),
            "carbs": round(carbs),
        }

    def summary(self):
        base_bmr = self.bmr_calc()
        macros = self.macros_calc()
        bmi_index, bmi_health = self.bmi_calc()
        water_ml = self.water_calc()

        return {
            "bmr": {"base": base_bmr, "goal": macros["goal"]},
            "nutrients": {
                "proteins": macros["proteins"],
                "fat": macros["fat"],
                "carbs": macros["carbs"],
            },
            "water": {"ml": water_ml, "l": round(water_ml / 1000, 2)},
            "bmi": {"index": bmi_index, "health": bmi_health},
        }

