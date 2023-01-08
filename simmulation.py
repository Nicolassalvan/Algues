import deplacement_final as df
import class_algue as cla 
import matplotlib.pyplot as plt
import settings as config


box = cla.Box(config.X_MAX,config.Y_MAX)
population = cla.Population(config.taille_max,box)
plt.xlim(-5,box.x_max+5)
plt.ylim(-5,box.y_max+5)
plt.scatter(population.x,population.y, s=population.taille)

for i in range(1000):
    population = df.deplacement_avec_stresse(population,box)
    plt.clf()
    plt.xlim(-5,box.x_max+5)
    plt.ylim(-5,box.y_max+5)
    plt.scatter(population.x,population.y,color='green', s=population.taille)
    plt.pause(0.01)

plt.show()
