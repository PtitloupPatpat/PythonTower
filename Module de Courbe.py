import numpy as np
import matplotlib.pyplot as plt


t=[x/2 for x in range(100)]

e=[x for x in range(100)]
s=[2*x for x in range(100)]
p=np.polyfit(t,e,1)
q=np.polyfit(t,s,1)

plt.figure(1)
plt.errorbar(t, e, fmt='x')
plt.errorbar(t, s, fmt='o')
plt.plot(t, np.polyval(p, t), '--')
plt.plot(t, np.polyval(q, t), '-')
plt.xlabel('temps en secondes')
plt.ylabel('signal d\'entrée(x) et de sortie réel(o)')
plt.title('filtre passe bas')
plt.grid()
plt.show()