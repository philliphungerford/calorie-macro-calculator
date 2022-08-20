# Calorie Calculator
def fCalculateCaloriesLose(CurrentBodyWeightKG):
    CaloriesMaintain = ((CurrentBodyWeightKG)*2.2) * 15
    CaloriesLose = CaloriesMaintain - 500
    print("Calories:", CaloriesLose)
    return(CaloriesLose)

# Macronutrients
def fMacrosKeto(Calories):
    PFats     = Calories * 0.70
    PCarbs    = Calories * 0.05
    PProteins = Calories * 0.25
    
    print("Fats: ", round(PFats), "Carbs: ", round(PCarbs), "Protein: ", PProteins)
    print()
    print("Grams")
    print("Fats: ", round(PFats/9), "Carbs: ", round(PCarbs/4), "Protein: ", round(PProteins/4))
    print("##############################################################")

#


# Run
fMacrosKeto(fCalculateCaloriesLose(CurrentBodyWeightKG = 77))
