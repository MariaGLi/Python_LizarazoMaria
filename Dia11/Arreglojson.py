import json

with open("large-file.json", encoding="utf-8") as openfile:
    miJson= json.load(openfile)

print(miJson[3])

'''
for i in range (5):
  print(miJSON[i])
'''
crearEventos=[]
for i in range (len(miJson)):
    if(miJson[i]['type']=='CreateEvent'):
        crearEventos.append(miJson[i])

print(crearEventos[5]['actor']['id'])

for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

crearEventos[0]['id']=256
with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)