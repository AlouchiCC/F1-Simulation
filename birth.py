import os
import json
import random
import shutil
import tkinter as tk

SIMULATION_DIR = "simulation"
GOOD_SIM_DIR = "good_sim"
os.makedirs(SIMULATION_DIR, exist_ok=True)
os.makedirs(GOOD_SIM_DIR, exist_ok=True)

def get_next_simulation_number():
    files = [f for f in os.listdir(SIMULATION_DIR) if f.startswith("Simulation-") and f.endswith(".json")]
    numbers = []
    for f in files:
        try:
            num = int(f.split("-")[1].split(".")[0])
            numbers.append(num)
        except:
            pass
    return max(numbers) + 1 if numbers else 1

def generate_simulation():
    num = get_next_simulation_number()
    filename = f"Simulation-{num}.json"
    filepath = os.path.join(SIMULATION_DIR, filename)

    data = {
        "nom": f"Simulation-{num}",
        "argent": random.randint(0, 3),
        "malade": random.randint(0, 1),
        "poids": random.randint(70, 120),
        "passion": random.randint(0, 1),
        "sponsor": random.randint(1, 250)
    }

    # Validation
    if data["poids"] < 80 and data["argent"] in [3, 4] and data["malade"] == 0 and data["passion"] == 1:
        data["valide"] = "✅"
    elif data["poids"] < 80 and data["malade"] == 0 and data["passion"] == 1 and data["sponsor"] == 1:
        data["valide"] = "✅"
    else:
        data["valide"] = "❌"

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    if data["valide"] == "✅":
        good_filepath = os.path.join(GOOD_SIM_DIR, filename)
        shutil.copy(filepath, good_filepath)

    print("\n" + "="*40)
    print(f"🎯 Nouvelle simulation générée : {filename}")
    print("="*40)
    for key, value in data.items():
        print(f"  ➜ {key:<15} : {value}")
    print("="*40 + "\n")

for i in range(100):
    generate_simulation() 
  
"""root = tk.Tk()
root.title("🧬 Générateur de Simulation")
root.geometry("600x400")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

def create_gradient(canvas, color1, color2):
    width, height = 600, 400
    (r1, g1, b1) = root.winfo_rgb(color1)
    (r2, g2, b2) = root.winfo_rgb(color2)
    for i in range(height):
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        color = f"#{r>>8:02x}{g>>8:02x}{b>>8:02x}"
        canvas.create_line(0, i, width, i, fill=color)

canvas = tk.Canvas(root, width=600, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, "#141426", "#2d2d4a")

title_label = tk.Label(
    root, text="✨ Générateur de Simulation ✨",
    font=("Segoe UI", 22, "bold"), fg="white", bg="#1e1e2f"
)
canvas.create_window(300, 80, window=title_label)

desc_label = tk.Label(
    root, text="Clique sur le bouton pour générer une simulation JSON.",
    font=("Segoe UI", 14), fg="#dddddd", bg="#1e1e2f"
)
canvas.create_window(300, 130, window=desc_label)

generate_button = tk.Button(
    root, text="⚡ Générer une Simulation",
    command=generate_simulation,
    font=("Segoe UI", 16, "bold"),
    bg="#4c72ff", fg="white",
    activebackground="#3555cc", activeforeground="white",
    relief="flat", bd=0, padx=30, pady=10
)
canvas.create_window(300, 220, window=generate_button)

footer_label = tk.Label(
    root, text="Créé avec ❤️ en Python pur",
    font=("Segoe UI", 10, "italic"),
    fg="#aaaaaa", bg="#1e1e2f"
)
canvas.create_window(300, 360, window=footer_label)"""

#root.mainloop()
