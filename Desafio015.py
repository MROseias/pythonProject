da = int(input('Quantos dias Alugados?'))
km = float(input('Quantos km rodados?'))
cust = (60*da) + (0.15*km)
print('O total a pagar é R${:.2f}'.format(cust))
