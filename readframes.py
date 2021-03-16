import wave
import numpy as np
import matplotlib as plt

#cargar archivo wav en la variable

goodmorning = wave.open('good-morningMan.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)

#mostrar el resultado de frames
#print(frames[:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer (frames, dtype='int16')

#Muestra los primeros 10 int
#print (ondaconvertida [:10])

framerate_gm = goodmorning.getframerate()

print(framerate_gm)

time_gm = np.linspace(start=0, stop=len(ondaconvertida)/framerate_gm)

print(time_gm)




#goodafternoon

goodafternoon = wave.open('good-afternoon.wav', 'r')

frames_ga = goodafternoon.readframes(-1)

print(frames_ga [:10])

ga_convertida = np.frombuffer(frames_ga, dtype='int16')

print(ga_convertida[:10])

framerate_ga =goodafternoon.getframerate()

print (framerate_ga)

time_ga = np.linspace(start = 0, stop = len(ga_convertida)/framerate_ga)

print(time_ga[:10])

#Generacion de la grafica

plt.title('Good morning vs Good Afternoon')

plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#agregar infomracion de las ondas para graficar
plt.plot(time_ga, ga_convertida, label="Good Afternoon")
plt.plot(time_gm, ondaconvertida, label="Good Morning", alpha=0.5)

plt.legend()
plt.show()

#bruh

bruh = wave.open('bruh.wav', 'r')

frames_bruh= bruh.readframes(-1)

print (frames_bruh [:10])

br_convertida = np.frombuffer(frames_bruh, dtype='int16')

print (br_convertida[:10])

framerate_br = bruh.getframerate()

print (framerate_br)

time_br =  np.linspace(start=0, stop=len(br_convertida)/framerate_br)

print (time_br)

#nice

nice = wave.open('nice.wav', 'r')

frames_nice= nice.readframes(-1)

print (frames_nice [:10])

nc_convertida = np.frombuffer(frames_nice, dtype='int16')

print (nc_convertida[:10])

framerate_nc = nice.getframerate()

print (framerate_nc)

time_nc =  np.linspace(start=0, stop=len(nc_convertida)/framerate_nc)

print (time_nc)

plt.title('Nice vs. Bruh')

plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

plt.plot(time_nc, nc_convertida, label='Nice')
plt.plot(time_br, br_convertida, label='Bruh', alpha=0.5)

plt.legend()
plt.show()

