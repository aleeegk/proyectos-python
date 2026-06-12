def paper_fold():
    i = 1
    while True:
        # El truco binario para calcular el bit de la curva del dragón en O(1)
        yield 1 if ((i & -i) << 1) & i == 0 else 0
        i += 1