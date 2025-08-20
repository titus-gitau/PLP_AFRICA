def calculate_discount(price, discount_percentage):

    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price



original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))


final_price = calculate_discount(original_price, discount)


if discount >= 20:
    print(f"Discount has been applied! The price is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price remains: {final_price:.2f}")
