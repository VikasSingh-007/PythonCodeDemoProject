# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Main entry point of the Inventory Management System.

Step-by-step Instructions:
1. Import classes: Product, Category, Store, Report.
2. Create a Store object (this will hold all products and categories).
3. Implement a simple menu system:
   a. Add product
   b. Remove product
   c. Update stock
   d. Generate report
   e. Exit
4. Use input() to interact with the user.
5. Call appropriate Store methods based on the menu choice.

TODO for Students:
- Implement the menu logic.
- Make sure invalid choices are handled using try/except.
- Provide clean output for the user.
"""
# TODO: Import required classes here
# from product import Product
# from store import Store
# from report import Report


# Entry point for the system.
# TODO: Implement this file

# Entry point (menu-driven interface).
# Students will implement CLI to test functionality.

from inventory_students.store import Store
from inventory_students.product import Product
from inventory_students.report import Report
from inventory_students.category import Category
from inventory_students.exceptions import categoryNotFoundError, ProductNotFoundError


def main():
    # TODO: Create Store instance
    # TODO: Add some sample products
    # TODO: Menu options:
    #   1. Add Product
    #   2. Remove Product
    #   3. Update Stock
    #   4. Update Price
    #   5. Apply Discount
    #   6. Show Reports
    #   7. Export Data
    category_id = 0
    product_id = 0
    store_name = input("Enter Store Name:")
    s1 = Store(store_name)
    while True:
        caterory_name = input(
            "Add Category Name ex.ice cream (or 'exit' to add product):")
        if caterory_name.lower() == "exit":
            break
        category_id += 1
        category_id_name = "C"+str(category_id)
        s1.add_category(Category(caterory_name, category_id_name))
    while True:
      print("Menu Options:")
      print("1. Add Product\n2. Remove Product\n3. Update Stock\n4. Update Price\n5. Apply Discount\n6. Show Reports\n7. Export Data")
      function_name = input(
          "to continue select from menu option: (or 'exit'):")
      if function_name.lower() == "exit":
          break
      match function_name.lower().strip():
        case "add product" | "1":
            print("add product ....")
            name = input("add product name:")
            price = input("add product price:")
            stock = input("add product stock:")
            category = input("add product category:")
            check_category = False
            for k in s1.categories.keys():
                if s1.categories[k].name == category:
                    product_id += 1
                    product_id_name = "P"+str(product_id)
                    check_category = True
                    s1.categories[k].add_product(
                        Product(product_id_name, name, price, stock, category))

            if check_category == False:
                print("Error -Invalid category ,please select from following:")
                for k in s1.categories.keys():
                    print(s1.categories[k].name)
                category = input("add product category:")
                check_category = False
                for k in s1.categories.keys():
                    if s1.categories[k].name == category:
                        product_id += 1
                        product_id_name = "P"+str(product_id)
                        check_category = True
                        s1.categories[k].add_product(
                            Product(product_id_name, name, price, stock, category))
                if check_category == False:
                    raise categoryNotFoundError("Error: Invalid Category")

        case "remove product" | "2":
            print("remove product ....")
            product_to_remove = input("Enter product name:")
            check_product = False
            for k in s1.categories.keys():
                for p in s1.categories[k].products:
                    product_id_n = p.name
                    if product_to_remove == product_id_n:
                        s1.categories[k].remove_product(p.proudct_id)
                        check_product = True
            if check_product == False:
                 raise ProductNotFoundError("Error: Invalid product")

        case "update stock" | "3":
            print("update product stock ....")
            product_to_update_stock = input("Enter product name:")
            qty=input("Enter product Qty:")
            s1.update_stock(product_to_update_stock, qty)
        case "update price" | "4":
            print("update product price ....")
            product_to_update_price = input("Enter product name:")
            p_price=input("Enter product new price:")
            s1.update_price(product_to_update_price, p_price)
        case "apply discount" | "5":
            print("apply dicount ....")
            product_to_update_discount_category = input("Enter category name:")
            product_to_update_discount_percent= input("Enter discount % :")
            check_category = False
            for k in s1.categories.keys():
                if s1.categories[k].name == product_to_update_discount_category:
                    s1.apply_discount_to_category(product_to_update_discount_category, product_to_update_discount_percent)
                    check_category=True
            if check_category == False:
                print("Error -Invalid category ,please select from following:")
                for k in s1.categories.keys():
                    print(s1.categories[k].name)
                product_to_update_discount_category = input("Enter category name:")
                check_category = False
                for k in s1.categories.keys():
                    if s1.categories[k].name == product_to_update_discount_category:
                        s1.apply_discount_to_category(product_to_update_discount_category, product_to_update_discount_percent)
                        check_category=True
                if check_category == False:
                    raise categoryNotFoundError("Error: Invalid Category")
        case "show reports"|"6":
            r1=Report(s1)
            r1.category_summary()
            r1.total_inventory_value()
            r1.low_stock_items(10)
        case "export data" | "7":
            r1=Report(s1)
            r1.export_to_json("inventory_students/product_Details_json_report.json")
            r1.export_to_csv("inventory_students//product_Details_csv_report.csv")
            
       
if __name__ == "__main__":
    main()
