#calculating assets
def calculate_assets(liabilities, equity):
    return liabilities + equity

#calculating equity
def calculate_equity(liabilities, assets):
    return liabilities - assets

#calculating libilities
def calculate_liabilities(assets, equity):
    return assets - equity

#Interest formulas
def calculate_simpleinterest(principal, rate, time):
    return principal * rate * time

def calculate_compoundinterest(principal, rate, time, conversions):
    return principal * (1 + (rate / 100) / conversions) ** (time * conversions)

#Straight line depreciation 
def calculate_straightlinedepreciation(costprice, residualvalue, usefulife):
    return (costprice - residualvalue) / usefulife

#Income formula
def calculate_income(revenue, expense):
    return(revenue - expense)

#Revenue formula
def calculate_revenue(income, expense):
    return(income + expense)

#Expense formula
def calculate_expense(revenue, income):
    return(income + revenue)

#Sales formula
def calculate_sales(costofsales, grossprofit):
    return(costofsales + grossprofit)

#Sales (Stock) formula
def calculate_salestock(stockbegin, purchases, expense, endstock, grossprofit):
    return(stockbegin + purchases + expense - endstock + grossprofit)

#Gross profit formula
def calculate_grossprofit(sales, costofsales):
    return(sales - costofsales)

#Material consumpton methods
def calculate_materialconsumptioninv(openingstock, receivedgoods, finalstock):
    return(openingstock + receivedgoods - finalstock)

# Display menu options to the user
print("Welcome to the Financial Calculator! What would you like to calculate?")
print("1. Calculate Assets")
print("2. Calculate Equity")
print("3. Calculate Liabilities")
print("4. Calculate Simple Interest")
print("5. Calculate Compound Interest")
print("6. Straight-line Depreciation")
print("7. Calculate Inconme")
print("8. Calculate Revenue")
print("9. Calculate Expenses")
print("10. Calculate Sales")
print("11. Calculate Sales Stock formula")
print("12. Calculate Gross Profit")
print("13 Calculate Material Consumption")
      
choose_formula = input("Enter your choice (1-12): ")

if choose_formula == "1":
    liabilities = float(input("Enter total Liabilities: "))
    equity = float(input("Enter total equity: "))
    result = calculate_assets(liabilities, equity)
    print(f"Total Assets: {result}")

elif choose_formula == "2":
    liabilities = float(input("Enter total Liabilities: "))
    assets = float(input("Enter total assets: "))
    result = calculate_equity(liabilities, assets)
    print(f"Total Equity: {result}")

elif choose_formula == "3":
    equity = float(input("Enter total equity: "))
    assets = float(input("Enter total assets: "))
    result = calculate_liabilities(assets, equity)
    print(f"Total Liabilities: {result}")

elif choose_formula == "4":
    principal = float(input("Principal amount: "))
    rate = float(input("Rate amount (in %): "))
    time = float(input("time (in years): "))
    result = calculate_simpleinterest(principal, rate, time)
    print(f"Simple interest amount: {result}")

elif choose_formula == "5":
    principal = float(input("Principal amount: "))
    rate = float(input("Rate amount (in %): "))
    time = float(input("time(in years): "))
    conversions = float(input("number of conversions (monthly, quarterly, etc): "))
    result = calculate_compoundinterest(principal, rate, time, conversions)
    print(f"Compound interest amount: {result}")

elif choose_formula == "6":
    costprice = float(input("Asset cost price: "))
    residualvalue = float(input("Residual/Salvage value: "))
    usefulife = float(input("Useful life consumption(in years): "))
    result = calculate_straightlinedepreciation(costprice, residualvalue, usefulife)
    print(f"Straight-line depreciation amount: {result}")

elif choose_formula == "7":
    revenue = float(input("Revenue: "))
    expense = float(input("Expense: "))
    result = calculate_income(revenue, expense)
    print(f"Income amount: {result}")

elif choose_formula == "8":
    income = float(input("Income: "))
    expense = float(input("Expense: "))
    result = calculate_revenue(income, expense)
    print(f"Revenue amount: {result}")

elif choose_formula == "9":
    revenue = float(input("Revenue: "))
    income = float(input("Income: "))
    result = calculate_expense(revenue, income)
    print(f"Expense amount: {result}")

elif choose_formula == "10":
    costofsales = float(input("Cost of sales: "))
    grossprofit = float(input("Gross Profit: "))
    result = calculate_sales(costofsales, grossprofit)
    print(f"Sales amount: {result}")

elif choose_formula == "11":
    stockbegin = float(input("Stock in the beginning: "))
    purchases = float(input("Purchases: "))
    expense = float(input("Direct Expense: "))
    endstock = float(input("Stock at the end: "))
    grossprofit = float(input("Gross Profit: "))
    result = calculate_salestock(stockbegin, purchases, expense, endstock, grossprofit)
    print(f"Sales amount: {result}")

elif choose_formula == "12":
    sales = float(input("Sales: "))
    costofsales = float(input("Cost of Sales: "))
    result = calculate_grossprofit(sales, costofsales)
    print(f"Gross Profit amount: {result}")

elif choose_formula == "13":
    openingstock = float(input("Opening Stock: "))
    receivedgoods = float(input("Received Goods: "))
    finalstock = float(input("Final Stock: "))
    result =calculate_materialconsumptioninv(openingstock, receivedgoods, finalstock)
    print(f"Material Consumption amount: {result}")

else:
    print("Invalid input. Please try again")

  

