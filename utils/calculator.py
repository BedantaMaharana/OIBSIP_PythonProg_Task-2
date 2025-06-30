def validate_input(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if 10 <= weight <= 300 and 0.5 <= height <= 2.5:
            return weight, height
    except:
        pass
    return None, None

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
