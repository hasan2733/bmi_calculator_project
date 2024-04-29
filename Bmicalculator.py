import tkinter as tk


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        height_meters = height * 0.0254
        bmi_value = weight / (height_meters ** 2)

        result_var.set(f"Your BMI: {bmi_value:.2f}")

        if bmi_value < 18.5:
            category_var.set("You are underweight")
        elif 18.5 <= bmi_value <= 24.9:
            category_var.set("Normal weight")
        elif 25.0 <= bmi_value <= 29.9:
            category_var.set("You are overweight")
        elif 30.0 <= bmi_value <= 34.9:
            category_var.set("Obesity class 1")
        elif 35.0 <= bmi_value <= 39.9:
            category_var.set("Obesity class 2")
        elif bmi_value >= 40:
            category_var.set("Obesity class 3")
    except ValueError:
        result_var.set("Invalid input")
        category_var.set("")


def clear_inputs():
    weight_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    result_var.set("")
    category_var.set("")
# Create the main window


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("420x420")
window.config(background="#EDE4F3")

icon = tk.PhotoImage(file='bmi icon.png')
window.iconphoto(True, icon)

# Create and place widgets in the window
weight_label = tk.Label(window, text="Enter your weight in KG:", height=3, font=('Arial', 12), bg="#EDE4F3", fg="black")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window, font=('Arial', 12), fg="#1A1121")
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(window, text="Enter your height in Inch:", height=3,
                        font=('Arial', 12),
                        bg="#EDE4F3", fg="black")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(window, font=('Arial', 12), fg="#1A1121")
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate BMI",
                             font=('Arial', 12), bg="#EDE4F3",
                             fg="black", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=('Arial', 12), fg="#1A1121")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

category_var = tk.StringVar()
category_label = tk.Label(window, textvariable=category_var, font=('Arial', 12), fg="#1A1121")
category_label.grid(row=4, column=0, columnspan=2, pady=10)

clear_button = tk.Button(window, text="Clear", font=('Arial', 12), bg="#EDE4F3", fg="black", command=clear_inputs)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)
# Run the main loop
window.mainloop()
