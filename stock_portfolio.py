import yfinance as yf

def display_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\nCurrent Portfolio:")
    print(f"{'Ticker':<10}{'Shares':<10}{'Price':<10}{'Value':<10}")
    total_value = 0

    for ticker, shares in portfolio.items():
        stock = yf.Ticker(ticker)
        stock_price = stock.history(period="1d")['Close'].iloc[-1]
        stock_value = stock_price * shares
        total_value += stock_value
        print(f"{ticker:<10}{shares:<10}{stock_price:<10.2f}{stock_value:<10.2f}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")


def add_stock(portfolio):
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    shares = int(input("Enter the number of shares: "))
    portfolio[ticker] = portfolio.get(ticker, 0) + shares
    print(f"Added {shares} shares of {ticker} to your portfolio.")


def remove_stock(portfolio):
    ticker = input("Enter the stock ticker symbol to remove: ").upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from your portfolio.")
    else:
        print("Stock not found in your portfolio.")


def main():
    portfolio = {}
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Display Portfolio")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            display_portfolio(portfolio)
        elif choice == '2':
            add_stock(portfolio)
        elif choice == '3':
            remove_stock(portfolio)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
