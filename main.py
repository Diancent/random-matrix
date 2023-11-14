import numpy as np

if __name__ == '__main__':

    possible_values = np.append(np.arange(1, 11), np.nan)
    random_array = np.random.choice(possible_values, size=(10, 10), replace=True)

    mask = np.isnan(np.diag(random_array))
    random_array[mask, mask] = -1

    print(random_array)