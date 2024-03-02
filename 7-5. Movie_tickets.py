def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

def main():
    total_tickets = int(input("Enter the number of tickets: "))
    total_cost = 0

    for i in range(total_tickets):
        age = int(input(f"Enter the age of ticket holder {i+1}: "))
        ticket_price = calculate_ticket_price(age)
        total_cost += ticket_price

    print(f"Total cost for {total_tickets} tickets: ${total_cost}")

if __name__ == "__main__":
    main()