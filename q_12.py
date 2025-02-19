horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor da hora: "))
desconto = float(input("Digite o valor do desconto: "))
brut = horas * valor
liq = brut - desconto
print("O salário líquido é: ", liq)
print("O salário bruto é: ", brut)
print("O desconto foi de: ", brut % desconto)