import deplacement_final as df
import class_algue as cla 
import matplotlib.pyplot as plt
import settings as config
import aggregat as aggr


box = cla.Box(config.X_MAX,config.Y_MAX)
population = cla.Population(config.taille_max,box)
plt.xlim(-5,box.x_max+5)
plt.ylim(-5,box.y_max+5)
plt.scatter(population.x,population.y, s=population.taille)
aggregat = []
for i in range(1000):
    aggr.update_aggregat(population,aggregat)
    population = df.deplacement_sans_stresse(population,box)
    aggr.deplacement_aggregat(population, box, aggregat)
    plt.clf()
    plt.xlim(-5,box.x_max+5)
    plt.ylim(-5,box.y_max+5)
    plt.scatter(population.x,population.y,color='green', s=population.taille)
    plt.pause(0.1)
plt.show()
