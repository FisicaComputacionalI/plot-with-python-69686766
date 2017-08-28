#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones a la maquina de una forma resumida. Matplotlib es una libreria para crear graficas en 2 dimensiones. 
import matplotlib.pyplot as plt
#Construimos el objeto plt introduciendo valores que se grafican contra el numero de entrada. Por ejemplo si queremos graficar el crecimiento de un material por dia en centimetros. 
plt.plot([5,3,4,3,2,3,1,5,8,1,3,0,1,3,5,2,1,0,1,2,1])
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
plt.ylabel('# de hrmanos y primos [cm]')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()

