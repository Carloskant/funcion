import math

def resolver_ecuacion_cuadratica(a, b, c):
   
    discriminante = (b**2) - 4*(a*c)

    if discriminante > 0:
 
        x1 = (-b - math.sqrt(discriminante))/(2*a)
        x2 = (-b + math.sqrt(discriminante))/(2*a)
        return(x1,x2)
    elif discriminante ==0:
        x = -b / (2*a)
        return(x,x)
    else:
        parte_real= -b / (2*a)
        parte_imaginaria=math.sqrt(-discriminante)/(2*a)
        x1 = complex(parte_real, parte_imaginaria)
        return(x1, x2)

a= 1
b= -5
c= 6

soluciones = resolver_ecuacion_cuadratica(a, b, c)
print ("RESPUESTA las solucines son:{soluciones}")
