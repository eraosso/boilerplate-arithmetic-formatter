def arithmetic_arranger(problems):
    arranged_problems = ""
    resultado = ""
    resolve = None

    if isinstance(problems, list):
        if isinstance(problems[0], list) and len(problems) == 2:
            resolve = problems[1]
            problems = problems[0]
        else:
            if isinstance(problems[0], list):
                problems = problems[0]
                resolve = False

    if len(problems) > 5:
        return "Error: Too many problems."

    for problema in problems:
        conta = problema.split()
        if conta[1] not in {"+", "-"}:
            return "Error: Operator must be '+' or '-'."
        if not(conta[0].isnumeric()) or not(conta[2].isnumeric()):
            return "Error: Numbers must only contain digits."
        if (len(conta[0]) > 4) | (len(conta[2]) > 4):
            return "Error: Numbers cannot be more than four digits."

    qty = len(problems)

    op = {'+': lambda x, y: int(x) + int(y), '-': lambda x, y: int(x) - int(y)}

    def tamanho(l1, l2):
        if l1 >= l2:
            return l1
        else:
            return l2

    primeiro = []
    operacao = []
    segundo = []

    for problema in problems:
        primeiro.append(problema.split()[0])
        operacao.append(problema.split()[1])
        segundo.append(problema.split()[2])

    primeira_linha = ""
    segunda_linha = ""
    dashes = ""
    resultado = ""
    for i in range(qty):
        l1 = len(primeiro[i])
        l2 = len(segundo[i])
        n_chars = tamanho(l1, l2)
        primeira_linha += (" " * (n_chars + 2 - l1) + primeiro[i] + 4 * " ")
        segunda_linha += operacao[i] + (" " * (n_chars + 1 - l2) + segundo[i] + 4 * " ")

        dashes += "-" * (n_chars + 2) + " " * 4
        conta = str(op[operacao[i]](primeiro[i], segundo[i]))
        resultado += (" " * (n_chars + 2 - len(str(conta))) + conta + 4 * " ")

    primeira_linha = primeira_linha[:-4] + "\n"
    segunda_linha = segunda_linha[:-4] + "\n"
    dashes = dashes[:-4]
    resultado = resultado[:-4]

    if resolve:
        arranged_problems = primeira_linha + segunda_linha + dashes + "\n" + resultado
    else:
        arranged_problems = primeira_linha + segunda_linha + dashes

    return arranged_problems


