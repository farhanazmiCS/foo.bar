# Solution "Power Hungry"
def solution(x):
    x.sort()
    def product(x):
        if len(x) == 0:
            return 1
        elif len(x) == 1:
            return x[0]
        else:
            # Even Array
            if len(x) % 2 == 0:
                if x[0] * x[1] > 0:
                    return x[0] * x[1] * product(x[2:len(x)])
                else:
                    if len(x) == 2:
                        return x[1]
                    return product(x[1:len(x)])
            # Odd Array
            else:
                if x[0] * x[1] * x[2] > 0:
                    return x[0] * x[1] * x[2] * product(x[3:len(x)])
                elif x[0] * x[1] > 0:
                    if len(x) == 3:
                        return x[0] * x[1]
                    return x[0] * x[1] * product(x[2:len(x)])
                else:
                    return product(x[1:len(x)])
    return str(product(x))