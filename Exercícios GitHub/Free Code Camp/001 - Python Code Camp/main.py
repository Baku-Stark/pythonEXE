import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

def arithmetic_arranger(problems, solver=False):
    if len(problems) > 5:
        return "\033[31m Error: Too many problems.\033[m"

    toptier = ""
    bottomtier = ""
    lines = ""
    totals = ""

    for n in problems:
        fnumber = n.split()[0]
        operator = n.split()[1]
        snumber = n.split()[2]

        if operator != "+" and operator != "-":
            return "\033[31m Error: Operator must be '+' or '-'.\033[m"

        if not fnumber.isdigit() or not snumber.isdigit():
            return "\033[31m Error: Numbers must only contain digits.\033[m"

        if len(fnumber) > 4 or len(snumber) > 4:
            return "\033[31m Error: Numbers cannot be more than four digits.\033[m"

        total = ops[operator](int(fnumber), int(snumber))
        operatorDistance = max(len(fnumber), len(snumber)) + 2

        snumber = operator + snumber.rjust(operatorDistance - 1)
        toptier = toptier + fnumber.rjust(operatorDistance) + (4 * " ")

        bottomtier = bottomtier + snumber + (4 * " ")
        lines = lines + len(snumber) * "_" + (4 * " ")
        totals = totals + str(total).rjust(operatorDistance) + (4 * " ")

    if solver:
        print(toptier)
        print(operator)
        print(bottomtier)
        print(lines)
        print(totals)

if __name__ == "__main__":
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])