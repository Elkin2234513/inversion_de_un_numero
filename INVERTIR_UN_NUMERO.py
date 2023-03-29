print("-------------------------")
print("-------------------------")
print("   INVERTIR EL NUMERO ")
print("-------------------------")
print("-------------------------")



n = int(input("DIGITE UN NUMERO DE TRES CIFRAS: "))

a = n % 10 

b = (n % 100)//10

c = (n % 1000)//100

print(("EL INVERSO ES: ")+str(a) +str(b) +str(c))

