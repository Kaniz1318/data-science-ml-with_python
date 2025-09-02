year=input("Tell me a year:")
year=int(year)
if year%100!=0 and year%4==0:
    print(f"This {year} is leap year")
elif year%100==0 and year%400==0:
    print(f"This {year} is leap year")
else:
    print("No")
    


