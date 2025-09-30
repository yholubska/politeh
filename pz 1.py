import math
import traceback

def read_int(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt)
        try:
            v = int(s)
        except Exception:
            print("Невірне ціле число. Спробуйте ще раз.")
            continue
        if min_val is not None and v < min_val:
            print(f"Число має бути >= {min_val}.")
            continue
        if max_val is not None and v > max_val:
            print(f"Число має бути <= {max_val}.")
            continue
        return v

def read_float(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except Exception:
            print("Невірне дійсне число. Спробуйте ще раз.")


def task1():
    surname = "Голубська"
    name = "Ярина"
    year = 2008

    print(f"{surname} {name}, {year} р. н.")
    print(f"Прізвище: {surname}")
    print(f"Ім’я: {name}")
    print(f"Рік народження: {year}")


def task2():
    a = read_int("Введіть число a (ціле): ")
    b = read_int("Введіть число b (ціле): ")

    print("Сума:", a + b)
    print("Різниця:", a - b)
    print("Добуток:", a * b)
    print("Середнє арифметичне:", (a + b) / 2.0)

    prod = a * b
    if prod < 0:
        print("Середнє геометричне: не визначено (добуток від'ємний).")
    else:
        print("Середнє геометричне:", math.sqrt(prod))

    print("Відстань:", abs(a - b))
    print("Максимум:", max(a, b))
    print("Мінімум:", min(a, b))
    print("Сума квадратів:", a**2 + b**2)
    print("Квадрат суми:", (a + b)**2)
    try:
        print("a^b:", a**b)
    except OverflowError:
        print("a^b: переповнення (число надто велике).")


def task3():
    while True:
        num = read_int("Введіть 4-значне число (можна з провідними нулями не вказувати): ")
        if 1000 <= abs(num) <= 9999:
            break
        print("Число не є 4-значним. Спробуйте ще раз (або введіть число від 1000 до 9999).")
    digits = [int(d) for d in str(abs(num))]
    print(" + ".join(str(d) for d in digits), "=", sum(digits))


def task4():
    a = read_float("Введіть a: ")
    b = read_float("Введіть b: ")
    c = read_float("Введіть c: ")

    if abs(a) < 1e-12:
        if abs(b) < 1e-12:
            if abs(c) < 1e-12:
                print("Нескінченна кількість розв'язків (0 = 0).")
            else:
                print("Рівняння не має розв'язків (0*x + 0 = c, c != 0).")
        else:
            x = -c / b
            print(f"Лінійне рівняння, x = {x:.2f}")
        return

    D = b**2 - 4*a*c
    if D < 0:
        print("Дійсних коренів немає.")
    elif abs(D) < 1e-12:
        x = -b / (2*a)
        print(f"Подвійний корінь: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")


def task5():

    print("Формула 1: s = s0 + v0*t + 1/2*g*t^2")
    s0 = read_float("Введіть s0: ")
    v0 = read_float("Введіть v0: ")
    t = read_float("Введіть t: ")
    g = 9.81
    s = s0 + v0 * t + 0.5 * g * t**2
    print("s =", s)

    print("\nФормула 2: FV = PV * (1 + INT/100)^YRS")
    PV = read_float("Введіть PV (початкова сума): ")
    INT = read_float("Введіть INT (річний відсоток): ")
    YRS = read_int("Введіть YRS (кількість років, ціле): ", min_val=0)
    FV = PV * (1 + INT / 100) ** YRS
    print("FV =", FV)

    print("\nФормула 3: G = (4 * pi^2 * a^3) / (p^2 * (m1 + m2))")
    a = read_float("Введіть a: ")
    p = read_float("Введіть p: ")
    m1 = read_float("Введіть m1: ")
    m2 = read_float("Введіть m2: ")
    if abs(p) < 1e-12 or abs(m1 + m2) < 1e-12:
        print("Помилка: p або (m1 + m2) занадто близькі до нуля — неможливо обчислити формулу.")
    else:
        G = (4 * math.pi**2 * a**3) / (p**2 * (m1 + m2))
        print("G =", G)

    print("\nФормула 4: c = sqrt(a^2 + b^2 - 2ab*cos(gamma))")
    a2 = read_float("Введіть a: ")
    b2 = read_float("Введіть b: ")
    gamma_deg = read_float("Введіть γ в градусах: ")
    val = a2**2 + b2**2 - 2 * a2 * b2 * math.cos(math.radians(gamma_deg))
    if val < -1e-12:
        print("Підкореневий вираз від'ємний: неможливо взяти дійсний квадратний корінь.")
    else:
        c = math.sqrt(max(0.0, val))
        print("c =", c)


def task6():
    x = read_float("Введіть дійсне число: ")
    frac = x - math.floor(x)
    print("Дробова частина:", frac)


def task7():
    a = read_int("Введіть число a (1..1000): ", min_val=1, max_val=1000)
    b = read_int("Введіть число b (1..1000): ", min_val=1, max_val=1000)
    maximum = (a + b + abs(a - b)) // 2
    print("Максимальне число:", maximum)


def main():
    tasks = {
        1: ("Завдання 1 (ПІ)", task1),
        2: ("Завдання 2 (операції над a і b)", task2),
        3: ("Завдання 3 (сума цифр 4-значного числа)", task3),
        4: ("Завдання 4 (квадратне рівняння)", task4),
        5: ("Завдання 5 (формули)", task5),
        6: ("Завдання 6 (дробова частина)", task6),
        7: ("Завдання 7 (максимум без розгалужень)", task7),
    }

    while True:
        print("\nОберіть завдання (1-7) або 0 для виходу:")
        for k, (desc, _) in tasks.items():
            print(f"{k}: {desc}")
        print("0: Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            print("До побачення!")
            break
        try:
            ci = int(choice)
            if ci in tasks:
                try:
                    tasks[ci][1]()
                except Exception:
                    print("Під час виконання завдання сталася помилка:")
                    traceback.print_exc()
            else:
                print("Невірний номер завдання.")
        except ValueError:
            print("Введіть, будь ласка, число від 0 до 7.")


if __name__ == "__main__":
    main()
