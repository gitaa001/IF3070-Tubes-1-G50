import matplotlib.pyplot as plt
import time
import random
from bin.objective_function import objective_function
from bin.neighbor_state import generate_neighbors

class StochasticHillClimbing:
    def __init__(self, initial_state, kapasitas, max_iter=100, max_no_improve=10):
        self.current_state = initial_state
        self.kapasitas = kapasitas
        self.current_value = objective_function(initial_state, kapasitas)
        self.objective_values = [self.current_value]
        self.max_iter = max_iter
        self.max_no_improve = max_no_improve  

    def run(self):
        print("\n============================")
        print("   STATE AWAL STOCHASTIC      ")
        print("==============================")
        print(self.current_state)
        print(f"Objective awal : {self.current_value}")
        print(f"Jumlah kontainer: {len(self.current_state.kontainer_list)}\n")

        start_time = time.time()
        no_improve_count = 0
        
        for iterasi in range(1, self.max_iter + 1):
            neighbors = generate_neighbors(self.current_state)

            if not neighbors:
                print(f"Iterasi {iterasi}: tidak ada tetangga, berhenti.")
                break

            # Batas jumlah neighbors yang dievaluasi
            if len(neighbors) > 50:  
                neighbors = random.sample(neighbors, 50)

            neighbor = random.choice(neighbors)
            value = objective_function(neighbor, self.kapasitas)

            if value < self.current_value:
                self.current_state = neighbor
                self.current_value = value
                no_improve_count = 0 
                print(f"Iterasi {iterasi}: perbaikan → {value}")
            else:
                no_improve_count += 1

            self.objective_values.append(self.current_value)

            if no_improve_count >= self.max_no_improve:
                print(f"Iterasi {iterasi}: tidak ada perbaikan dalam {self.max_no_improve} iterasi, berhenti.")
                break

            if iterasi % 10 == 0:
                print(f"Iterasi {iterasi}: Objective = {self.current_value}")

        elapsed = time.time() - start_time

        print("\n============================")
        print("    STATE AKHIR STOCHASTIC    ")
        print("==============================")
        print(self.current_state)
        print(f"Objective akhir : {self.current_value}")
        print(f"Total iterasi   : {iterasi}")
        print(f"Jumlah kontainer: {len(self.current_state.kontainer_list)}")
        print(f"Durasi eksekusi  : {elapsed:.3f} detik\n")

        self.show_plot()
        return self.current_state, self.current_value, elapsed

    def show_plot(self):
        if len(self.objective_values) < 2:
            print("Tidak cukup data untuk plot.")
            return
            
        plt.figure(figsize=(10, 6))
        plt.plot(self.objective_values, marker='o', linewidth=2, markersize=4)
        plt.title("Perkembangan Objective Value per Iterasi")
        plt.xlabel("Iterasi")
        plt.ylabel("Objective Value")
        plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)
        plt.tight_layout()
        plt.show()