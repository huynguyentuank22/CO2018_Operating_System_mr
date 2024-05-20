import matplotlib.pyplot as plt


def plot_result(hit_ratio, ref_str):
    # Plotting the data
    plt.figure(figsize=(10, 6))

    plt.plot(ref_str, hit_ratio['DCLL'], label='Doubly Circular LL', marker='o')
    plt.plot(ref_str, hit_ratio['SplayTree'], label='Splay Tree', marker='s')
    plt.plot(ref_str, hit_ratio['BitUsed'], label='Bit Used', marker='^')

    # Adding titles and labels
    plt.title('Hit Ratios of LRU Structures vs. Length of Reference Strings')
    plt.xlabel('Length of Reference String')
    plt.ylabel('Hit Ratio')
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()