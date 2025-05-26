from decimal import Decimal, getcontext

# Set the precision to 300 digits
getcontext().prec = 300


def calculate_pi():
    """Calculate pi to 300 digits using the Chudnovsky algorithm."""
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, 100):
        M = (K**3 - 16 * K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi


if __name__ == "__main__":
    pi_value = calculate_pi()
    print(f"First 300 digits of pi:\n{pi_value}")
