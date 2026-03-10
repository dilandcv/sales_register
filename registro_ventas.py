def register_sale():
    sales = {}
    another_product = "yes"

    while another_product == "yes":
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))

        if product in sales:
            sales[product]['quantity'] += quantity
            sales[product]['total'] += quantity * price
        else:
            sales[product] = {'quantity': quantity, 
                             'total': quantity * price}
        another_product = input("Do you want to add another product? (yes/no): ")
        print("------------------------------------------------------------------------")
    return sales

register_sale()
