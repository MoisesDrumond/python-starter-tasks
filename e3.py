import time
price = float(input('Qual e o preço do produto? R$'))
estilo = ' FORMAS DE PAGAMENTO '
print(f'{estilo:=^40}')
print("""[1] a vista dinheiro/cheque
[2] a vistao cartao
[3] 2x no cartao
[4] 3x ou mais no cartao""")
time.sleep(1)
payterm = int(input('Qual e a forma de pagamento?'))
if payterm == 1:
    totalprice = price - (price * 10)/100
elif payterm == 2:
    totalprice = price - (price * 5)/100
elif payterm == 3:
    totalprice = price
    parcela = totalprice / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f}.')
elif payterm == 4:
    totalprice = price + (price * 20)/100
    parcelatotal = int(input('Quantas parcelas?'))
    parcela = totalprice / parcelatotal
    print(f'Sua compra sera parcelada em {parcelatotal} de R${parcela:.2f}.')
else:
    total = price
    print('\033[1;31;40mOPCAO INVALIDA de pagamento. Tente novamente!\033[m')
print(f'Sua compra de R${price:.2f} vai custar R${totalprice:.2f} no final.')
