import requests

def cooking(item):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={item}"
    api = "1"
    headers = {
        'X-Auth-Token': api
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    meals = data['meals']
    if meals is None:
        print("No recipe found.")
        return
    for meal in meals:
        meal_name = meal['strMeal']
        meal_category = meal['strCategory']
        meal_area = meal['strArea']
        meal_instructions = meal['strInstructions']
        print(f"Recipe for {meal_name}:")
        print(f"Category: {meal_category}")
        print(f"Area: {meal_area}")
        print(f"Instructions: {meal_instructions}")
        print("Ingredients:")
        for i in range(1, 21):
            ingredient = meal[f'strIngredient{i}']
            measure = meal[f'strMeasure{i}']
            if ingredient:
                print(f"{measure} {ingredient}")
