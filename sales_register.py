sales = {}
def register_sale():
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

def show_summary(sales):
    total = 0
    print("SALES SUMMARY: ")
    for product in sales:
        print("product:", product)
        print("quantity:", sales[product]['quantity'])
        print("total:", sales[product]['total'])
        print("------------------------------------------------------------------------")
    total += sales[product]['total']
    print("Total sales:", total)

register_sale()
show_summary(sales)
