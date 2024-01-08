def mult(arr):
    result = 1
    for num in arr:
        result *= int(num)

    return result


def div(arr):
    result = int(arr[0])
    for i in range(1,len(arr)):
        result = result / int(arr[i])

    return result


def ad(arr):
    result = 0
    for num in arr:
        result += int(num)

    return result


def sub(arr):
    result = int(arr[0])
    for i in range(1,len(arr)):
        result = result - int(arr[i])

    return result

