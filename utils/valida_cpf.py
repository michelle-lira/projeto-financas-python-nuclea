from validate_docbr import CPF


def valida_cpf():

    cpf_validador = CPF()

    while True:
        cpf = input('Informe o CPF ou digite "sair" para encerrar: ')
        resultado_validacao = cpf_validador.validate(cpf)

        if cpf.lower() == 'sair':
            break

        if resultado_validacao:
            cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
            print(f'O CPF digitado foi: {cpf_formatado} e o número é VÁLIDO.')
        else:
            print(f'O CPF digitado foi: {cpf} e o número é INVÁLIDO.')


# def gera_cpf():
#     cpf = CPF()
#     cpf_gerado = cpf.generate()
#     return cpf_gerado


if __name__ == "__main__":
    valida_cpf()


# Testando a validação de 'cpf':

# cpf1 = "123.345.675-33"  # Saída: CPF 123.345.675-33 é válido.
# cpf2 = "112.345.544-00"  # Saída: CPF 112.345.544-00 é válido.
# cpf3 = "111.222.333-44"  # Saída: CPF 111.222.333-44 é válido.
# cpf4 = "111.111.111-11"  # Saída: CPF 111.111.111-11 é inválido.
# cpf5 = "123.345.675"  # Saída: CPF 123.345.675 é inválido.

# validar_cpf(cpf1)
# validar_cpf(cpf2)
# validar_cpf(cpf3)
# validar_cpf(cpf4)
# validar_cpf(cpf5)
