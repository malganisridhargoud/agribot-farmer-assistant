def get_crop_suggestion(soil, climate, season):
    if not soil or not climate or not season:
        return "🚫 Please fill all fields to get accurate suggestions."
    if soil == "Loamy" and climate == "Tropical" and season == "Summer":
        return "✅ Recommended Crops: Rice, Sugarcane, Cotton."
    elif soil == "Sandy" and climate == "Dry":
        return "✅ Recommended Crops: Millet, Groundnut, Sunflower."
    elif soil == "Clay" and climate == "Temperate":
        return "✅ Recommended Crops: Wheat, Barley, Potatoes."
    return "✅ Recommended Crops: Maize, Soybean, Pulses."

def get_fertilizer_advice(crop, ph):
    if not crop or not ph:
        return "🚫 Please fill all fields."
    if ph < 5.5:
        return f"🌱 For {crop}, use acidic soil fertilizers like ammonium sulfate."
    elif ph > 7.5:
        return f"🌱 For {crop}, use alkaline soil fertilizers like ammonium nitrate."
    return f"🌱 For {crop}, use balanced NPK fertilizers."

def get_pest_control(pest, crop):
    if not pest or not crop:
        return "🚫 Please fill all fields."
    return f"🛡 To control {pest} in {crop}, use neem oil spray and keep fields hygienic."

def get_market_price(crop, location):
    if not crop or not location:
        return "🚫 Please fill all fields."
    return f"💹 Market price of {crop} in {location} is approx ₹1500 per quintal. (Subject to change)"

def get_govt_schemes(state):
    if not state:
        return "🚫 Please select a state."
    return f"🏛 Govt schemes in {state}: PM-Kisan, Crop Insurance, Soil Health Card, Fertilizer Subsidy."