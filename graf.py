import pylab as pl
from pylab import pi

f = 50
t = pl.linspace(0, 0.05, 444)

u = 3.3 * pl.cos(2*pi*f*t)
i = 2.2 * pl.cos(2*pi*f*t + pi/4)

pl.plot(t, u, 'g:', label='napětí', color="#123456")
pl.plot(t, i, 'b-.',label='proud', linestyle='-.')
pl.plot(t, u*i, 'rx', label='výkon')

pl.grid(1)
pl.title('Výkon střídavéo proudu')
pl.xlabel('t [s]')
pl.ylabel('u(t), i(t), p(t)')
pl.legend(loc='upper right')

pl.xlim(0, 0.02)

pl.show()