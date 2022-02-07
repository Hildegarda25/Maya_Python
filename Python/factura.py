importe=float(input("Ingrese su importe: \n --> "))
porcentaje=float(input("Ingrese el IGV: \n --> "))
porcentaje=porcentaje/100
IGV=importe*porcentaje
total=importe +IGV
print("El IGV es: {:.2f}".format(IGV))
print("El importe a pagar es: {:.2f}".format(total))
