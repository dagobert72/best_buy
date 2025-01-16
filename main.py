from store import Store
from products import Product

def start(store: Store):
    while True:
        print("\nWelcome to Best Buy Store!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":

            products = store.get_all_products()
            if not products:
                print("No products available in the store.")
            else:
                for product in products:
                    print(product.show())

        elif choice == "2":

            total_quantity = store.get_total_quantity()
            print(f"Total items in store: {total_quantity}")

        elif choice == "3":

            shopping_list = []
            while True:
                products = store.get_all_products()
                print("\nAvailable products:")
                for idx, product in enumerate(products, 1):
                    print(f"{idx}. {product.show()}")

                product_choice = input("Enter the product number to buy (or 'done' to finish): ").strip()
                if product_choice.lower() == "done":
                    break

                try:
                    product_idx = int(product_choice) - 1
                    if product_idx < 0 or product_idx >= len(products):
                        print("Invalid product number. Try again.")
                        continue

                    quantity = int(input(f"Enter quantity for {products[product_idx].name}: ").strip())
                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue

                    shopping_list.append((products[product_idx], quantity))
                except ValueError:
                    print("Invalid input. Please try again.")

            try:
                total_price = store.order(shopping_list)
                print(f"Order completed! Total price: {total_price} dollars.")
            except ValueError as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Thank you for visiting! Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)
