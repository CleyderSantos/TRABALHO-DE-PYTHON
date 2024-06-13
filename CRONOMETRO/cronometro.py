import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Parar", command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Resetar", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.start_time = None

    def update_time(self):
        if self.running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            total_seconds = int(elapsed_time)
            self.hours, rem = divmod(total_seconds, 3600)
            self.minutes, self.seconds = divmod(rem, 60)

            time_string = "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)
            self.label.config(text=time_string)
            self.root.after(1000, self.update_time)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.seconds - self.minutes*60 - self.hours*3600
            self.update_time()

    def stop_stopwatch(self):
        self.running = False

    def reset_stopwatch(self):
        self.stop_stopwatch()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()