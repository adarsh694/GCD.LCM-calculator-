#gcd and lcm calculator 
a  = int(input("Enter first number: "))
b  = int(input("Enter second number: "))

# handle both zero case
if a == 0 and b == 0:
    gcd = 0
else:
    for i in range(min(abs(a), abs(b)), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
# calculate lcm using gcd
lcm = 0 if gcd == 0 else abs(a * b) // gcd

print(f"GCD = {gcd}")
print(f"LCM = {lcm}")

