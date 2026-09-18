#Valida o tipo de residência (Entrada)
print('Calculadora de consumo')
print('Qual é o tipo de sua residência? ')

residencia = input('Apartamento, Casa ou Comercial? ')

while True:
    if residencia.lower() in ['apartamento', 'casa', 'comercial']:
        break
    else:
        print('Por favor, digite um tipo de residência válido.')
        residencia = input('Apartamento, Casa ou Comercial? ')

#Valida o consumo de água (Processamento)
while True:
    try:
        consumo = float(input('Digite o consumo em metros cúbicos (m³): ').replace(',', '.'))
        if consumo < 0:
            print('Consumo não pode ser negativo. Tente novamente.')
            continue
        break
    except ValueError:
        print('Digite um número válido.')

if residencia.lower() == 'comercial':
    print('Tarifa comercial aplicada – consulte o plano corporativo.')

elif residencia.lower() == 'apartamento' and consumo < 10:
    print('Consumo econômico – excelente controle de água!')

elif (residencia.lower() == 'apartamento' or residencia.lower() == 'casa') and consumo <= 25:
    print('Consumo moderado – dentro do padrão residencial.')

else:
    print('Consumo excessivo – adote medidas de economia e verifique vazamentos.')

#Encerra o programa (Saída)
print('Obrigado por utilizar a calculadora de consumo!, pode fechar o programa.')