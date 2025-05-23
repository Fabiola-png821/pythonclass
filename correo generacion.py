#correo generador
correo= input("Ingrese su nombre:")
nombre=input("Ingrese su apellido:")
print(correo,nombre,"@keyinstitute.edu.sv")

#propina
t = float(input())
p = float(input())
print(f"\nTotal de la cuenta: ${t:.2f}")
print(f"Propina: ${t*p/100:.2f}")
print(f"Total de la cuenta con propina ({int(p)}%): ${t + t*p/100:.2f}")


#contraseña
contraseña =input("Escribe la contraseña:")
mayuscula = False
minuscula =False 
numero= False 

for i in contraseña:
    if i.isupper():
        mayuscula= True 
    elif i.islower():
        minuscula= True
    elif i.isdigit(): 
        numero= True
   
if mayuscula and minuscula and numero == True:
    print("contraseña segura")
else: 
    print("contraseña insegura")

#año bisiesto 
a= int(in)
#numero magico 