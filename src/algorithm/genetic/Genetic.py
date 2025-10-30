import random
import time
import matplotlib.pyplot as plt
from bin.objective_function import objective_function
from bin.state import State 

class GeneticAlgorithm:
    def __init__(self, initial_state, kapasitas):
        self.initial_state = initial_state
        self.kapasitas = kapasitas
        
        print("\n=== Input Parameter Genetic Algorithm ===")
        self.population_size = int(input("Masukkan jumlah populasi: "))
        self.max_iterasi = int(input("Masukkan banyak iterasi (generasi): "))
        self.mutation_rate = float(input("Masukkan probabilitas mutasi (contoh 0.1): "))

        # ambil jumlah barang
        self.barang_list = []
        for k in initial_state.kontainer_list:
            for b in k.isi:
                self.barang_list.append(b)
        self.n_barang = len(self.barang_list)

        # banyak kontainer awal = batas max kontainer
        self.max_kontainer = len(initial_state.kontainer_list)

        self.population = []
        self.best_chrom = None
        self.best_value = float("inf")
        self.best_history = []
        self.avg_history = []

    def initialize_population(self):
        # hasil awal pakai representasi kromosom
        init_chrom = []
        mapping = {} 
        for idx_k, k in enumerate(self.initial_state.kontainer_list):
            for b in k.isi:
                mapping[b.id] = idx_k
        
        for b in self.barang_list:
            init_chrom.append(mapping[b.id])
        
        self.population.append(init_chrom)

        while len(self.population) < self.population_size:
            chrom = [random.randint(0, self.max_kontainer - 1) for _ in range(self.n_barang)]
            self.population.append(chrom)

    def decode(self, chrom):
        from bin.entity.kontainer import Kontainer

        kontainer_real = [Kontainer(self.kapasitas) for _ in range(self.max_kontainer)]
        for idx_barang, id_k in enumerate(chrom):
            kontainer_real[id_k].tambah_barang(self.barang_list[idx_barang])

        # if kontainer kosong = remove
        kontainer_real = [k for k in kontainer_real if len(k.isi) > 0]
        return kontainer_real

    def evaluate(self, chrom):
        kontainer_real = self.decode(chrom)
        return objective_function(State(kontainer_real), self.kapasitas)

    def selection(self):
        # Tournament selection
        a = random.choice(self.population)
        b = random.choice(self.population)
        return a if self.evaluate(a) < self.evaluate(b) else b

    def crossover(self, p1, p2):
        point = random.randint(1, self.n_barang - 1)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return c1, c2

    def mutate(self, chrom):
        if random.random() > self.mutation_rate:
            return chrom 
        # mutasi: pindahkan 1 barang ke kontainer lain
        idx = random.randint(0, self.n_barang - 1)
        new_k = random.randint(0, self.max_kontainer - 1)
        chrom[idx] = new_k
        return chrom

    def run(self):
        self.initialize_population()

        print("\n==============================")
        print("STATE AWAL GENETIC ALGORITHM")
        print("==============================")
        print(self.initial_state)
        print(f"Objective awal  : {objective_function(self.initial_state, self.kapasitas)}\n")

        start = time.time()

        for gen in range(self.max_iterasi):
            scored = [(chrom, self.evaluate(chrom)) for chrom in self.population]
            scored.sort(key=lambda x: x[1])

            best_val = scored[0][1]
            avg_val = sum(val for _, val in scored) / len(scored)

            self.best_history.append(best_val)
            self.avg_history.append(avg_val)

            if best_val < self.best_value:
                self.best_value = best_val
                self.best_chrom = scored[0][0]

            print(f"Iterasi {gen+1} | Best: {best_val} | Avg: {avg_val}")

            new_pop = []
            while len(new_pop) < self.population_size:
                p1 = self.selection()
                p2 = self.selection()
                c1, c2 = self.crossover(p1, p2)
                c1 = self.mutate(c1)
                c2 = self.mutate(c2)
                new_pop.extend([c1, c2])

            self.population = new_pop[:self.population_size]

        elapsed = time.time() - start

        best_kontainer = self.decode(self.best_chrom)

        print("\n==============================")
        print("STATE AKHIR GENETIC ALGORITHM")
        print("==============================")

        for i, k in enumerate(best_kontainer):
            print(f"Kontainer {i+1}: {k}")

        print("\nDetail Eksekusi:")
        print(f"Objective Terbaik        : {self.best_value}")
        print(f"Jumlah Iterasi           : {self.max_iterasi}")
        print(f"Jumlah Populasi          : {self.population_size}")
        print(f"Probabilitas Mutasi      : {self.mutation_rate}")
        print(f"Waktu Eksekusi           : {elapsed:.4f} detik")
        print("=" * 32)

        self.show_plot()

        return best_kontainer, self.best_value, elapsed

    def show_plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.best_history, label="Best Objective")
        plt.plot(self.avg_history, label="Avg Objective")
        plt.xlabel("Iterasi")
        plt.ylabel("Objective Value")
        plt.title("Perkembangan Objective Value terhadap Iterasi")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

