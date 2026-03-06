import re

# open and read the file
with open("/Users/timchik/Desktop/pp2/Practice-05/raw.txt") as f:
  text = f.read()

# Finding prices
prices = re.findall('x\s*([\d\s]+,\d{2})', text)
#x followed by any digits and whitecases, followed by a comma and 2 digits)

print("\nPrices:")
for price in prices:
    print(price)


# Finding product names
products = re.findall(r'\d+\.\s*\n(.+)', text) 
#any list followed after any number, dot, whitcase and a newline

print("\nProducts:")
for p in products:
    print("-", p.strip())


# Finding total amount
total = re.search(r'ИТОГО:\s*([\d\s,]+)', text)
#any numbers followed after Итого: 
if total:
    amount = total.group(1).replace(" ", "")
    print("\nTotal:", amount)


# Extracting date and time information
dt = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})', text)
if dt:
    print("\nDate:", dt.group(1))
    print("Time:", dt.group(2))


# Finding payment method
payment = re.search(r'(Банковская карта|Наличные)', text)
if payment:
    print("\nPayment method:", payment.group(1))

