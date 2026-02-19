'''
Author: Kevin Ramirez
Date: 2/14/2026
Program: InvManSys.py
Purpose: Creating a generic store management system for a grocery store where employee can check out or do an inventory cost check and see entire stock

Latest revision 2/19/2026: 
After another close revision there was some logic errors, along with weak structuring in my checkout function
Was able to research how to enumerate better and be able to let user type the number corresponding to the option or still type it
Used exception handling to get rid of some else statments that was causing indentation issues 
Also researched how to print out the recipt better and that was just to take the elements as a tuple
'''

#using a nested dictionary to catagorize the items for manual search
inventory_catalog: dict = { 
    
    "Ambient" :
      {
        "Ambient Produce":  
            {"Banana" : 0.99,
             "Watermelon": 1.50,
             "Mango": 0.65},
       "General Ambient": 
            {"Cereal": 2.99,
             "Macaroni": 2.00,
             "Spaghetti": 2.30,
             "Candy": 0.50},
        "Ambient Beverages" :
            {"Coke Bottle": 1.50,
             "Pepsi Bottle": 1.50,
             "Kids Juice": 1.20},
        "Large items": 
            {"Dog food": 8.99,
             "Cat food": 6.99,
             "12pk soda": 3.99,
             "24pk Water": 2.99}
      },

    "Chiller" : 
    {
        "Chill Beverages" : 
            {"Milk": 2.40,
             "Creamer": 1.50,
             "Smoothie": 1.99},
        "Chill Produce": 
            {"Strawberry": 0.70,
             "Cucumber": 0.85,
             "Broccoli": 0.60},
        "General Chill": 
            {"Cream cheese": 1.50,
             "Yogurt": 1.20,
             "Lunchables": 2.00},
        "Raw Meats":
            {"6oz steak": 4.00,
             "Full Chicken": 6.00,
             "Pork Chops" : 3.00}
    },
    
    "Freezer": 
    {
        "General Frozen": 
            {"Frozen Pizza": 3.90,
             "Frozen Pastry": 2.40,
             "TV Dinner": 2.70},
        "Frozen Meats" : 
            {"Frozen Shrimp 40ct": 6.99,
             "Frozen Turkey": 5.00,
             "Frozen Salmon": 3.50}
    }
}

#starting with two seperate function for each task, creating checkout
def Checkout():

    #will be adding a better output of the recipt and allow user to enter number corresponding to options
    list_of_items: list = []

    while True:
        #getting items to checkout(won't be any quantity for item in inventory for now, stock is constant)
        #printing keys so user can see where to find item, will enumerate the dictionary to avoid typing for the user
        print("\nItem Temperature Zones:")
        #printing keys so user can see where to find item
        for i, zone in enumerate(inventory_catalog, 1):
            print(f"{i}. {zone}")

        zone: str = input("Enter number or name of zone('q' to quit or 'f' to finalize): ").strip().lower()

        #q to return to main menu or f to finalize checkout and print total
        if zone == 'q':
            break

        #fixing how checkout outputs recipt
        elif zone == 'f':
            if not list_of_items:
                print("No items have been added.")
                continue
            
            else:
                total: float = sum(price for _, price in list_of_items)
                print("\n***Recipt***")

            for name, price in list_of_items:
                print(f"{name.title()}: ${price:.2f}")
            print(f"Total: ${total:.2f}")
            break

        #Allows user to match zone by number or name
        try:
            zone_idx = int(zone) - 1
            zone = list(inventory_catalog.keys())[zone_idx]
        except (ValueError, IndexError):
            if zone in inventory_catalog:
                zone = zone.title()
            else:
                print("Invalid zone. Try again.")
                continue
        
        #gets the key from first set and stores it to a variable which ill us to create a list that outputs the next list of keys
        selected_zone = inventory_catalog[zone]
        categories = list(selected_zone.keys())

        #promting user to select item category within following set of keys
        #think of a way to make this better but for now make it basic and straight forward steps to get the logic
        print(f"Select item category in {zone}:")

        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        
        cat_input: str = input("Enter items category(enter number or name): ").strip().lower()
        
        #same allows user to match category with number or type name
        try:
            cat_idx = int(cat_input) - 1
            category = categories[cat_idx]
        except (ValueError, IndexError):
            category = cat_input.title()
        if category not in selected_zone:
            print("Invalid category.")
            continue

        #gets the key from second set and stores it to a variable which ill us to create a list that outputs the next list of keys
        selected_category = selected_zone[category]
        items_list = list(selected_category.keys())

        for i, items in enumerate(items_list, 1):
            print(f"{i}. {items}")
        
        item = input("Select item from list(enter number or name): ").strip().lower()

        try:
            item_idx = int(item) - 1
            item_name = items_list[item_idx]
        except (ValueError, IndexError):
            item_name = item.title()
        
        price = selected_category[item_name]
        list_of_items.append((item_name, price))
        print(f"Added: {item_name} - ${price:.2f}")

    return 
              
#recursion for summing values in dictionary
def sum_nested_dict(d) -> float:

    '''
    Recursive function to sum up inventory cost

    :param dictionary
    :returns total cost of inventory
    '''
    total:float = 0
    for v in d.values():
        if isinstance(v, dict):
            total += sum_nested_dict(v)
        else:
            total += v
    return total

#creating a function to check whats in inventory and can take the sum of all items
def InventoryManagement():

    '''
    Viewer and cost for inventory

    :param none
    :prints entire catalog, search for specific category or item price, or total cost of entire catalog
    '''
    action: int = 0

    while True:
        action = int(input("Select options: \n"
                            "1. Print entire catalog\n"
                            "2. Sum up catalog cost\n"
                            "3. Return to main menu\n"))
        #input validation
        if action < 1 or action > 4:
            print(f"Invalid option: {action}.")
            continue

        elif action == 1:
            for key, value in inventory_catalog.items():
                print(f"{key}: {value}")

        elif action == 2:
            total_catalog_cost: float = sum_nested_dict(inventory_catalog)

            print(f"The total cost of inventory is: {total_catalog_cost:.2f}")
                  

        elif action == 3:
            break
    return

    
        


#creating main menu
menuChoice: int = 0

print("Inventory management system.\n")
while True:

    #creating menu for roles 
    menuChoice = int(input("Select task:\n"
    "1. Check out\n"
    "2. Inventory Managment\n"
    "3. Exit.\n"))

    if menuChoice < 1 or menuChoice > 3:
        print(f"Invalid Input. {menuChoice} is not an option")
        continue
    
    match menuChoice:
        case 1:
            Checkout()
        case 2:
            InventoryManagement()
        case 3:
            #closing program
            print("Closing app....")
            break

print("Goodbye.")
    
