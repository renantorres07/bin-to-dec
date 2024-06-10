def is_valid_binary(binary_str):
    """ Verifica se a string fornecida contém apenas '0' e '1'. """
    for char in binary_str:
        if char not in ('0', '1'):
            return False
    return True


def binary_to_decimal(binary_str):
    """ Converte uma string binária em seu equivalente decimal. """
    decimal_value = 0
    length = len(binary_str)
    for i, digit in enumerate(binary_str):
        # Calcula o valor decimal usando a potencia de 2
        decimal_value += int(digit) * (2 ** (length - i - 1))
    return decimal_value


def main():
    # Receber a entrada do usuário
    binary_str = input("Digite um número binário: ")

    if not is_valid_binary(binary_str):
        print("Erro: Entrada inválida. Por favor, insira apenas 0s e 1s.")
        return

    # Converter binário para decimal
    decimal_value = binary_to_decimal(binary_str)

    # Exibir o resultado
    print(f"O valor decimal de {binary_str} é {decimal_value}")


if __name__ == "__main__":
    main()
