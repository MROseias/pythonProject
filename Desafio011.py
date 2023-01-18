Largura = float(input('Largura da parede:'))
Altura = float(input('Altura da parede:'))
area = Largura * Altura
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}'.format(Largura, Altura, area))
print('Para pintar essa parede, você precisará de {:.3f}litros de tinta'.format(area/2))
