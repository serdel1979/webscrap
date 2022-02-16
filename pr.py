secciones = []

for i in range(137):
    val = ("0000"+str(i+1))[-5:]
    secciones.append(val)
secciones.append("00998")
secciones.append("00999")

for i in secciones:
    print(i)