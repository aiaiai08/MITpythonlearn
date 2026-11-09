import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.2 )
y1 = np.sin(x)
y2 = np.cos(x)
plt.style.use('ggplot')
plt.subplot(211)

plt.plot(x,y1,label='sin')

plt.subplot(212)
plt.plot(x,y2,label='cos')
plt.plot(x,y1,label='sin')
plt.legend(loc='upper right')
plt.show()

