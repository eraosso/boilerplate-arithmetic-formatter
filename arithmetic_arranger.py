def arithmetic_arranger(problems):
    arranged_problems = ""
    resultado = ""

    if isinstance(problems, tuple):
        problems, resolve = problems

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

    op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}


    for i in range(qty):
        primeiro = problems[i].split()[0]
        segundo = problems[i].split()[2]
        operacao = problems[i].split()[1]

        arranged_problems += (' ' * (5 - len(primeiro)) + primeiro + ' ' * 4 * ())
        # temp = op[operacao](primeiro, segundo)
        # resultado += (' ' * (5 - len(str(temp))) + str(temp) + ' ' * 4)

    arranged_problems += "\n"

    for i in range(qty):
        arranged_problems += (problems[i].split()[1] + ' ' * (4 - len(problems[i].split()[2])) + problems[i].split()[
            2] + " " * 4)
    arranged_problems += "\n"

    for i in range(qty):
        arranged_problems += ("-" * 5 + " " * 4)

    if resolve:
        arranged_problems += "\n"+ resultado

    return arranged_problems
