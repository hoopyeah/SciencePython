from pylab import *

y_list = [.3, .36, .49, .63, .7]
m_list = []
for y in y_list:
    m_1 = 1 + (.6962 * y ** 2) / (y ** 2 - .0684 ** 2) + (.4079 * y ** 2) / (y ** 2 - .1162 ** 2) + (.8975 * y ** 2) / (y ** 2 - 9.8962 ** 2)
    print str(y) + ': ' + str(math.sqrt(m_1))
    m_list.append(math.sqrt(m_1))
    
plot(y_list, m_list)
lam = r'$\lambda$'
mu = r'$\mu$'
n = r'$n$'
xlabel('wavelength ' + lam + ' (' + mu + 'm)')
ylabel('refractive index ' + n)
title('Application of Sellmeier Equation for Fused Silica')
grid(True)
savefig("/Users/hoopyeah/Desktop/test.png")
show()