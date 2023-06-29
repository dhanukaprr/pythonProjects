import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    start_num = int(start_entry.get())
    end_num = int(end_entry.get())
    num_list = []

    while start_num <= end_num:
        sqr = start_num * start_num
        print(sqr)
        start_num += 1
        num_list.append(sqr)

    highest = max(num_list)
    xaxis = list(range(1, len(num_list) + 1))

    x = np.array(xaxis)
    y = np.array(num_list)

    plt.plot(x, y)
    plt.show()

# Create the main window
window = tk.Tk()
window.title("Number Plotter")

# Create labels and entry fields for user input
start_label = tk.Label(window, text="Enter starting number:")
start_label.pack()
start_entry = tk.Entry(window)
start_entry.pack()

end_label = tk.Label(window, text="Enter ending number:")
end_label.pack()
end_entry = tk.Entry(window)
end_entry.pack()

# Create a button to generate the plot
plot_button = tk.Button(window, text="Generate Plot", command=generate_plot)
plot_button.pack()

# Run the GUI main loop
window.mainloop()
