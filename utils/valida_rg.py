import re


def valida_rg():
    # Regex para RG com 7 dígitos sem dígito verificador: ex. 2345674
    regex_rg_7_digitos = r'^\d{7}$'

    # Regex para RG com 9 dígitos com dígito verificador, ex: 12.345.678-9
    regex_rg_9_digitos = r'^\d{2}\.\d{3}\.\d{3}-\d$'

    # Combina as duas regex usando o pipe | (ou)
    regex_rg_completo = f'{regex_rg_7_digitos}|{regex_rg_9_digitos}'

    while True:
        rg = input('Informe o RG (ou digite "sair" para encerrar): ')

        if rg.lower() == 'sair':
            break

        # Verifica o RG usando a variável com o regex completo
        if re.match(regex_rg_completo, rg):
            print(f'O RG digitado foi: {rg} e o número é VÁLIDO.')
        else:
            print(f'O RG digitado foi {rg} é o número é INVÁLIDO. Tente novamente.')


if __name__ == "__main__":
    valida_rg()


# Testando a validação de 'rg':

# rg_1 = '58651220'
# rg_2 = '11.756.677-1'
# rg_3 = '543765098'
# rg_4 = '22376515'
# rg_5 = '32532859328434'
#
# validar_rg(rg_1)
# validar_rg(rg_2)
# validar_rg(rg_3)
# validar_rg(rg_4)
# validar_rg(rg_5)
