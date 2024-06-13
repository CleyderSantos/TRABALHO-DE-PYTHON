import tkinter as tk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        
        self.label_height = tk.Label(root, text="Altura (m):")
        self.label_height.pack()
        
        self.entry_height = tk.Entry(root)
        self.entry_height.pack()
        
        self.label_weight = tk.Label(root, text="Peso (kg):")
        self.label_weight.pack()
        
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()
        
        self.calculate_button = tk.Button(root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.pack()
        
        self.label_result = tk.Label(root, text="")
        self.label_result.pack()
    
    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            
            bmi = weight / (height ** 2)
            self.show_bmi_category(bmi)
        except ValueError:
            self.label_result.config(text="Erro: Insira valores numéricos para altura e peso.")
    
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            category = "Peso normal"
        elif 25 <= bmi < 30:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        self.label_result.config(text="IMC: {:.2f} ({})".format(bmi, category))

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()