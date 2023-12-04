from ShoppingKJ import Shopping

# A function that creates a list of objects (lob = list of objects)
def lobKJ():
    # Makes an Empty List
    foodList = list()
    # Validation for number of items
    while True:
        try:
            numOfItems = int(input("How many items will you order today?"))
        except ValueError:
            print("Enter a valid number!")
        if numOfItems > 0:
            break
        else:
            print("Number of items must be at least 1.")
            continue
    # Loop through the range of items specified by numOfItems
    for i in range(numOfItems):
        print(f'Item #{i+1}-')
        # Prompt the user to enter the type of food
        food = input("Enter Food:")
        # Prompt the user to enter the amount of food in pounds and validation
        while True:
            foodAmount = float(input("Enter amount of pounds:"))
            if foodAmount > 0:
                break
            else:
                print("Amount of pounds must be greater than 0.")
                continue
        # Create a Shopping object with the entered food and its amount
        foodobj = Shopping(food,foodAmount)
        # Append the Shopping object to the foodList
        foodList.append(foodobj)
    return foodList

# A function to display the contents of the list.
def displayListKJ(foodList):
    print("")
    print("Here's a summary of the items purchased:")
    print("-----------------------------------------")
    for food in foodList:
        print(f'Item: {food.foodName}')
        print(f'Amount Ordered: {food.foodAmount} pounds')
        print(f'Price per pound: ${food.standardPrice}')
        print(f'Price of order: ${food.totalPrice}\n')

# A function that calculates the total cost of all items. 
def totalCostKJ(foodList):
    # Creates an empty list
    foodPrices = list()
    #Loop through all the items in the list of objects
    for food in foodList:
        # Access the total price of the specified food and put it in the empty list
        foodPrices.append(food.totalPrice)
    # Returns the total sum of price
    return sum(foodPrices)

# A main function
def fancyShoppingKJ():
    foodlist = lobKJ()
    displayListKJ(foodlist)
    print(f'Total cost: ${totalCostKJ(foodlist)}')

fancyShoppingKJ()
