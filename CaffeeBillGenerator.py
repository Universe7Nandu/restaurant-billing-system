import time

menu = {
    'Pizza': 120,
    'Burger': 80,
    'Salad': 40,
    'Coffee': 25
}
coupon_codes = {
    'DISCOUNT20': 0.2,
    'FREEDRINK': 'free_drink',  # Adds a free coffee to the bill
    'NANDESH25': 0.2,  # 20% discount
    'NANDU': 0.2       # 20% discount
}

def display_menu():
    print("\nWelcome to our Restaurant! Here's our menu:\n")
    print("Item\t\tPrice (₹)")
    print("-" * 25)
    for item, price in menu.items():
        print(f"{item}\t\t₹{price}")
    print("-" * 25)

def calculate_bill(order_list):
    return sum(menu[item] for item in order_list)

def apply_coupon(coupon, total):
    if coupon in coupon_codes:
        if coupon_codes[coupon] == 'free_drink':
            print("\n🎉 Congratulations! You get a free Coffee with your order!")
            return total  # No additional charges for the free drink
        elif isinstance(coupon_codes[coupon], float):
            discount = total * coupon_codes[coupon]
            print(f"\n🎉 Coupon applied! You saved ₹{discount:.2f}!")
            return total - discount
    print("\n❌ Invalid coupon code.")
    return total

# Main program
order_list = []
display_menu()

while True:
    order = input("\nWhat would you like to order? (Enter item name or 'done' to finish): ").capitalize()
    if order == 'Done':
        if not order_list:
            print("\n⚠️ You must order at least one item.")
            continue
        break
    elif order in menu:
        order_list.append(order)
        print(f"✅ {order} added to your order.")
    else:
        print("\n❌ Sorry, that item is not on the menu. Please try again.")

# Displaying the order summary
print("\nYour Order Summary:")
print("-" * 25)
for item in order_list:
    print(f"{item}\t\t₹{menu[item]}")
print("-" * 25)

# Calculating total bill
total = calculate_bill(order_list)
print(f"\nYour total bill is: ₹{total}")

# Asking if the customer wants to apply a coupon
use_coupon = input("\nDo you have a coupon code? (Yes/No): ").strip().lower()
if use_coupon == 'yes':
    coupon = input("\nEnter your coupon code: ").upper()
    total = apply_coupon(coupon, total)

# Final output
print("\nProcessing your bill...")
time.sleep(2)
print(f"\n💵 Your final bill is: ₹{total:.2f}")
print("\nThank you for dining with us! Have a great day! ✨")
