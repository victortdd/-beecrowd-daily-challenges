negativo = 0
positivo = 0
par = 0
impar = 0
for _ in range(5):
    number = int(input())
    if number < 0:
        negativo +=1
    if number %2 == 0:
        par +=1
    if number %2 == 1:
        impar +=1
    if number > 0:
        positivo +=1
print (f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)")