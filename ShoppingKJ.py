class Shopping:
    def __init__(self, foodName, foodAmount):
        # Sets the food name
        self.foodName = foodName
        # Sets the amount of food in pounds
        self.foodAmount = foodAmount
        # Sets the standard price of food per pound
        self.standardPrice = 0
        self.__PriceListKJ()
        # Sets the total price 
        self.totalPrice = self.calculatePriceKJ()

    #Returns the price of the specified food per pound
    def  __PriceListKJ(self):
        if self.foodName == "Dry Cured Iberian Ham":
            self.standardPrice = 177.80
        elif self.foodName == "Wagyu Steaks":
            self.standardPrice = 450.00
        elif self.foodName == "Matsutake Mushrooms":
            self.standardPrice =  272.00
        elif self.foodName == "Kopi Luwak Coffee":
            self.standardPrice = 306.50
        elif self.foodName == "Moose Cheese":
            self.standardPrice = 487.20
        elif self.foodName == "White Truffles":
            self.standardPrice = 3600.00
        elif self.foodName == "Blue Fin Tuna":
            self.standardPrice = 3603.00
        elif self.foodName == "Le Bonnotte Potatoes":
            self.standardPrice = 270.81
        else:
            self.standardPrice = 0.00
    
    #Calculates the total price
    def calculatePriceKJ(self):
        return self.foodAmount * self.standardPrice

    def __str__(self):
        print(self.totalPrice)
