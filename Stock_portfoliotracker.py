# Smart Portfolio Tracker
# Created by Vignesh

print("Welcome to Smart Portfolio Tracker")
print("----------------------------------")

portfolio = []

total_invested = 0
total_current = 0

number_of_stocks = int(input("How many stocks do you own? "))

for i in range(number_of_stocks):

    print("\nStock", i + 1)

    stock_name = input("Enter stock name: ")

    quantity = int(input("Enter quantity: "))

    purchase_price = float(
        input("Enter purchase price per share: ")
    )

    current_price = float(
        input("Enter current market price: ")
    )

    invested = quantity * purchase_price
    current_value = quantity * current_price

    total_invested += invested
    total_current += current_value

    portfolio.append([
        stock_name,
        quantity,
        invested,
        current_value
    ])

print("\nPortfolio Summary")
print("----------------------------------")

for stock in portfolio:

    profit = stock[3] - stock[2]

    print("\nStock Name :", stock[0])
    print("Quantity   :", stock[1])
    print("Invested   : ₹", stock[2])
    print("Current    : ₹", stock[3])
    print("Profit/Loss: ₹", profit)

overall_profit = total_current - total_invested

if total_invested > 0:
    overall_return = (
        overall_profit / total_invested
    ) * 100
else:
    overall_return = 0

print("\n----------------------------------")
print("Total Invested :", total_invested)
print("Current Value  :", total_current)
print("Profit/Loss    :", overall_profit)
print("Return %       :", round(overall_return, 2))
print("----------------------------------")

if overall_profit > 0:
    print("Your portfolio is currently in profit.")
elif overall_profit < 0:
    print("Your portfolio is currently in loss.")
else:
    print("No profit and no loss.")

with open("portfolio_report.txt", "w") as file:

    file.write("PORTFOLIO REPORT\n")
    file.write("--------------------------\n")

    for stock in portfolio:

        profit = stock[3] - stock[2]

        file.write(
            f"Stock: {stock[0]}\n"
        )

        file.write(
            f"Quantity: {stock[1]}\n"
        )

        file.write(
            f"Invested: {stock[2]}\n"
        )

        file.write(
            f"Current Value: {stock[3]}\n"
        )

        file.write(
            f"Profit/Loss: {profit}\n\n"
        )

    file.write(
        f"Total Invested: {total_invested}\n"
    )

    file.write(
        f"Current Value: {total_current}\n"
    )

    file.write(
        f"Overall Profit/Loss: {overall_profit}\n"
    )

print("\nReport saved in portfolio_report.txt")
print("Thank you for using the program.")