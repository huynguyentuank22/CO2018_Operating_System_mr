import matplotlib.pyplot as plt
import numpy as np

class Memory():
    
    def memory_consumption():
        initial_megas = int(input("Enter the initial amount of megabytes: "))
        n_days = int(input("Enter the number of days: "))
        average_megas = int(input("Enter the average user memory consumption: "))
        days = []
        memory = []
        for i in range(n_days):
            print("Day " + str(i+1) + ", available storage: " +\
                         str(initial_megas) + " megabytes")
    
            if initial_megas < 28000:
                added_megas = initial_megas * 0.4
                initial_megas = initial_megas + (added_megas) - average_megas
                print("Added " + str(added_megas) + " more to the memory and subtracted " + str(average_megas) +\
                      " so now we have " + str(initial_megas) + " memory on day " + str(i+1))
                days.append(i+1)
                memory.append(initial_megas)
            else:
                added_megas = initial_megas * 0.31
                initial_megas = initial_megas + (added_megas) - average_megas
                print("Added " + str(added_megas) + " more to the memory and subtracted " + str(average_megas) +\
                      " so now we have " + str(initial_megas) + " memory on day " + str(i+1))
                days.append(i+1)
                memory.append(initial_megas)
        
        return days, memory
    
    def plot(days_history, memory_history, annot=False):
        fig, ax = plt.subplots(figsize=(10,5), dpi=100)
        ax.set_title('History of days vs available memory')
        ax.set_xlabel('Number of days')
        ax.set_ylabel('Available Memory')
        ax = plt.scatter(days_history, memory_history, s=100)
        if annot:
            for i, txt in enumerate(memory_history):
                plt.annotate(txt, (days_history[i], memory_history[i]))
        plt.show()
    
    def model():
        megas = int(input("Enter the memory consumption in megabytes: "))
        memory = 1
        percentage_value = 1
        
        while percentage_value < megas:
            if memory < 28000:
                percentage_value = memory * 0.4
                memory += 1

            else:
                percentage_value = memory * 0.31
                memory += 1        
        return memory
    
    def X_y(n):
        megas = np.random.randint(3000, 10000, n)
        y = []
        
        for i in range(len(megas)):
            memory = 1
            percentage_value = 1
        
            while percentage_value < megas[i]:
                if memory < 28000:
                    percentage_value = memory * 0.4
                    memory += 1

                else:
                    percentage_value = memory * 0.31
                    memory += 1
            
            y.append(memory)
            
        
        return megas, y
