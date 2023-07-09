def calculate_best_price_and_quantity(material, markup):
    print("You've selected " + material + " with a markup of " + str(markup) + "%.")

    avg_market_price = float(input("Please enter the average market price for " + material + ": "))
    amount_in_inventory = float(input("Please enter the amount of " + material + " in your inventory: "))

    best_price = avg_market_price * (1 + markup/100)
    best_quantity_to_sell = amount_in_inventory // 1  # The '//' operator is used to get the largest whole number.

    return best_price, best_quantity_to_sell


material = 'your_material'
markup = float(input("Please enter your desired markup percentage (without the % symbol): "))

best_price, best_quantity_to_sell = calculate_best_price_and_quantity(material, markup)

print("\nThe best price to sell your " + material + " is: " + str(best_price) + ".")
print("The best quantity to sell is: " + str(best_quantity_to_sell) + ".")
