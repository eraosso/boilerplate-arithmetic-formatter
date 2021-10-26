def arithmetic_arranger(problems):
    arranged_problems = ""
    resultado = ""

    if len(problems[0]) > 5:
        return "Error: Too many problems."

    for problema in problems[0]:
        conta = problema.split()
        if conta[1] not in {"+", "-"}:
            return "Error: Operator must be '+' or '-'."
        if not(conta[0].isnumeric()) or not(conta[2].isnumeric()):
            return "Error: Numbers must only contain digits."
        if (len(conta[0]) > 4) | (len(conta[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
    
    qty = len(problems[0])

    op = {'+': lambda x, y: int(x) + int(y), '-': lambda x, y: int(x) - int(y)}

    primeiro = []
    operacao = []
    segundo = []

    for problema in problems[0]:
        primeiro.append(problema.split()[0])
        operacao.append(problema.split()[1])
        segundo.append(problema.split()[2])

    primeira_linha = ""
    segunda_linha = ""
    dashes = ""
    resultado = ""
    for i in range(qty):
        primeira_linha += (" " * (5 - len(primeiro[i])) + primeiro[i] + 4 * " ")
        segunda_linha += operacao[i] + (" " * (5 - len(segundo[i])) + segundo[i] + 4 * " ")
        dashes += "-" * 5 + " " * 4
        conta = str(op[operacao[i]](primeiro[i], segundo[i]))
        resultado += (" " * (5 - len(str(conta))) + conta + 4 * " ")

    primeira_linha = primeira_linha[:-4] + "\n"
    segunda_linha = segunda_linha[:-4] + "\n"
    dashes = dashes[:-4]
    resultado = resultado[:-4]

    if len(problems) == 2:
        problems, resolve = problems
        if resolve:
            arranged_problems = primeira_linha + segunda_linha + dashes + "\n" + resultado
    else:
        arranged_problems = primeira_linha + segunda_linha + dashes

    return arranged_problems

