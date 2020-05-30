hours = input("Enter hours: ")
h = float(hours)
rate = input("Enter the rate: ")
r = float(rate)
if h <= 40:
    print(h * r)
if h > 40:
    print(r * 1.5 * (h-40) + 40 *r )
