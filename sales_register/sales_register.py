sales = {}
def register_sale():
    another_product = "yes"

    while another_product == "yes":
        product = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))

        if product in sales:
            sales[product]["quantity"] += quantity
        else:
            sales[product] = {"price": price, 
                             "quantity": quantity,}
                             
        another_product = input("Do you want to add another product? (yes/no): ")
        print("------------------------------------------------------------------------")

def total_sales():
    total=0
    for product in sales:
        price = sales [product]["price"]
        quantity = sales [product]["quantity"]
        subtotal = price * quantity
        total = subtotal + total
    return total

def show_summary():
    print("SALES SUMMARY: ")
    for product in sales:
        print("product:", product)
        print("quantity:", sales[product]["quantity"])
        print("price:", sales[product]["price"])
        print("------------------------------------------------------------------------")
        
    

register_sale()
total = total_sales()
show_summary()
print("total:", total)
