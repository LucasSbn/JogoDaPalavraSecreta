# lucas o Maior

cpf_enviado = '74682489070'
nove_digitos = cpf_enviado[0:9]
contador_regressivo_1 = 10
resultado_digito = 0
for numero_1  in nove_digitos:
    resultado_digito += (int(numero_1)) * contador_regressivo_1
    contador_regressivo_1 -= 1
numero_1 = (resultado_digito * 10 % 11)

numero_1 = numero_1 if numero_1 <= 9 else 0

dez_digitos = nove_digitos + str(numero_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for numero_2 in dez_digitos:
    resultado_digito_2 += int(numero_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
numero_2 = (resultado_digito_2 * 10 % 11)
numero_2 = numero_2 if numero_2 <= 9 else 0


