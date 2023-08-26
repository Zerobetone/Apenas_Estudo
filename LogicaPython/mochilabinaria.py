
def maxValue(capacidade, items):
    n = len(items)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso = items[i - 1]["peso"]
        valor = items[i - 1]["valor"]
        for w in range(capacidade + 1):
            if peso <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso] + valor)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

lista = []
item1 = {"valor": 1, "peso": 60}
item2 = {"valor": 2, "peso": 100}
item3 = {"valor": 3, "peso": 120}

lista.append(item1)
lista.append(item2)
lista.append(item3)

capacidade = 200

print(maxValue(capacidade, lista))