import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.2)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x,y1,'o',linewidth=3,color=(0.2,0.1,0.4))
plt.hold(True)
plt.plot(x,y2,'-',linewidth=2,color='g')
plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lab DLS')
plt.show()