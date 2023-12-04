from ShoppingKJ import Shopping

# A function that creates a list of objects
def lob():
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
    for i in range(numOfItems):
        print(f'Item #{i+1}-')
        food = input("Enter Food:")
        foodAmount = float(input("Enter amount of pounds:"))
        foodobj = Shopping(food,foodAmount)
        foodList.append(foodobj)
    return foodList

# A function to display the contents of the list.
def displayList(foodList):
    print("")
    print("Here's a summary of the items purchased:")
    print("-----------------------------------------")
    for food in foodList:
        print(f'Item: {food.foodName}')
        print(f'Amount Ordered: {food.foodAmount} pounds')
        print(f'Price per pound: ${food.standardPrice}')
        print(f'Price of order: ${food.totalPrice}\n')

# A function that calculates the total cost of all items. 
def totalCost(foodList):
    foodPrices = list()
    for food in foodList:
        foodPrices.append(food.totalPrice)
    return sum(foodPrices)

# A main function
def fancyShopping():
    foodlist = lob()
    displayList(foodlist)
    print(f'Total cost: ${totalCost(foodlist)}')

fancyShopping()
