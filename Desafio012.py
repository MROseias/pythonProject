pi = float(input('Qual é o preço do produto?R$'))
promo = 5/100
desc = pi-(promo*pi)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pi, desc))
