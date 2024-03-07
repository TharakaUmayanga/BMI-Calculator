from pyscript import document


def calculate_bmi(click):
    weight = float(document.getElementById("weight").value)
    height = float(document.getElementById("height").value)
    bmi = weight / (height / 100) ** 2

    document.getElementById("result").textContent = f"Your BMI is: {bmi:.1f}"


    categories = {
        "Underweight": bmi <= 18.5,
        "Normal": bmi > 18.5 and bmi <= 24.9,
        "Overweight": bmi > 25 and bmi <= 29.9,
        "Obese": bmi > 30
    }

    category = next((key for key, value in categories.items() if value), None)
    document.getElementById("category").textContent = f"Category: {category}"
