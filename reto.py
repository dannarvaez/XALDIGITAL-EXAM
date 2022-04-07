# Reto de programación XALDIGITAL
#Daniel Narvaez
#Librerias usadas
import requests

#Obtenemos la información del url
url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
html_content = requests.get(url).text
con_len= len(html_content)

#Número de respuestas contestadas y sin contestar
answer1= "true"
lena1= len(answer1)
numbera1= 0

answer2= "false"
lena2= len(answer2)
numbera2= 0

for i in range(con_len-lena1+1):
    j=0
    while j<lena1:
        if (html_content[i+j] != answer1[j]):
          break
        j +=1
    if (j==lena1):
        numbera1 +=1
        j=0
        
for i in range(con_len-lena2+1):
    j=0
    while j<lena2:
        if (html_content[i+j] != answer2[j]):
          break
        j +=1
    if (j==lena2):
        numbera2 +=1
        j=0

print("Número de respuestas contestadas y sin contestar:",numbera1,",", numbera2)

#Menor número de vistas
vistas=[]
stringvistas= "view_count"
lenview= len(stringvistas)
j=1

for i in range(30):
    j=html_content.index("view_count",j,con_len)
    for z in range(6):
        if html_content[j+12+z]==",":
            if i!=29:
                vistas.append(";")
            break
        vistas.append(html_content[j+12+z])
    j=html_content.index(stringvistas,j,con_len)+1
vistasj="".join(vistas)
vistasn=vistasj.split(";")
vistasint=[]
for i in range(len(vistasn)):
    vistasint.append(int(vistasn[i]))
print("la respuesta con el menor número de vistas tiene: "+str(min(vistasint))+" vistas y es la respuesta número: "+str(vistasint.index(min(vistasint))+1) )

#Obtener respuesta más vieja y más actual
creation=[]
stringcreation= "creation_date"
lencreation= len(stringcreation)
j=1

for i in range(30):
    j=html_content.index("creation_date",j,con_len)
    for z in range(12):
        if html_content[j+15+z]==",":
            if i!=29:
                creation.append(";")
            break
        creation.append(html_content[j+15+z])
    j=html_content.index(stringcreation,j,con_len)+1
creationj="".join(creation)
creationn=creationj.split(";")
creationint=[]
for i in range(len(creationn)):
    creationint.append(int(creationn[i]))
print("La respuesta más vieja es la respuesta número: "+str(creationint.index(max(creationint))+1))
print("La respuesta más actual es la respuesta número: "+str(creationint.index(min(creationint))+1))


#Obtener la respuesta del owner con mayor reputación
reputation=[]
stringreputation="reputation"
lenreputation=len(stringreputation)
j=1
for i in range(30):
    j=html_content.index("reputation",j,con_len)
    for z in range(10):
        if html_content[j+12+z]==",":
            if i!=29:
                reputation.append(";")
            break
        reputation.append(html_content[j+12+z])
    j=html_content.index(stringreputation,j,con_len)+1
reputationj="".join(reputation)
reputationn=reputationj.split(";")
reputationint=[]
for i in range(len(reputationn)):
    reputationint.append(int(reputationn[i]))
print("La respuesta del owner con mayor reputación es la respuesta número: "+str(reputationint.index(max(reputationint))+1))


#Imprimir puntos del 2 al 5
print("Puntos del 2 al 5")
for i in range(2,5,1):
    print(html_content[i])