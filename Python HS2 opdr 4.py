tax = 1.07

price_item1 = 2.50
price_item2 = 6.75
price_item3 = 4.65
price_item4 = 3.95
price_item5 = 2.55
total_without_tax = price_item1 + price_item2 + price_item3 + price_item4 + price_item5
tax_only = total_without_tax * 0.07
total_with_tax = total_without_tax + tax_only

round(total_without_tax, 2)
round(tax_only, 2)
round(total_with_tax, 2)


print("The total price without tax is: $" +format(total_without_tax, ",.2f"),
      "The amount of money you have to pay in only tax is: $" + format(tax_only, ",.2f"),
      "The total price including tax is: $" + format(total_with_tax, ",.2f"), sep = "\n")
