import matplotlib.pyplot as plt

def plot_result(hit_ratio, ref_str, cache_size, type, sz_ref_str):
    # Plotting the data
    plt.figure(figsize=(10, 6))

    plt.plot(ref_str, hit_ratio['DCLL'], label='Doubly Circular LL', marker='o')
    plt.plot(ref_str, hit_ratio['SplayTree'], label='Splay Tree', marker='s')
    plt.plot(ref_str, hit_ratio['BitUsed'], label='Bit Used', marker='^')
    plt.plot(ref_str, hit_ratio['SkipList'], label='Skip List', marker='x')

    # Adding titles and labels
    plt.title('Hit Ratios of LRU Structures with cache size = ' + str(cache_size) + ' for ' + type + ' trace')
    plt.xlabel('Number of page references')
    plt.xticks(sz_ref_str)
    plt.ylabel('Hit Ratio (%)')
    plt.legend()

    # Display the plot
    plt.grid(True, axis = 'y')
    plt.show()