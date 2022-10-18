from collections import Counter

if __name__ == "__main__":
    no_of_shoes= int(input())
    shoe_sizes = list(map(int, input().split(" ")))
    no_of_customers = int(input())
    customer_desire_list = []
    eligible_shoes = dict(Counter(shoe_sizes).items())
    total = 0
    for i in range(no_of_customers):
        customer_wants = list(map(int, input().split(" ")))
        shoe_number, price = customer_wants
        stock = eligible_shoes.get(shoe_number)
        if stock is not None and stock > 0:
           total += price
           stock -= 1
           eligible_shoes.update({shoe_number: stock})
        else:
           pass
    print(f"{total}")

        