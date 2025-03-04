import matplotlib.pyplot as plt
from itertools import product
import matplotlib
matplotlib.use('Agg')

def check_if_word_is_locally_bounded(n,word, l, delta):
    'iterate over all the windows'
    for i in range(n - l + 1):
        window = word[i:i+l]
        'check the current window'
        if sum(window) > l // 2 - delta:
            return False
    return True

def count_amount_of_n_l_delta_locally_bounded_codes(n, l, delta):
    vectors_counter = 0
    'iterate over all possible n sized vectors'
    for word in product([0, 1], repeat=n):
        if check_if_word_is_locally_bounded(n,word, l, delta):
            vectors_counter += 1
    return vectors_counter

# the identification function
def calculate_L_n_r_l_delta(n, r, l, delta):
    if count_amount_of_n_l_delta_locally_bounded_codes(n+r, l, delta) >= 2**n:
        return 1
    return 0

# the main function. l in relation to r
def calulate_f_n_delta(n, delta, r):
    for l in range(2*delta, n+3):
        if calculate_L_n_r_l_delta(n, r, l, delta) > 0:
            return l
    return None

# plotting the graphs
def plot_graphs(n, delta_values, r_values):
    plt.figure(figsize=(10, 6))

    for delta in delta_values:
        l_values = [calulate_f_n_delta(n, delta, r) for r in r_values]
        plt.plot(r_values, l_values, marker='o', linestyle='-', label=f'delta={delta}')

    plt.xlabel('r values')
    plt.ylabel('l values')
    plt.title(f'Graph of l vs r for fixed n={n} and multiple delta values')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plot_N={n}.png")

# Example Usage
if __name__ == '__main__':
    n = int(input("Enter n: "))
    delta_values = list(map(int, input("Enter delta values (comma-separated): ").split(',')))
    r_values = range(1, 10)

    plot_graphs(n, delta_values, r_values)

