def shop_from_grocery_list(*args):
    budget, shopping_list, *products = args

    def buying_products(budget, shopping_list):

        while products:
            product = products.pop(0)
            name, price = product[0], float(product[1])

            if name in shopping_list:
                if budget < price:
                    break
                else:
                    budget -= price
                    shopping_list.remove(name)
        return budget, shopping_list

    budget, shopping_list = buying_products(budget, shopping_list)

    if not shopping_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."
