from sympy import symbols, tan, sin, cos, log, lambdify
from random import uniform


def task1() -> None:
    x = symbols("x", real=True)
    gxs = (1 + tan(log(3.2 * x ** 2 - sin(x))) ** 2) * ((6.4 * x - cos(x)) / (3.2 * x ** 2 - sin(x)))
    gx = lambdify(x, gxs, "numpy")

    a = 1.57
    b = 5.4
    N = 150000

    integral = 0
    for _ in range(N):
        integral += gx(uniform(a, b))

    result = (b - a) / N * integral
    print(f"Результат: {result:.7f}")


def task2() -> None:
    x, y = symbols("x, y", real=True)
    Fxys = 3 ** 3 - 5.12 * x ** 2 + 6.3747 * x - 0.186660 - sin(0.52359878 * y - 0.56025069)
    Fxy = lambdify((x, y), Fxys, "numpy")

    delta = 0.01
    x_range = (0, 7)
    y_range = (0, 4)
    As = [
        (1, 2, 0, 3),
        (3, 7, 1, 4),
    ]
    S = 0
    for A in As:
        w = A[1] - A[0]
        h = A[3] - A[2]
        S += w * h

    N = int(S / (delta ** 2))

    print(f"Загальна площа: {S}")
    print(f"Число точок: {N}")

    min_value = float("inf")
    min_point = (None, None)
    for i in range(N):
        xi, yi = (0, 0)
        valid_point = False
        while not valid_point:
            xi, yi = uniform(*x_range), uniform(*y_range)
            for A in As:
                if A[0] < xi < A[1] and A[2] < yi < A[3]:
                    valid_point = True
                    break

            if valid_point:
                break

        value = Fxy(xi, yi)
        if value < min_value:
            min_value = value
            min_point = (xi, yi)

    print(f"Мінімум функції: {min_value:.7f} у точці ({min_point[0]:.7f}, {min_point[1]:.7f})")


def main() -> None:
    print("Завдання 1")
    task1()

    print("\nЗавдання 2")
    task2()


if __name__ == '__main__':
    main()
