


def power(num, pow):
    if pow <= 0:
        return 1
    elif pow == 1:
        return num
    else:
        result = power(num, pow // 2)
        # if power is even:
        if pow % 2 == 0:
            return result * result
        else:
            return num * result * result
