si = float(input('Qual é o salário do Funcionário? R$'))
sf = (si*(15/100))+si
print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber{:.2f}'.format(si, sf))
