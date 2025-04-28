def recursive_nth_fibo(idx):
    if idx == 0 or idx == 1:
        return idx
    else:
        return recursive_nth_fibo(idx - 1) + recursive_nth_fibo(idx - 2)

def main(number):
    print(recursive_nth_fibo(number))
    posloupnost = []
    for num in range(number + 1):
        n = recursive_nth_fibo(num)
        posloupnost.append(n)
    return print(posloupnost)


if __name__ == "__main__":
    main(5)
