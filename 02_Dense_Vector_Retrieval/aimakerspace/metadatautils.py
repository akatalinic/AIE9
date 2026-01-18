def assign_metadata_category(text: str) -> str:
    """Assigns a category to the text based on keyword in chunk of text"""
    
    # Convert to lowercase once (more efficient)
    text_lower = text.lower()

    # Defining keywords for each category (removed duplicates)
    exercise_keywords = ["exercise", "workout", "fitness", "gym", "sports", "cardio", "strength", 
                        "flexibility", "balance", "stretching", "aerobic", "crossfit", "yoga", 
                        "physical activity", "exercise routine", "exercise plan", "exercise program", 
                        "exercise schedule"]
    nutrition_keywords = ["nutrition", "diet", "food", "calories", "protein", "carbohydrates", "fats", 
                         "vitamins", "minerals", "water", "hydration", "nutrient", "nutrition plan", 
                         "nutrition schedule", "nutrition routine"]
    mental_health_keywords = ["mental health", "anxiety", "depression", "stress", "wellness", 
                             "mindfulness", "meditation", "sleep", "relaxation"]

    exercise_score = sum(1 for keyword in exercise_keywords if keyword in text_lower)
    nutrition_score = sum(1 for keyword in nutrition_keywords if keyword in text_lower)
    mental_health_score = sum(1 for keyword in mental_health_keywords if keyword in text_lower)

    scores = {
        "exercise": exercise_score,
        "nutrition": nutrition_score,
        "mental_health": mental_health_score
    }

    best_suited_category = max(scores, key=scores.get)

    return best_suited_category 