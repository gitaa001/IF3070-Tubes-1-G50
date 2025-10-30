import random
from initializer import generate_initial_state
from algorithm.hill_climbing.steepest_ascent.SteepestAscent import SteepestAscent
from algorithm.hill_climbing.sideways_move.HillClimbingSideways import HillClimbingSideways
from algorithm.hill_climbing.random_restart.RandomRestartHillClimbing import RandomRestartHillClimbing
from algorithm.hill_climbing.stochastic.StochasticHillClimbing import StochasticHillClimbing
from algorithm.simulated_annealing.SimulatedAnnealing import SimulatedAnnealing
from algorithm.genetic.Genetic import GeneticAlgorithm
from utils import load_input

def main_menu():
    print(r"""
    ________________________________________________
                        
    IRASSHAIMASE! Selamat Datang di Bin Packing Optimizer!

    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
    ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝      
                                                     
    ________________________________________________
    """)

    while True:
        print("""
            +-------------------------------+
            |     PILIH ALGORITMA YANG      |
            |          INGIN DICOBA         |
            +-------------------------------+
        """)
        print("1. Steepest Ascent Hill-Climbing")
        print("2. Hill-Climbing with Sideways Move")
        print("3. Random Restart Hill-Climbing")
        print("4. Stochastic Hill-Climbing")
        print("5. Simulated Annealing")
        print("6. Genetic Algorithm")
        print("7. Keluar dari program")

        pilihan = input("Masukkan nomor opsi (1-7): ")

        if pilihan == '1':
            print("\nAnda memilih Steepest Ascent Hill-Climbing.")

            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)

            random.shuffle(barang_list)
            initial_state = generate_initial_state(barang_list, kapasitas)
            
            algo = SteepestAscent(initial_state, kapasitas)
            algo.run()

        elif pilihan == '2':
            print("\nAnda memilih Hill-Climbing with Sideways Move.")
            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)
            
            random.shuffle(barang_list)
            initial_state = generate_initial_state(barang_list, kapasitas)
            
            algo = HillClimbingSideways(initial_state, kapasitas)
            algo.run()
        
        elif pilihan == '3':
            print("\nAnda memilih Random Restart Hill-Climbing.")

            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)
            
            algo = RandomRestartHillClimbing(barang_list, kapasitas)
            algo.run()

        elif pilihan == '4':
            print("\nAnda memilih Stochastic Hill-Climbing.")

            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)
            
            random.shuffle(barang_list)
            initial_state = generate_initial_state(barang_list, kapasitas)

            algo = StochasticHillClimbing(initial_state, kapasitas)
            algo.run()
        

        elif pilihan == '5':
            print("\nAnda memilih Simulated Annealing.")

            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)
            
            random.shuffle(barang_list)
            initial_state = generate_initial_state(barang_list, kapasitas)

            algo = SimulatedAnnealing(initial_state, kapasitas)
            algo.run()
        
        elif pilihan == '6':
            print("\nAnda memilih Genetic Algorithm.")

            filename = input("Masukkan nama file input (misal: input.json): ")
            kapasitas, barang_list = load_input(filename)

            initial_state = generate_initial_state(barang_list, kapasitas)
            ga = GeneticAlgorithm(initial_state, kapasitas)
            ga.run()


        elif pilihan == '7':
            print("\NTerima kasih telah menggunakan program ini. Keluar...")
            break
        else:
            print("\NOpsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
    print(r"""
    ________________________________________________
                        
    SAYONARA! Terima kasih telah menggunakan Bin Packing Optimizer!
          
    ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
    ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
       ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
       ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
       ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ 
                                                                                                 
    ________________________________________________
    """)