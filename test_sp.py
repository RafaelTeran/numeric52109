###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###
import simple_package.operations as sp_ops
import simple_package.statistics as sp_stats
import simple_package.graphics as sp_gfx
import random
import sys
import time

# This is a simple test script to demonstrate the functionalities
# of the simple_package. It allows the user to choose between
# operations (basic arithmetic) and statistics (mean, median, etc.).

# This function safely handles user input and allows exiting
def safe_input(prompt):
    text = input(prompt).strip().lower()
    if text == "exit":
        print("Exiting the test script. Goodbye!")
        sys.exit(0)
    return text

def slow_print(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Fuerza la salida a la terminal inmediatamente
        time.sleep(delay)

# Main test loop
if __name__ == "__main__":
    print("Hello! Welcome to the simple_package test script.")
    print("This package has two main functionalities: operations and statistics.")
    print("Operations include basic arithmetic calculations.")
    print("Statistics include calculating mean, median, and plotting histograms.")
    print("##########################    START OF THE TEST   ##########################")
    while True:
        print("Type 'exit' at any moment to quit the test.")
        choice = safe_input("Enter 'ops' for operations or 'stats' for statistics: ")
        # Handle statistics choice
        if choice == 'stats':
            try:
                # We are going to generate a sample data set for testing
                n = int(safe_input("Enter the number of random data points to generate for statistics: "))
                distribution = safe_input("Enter 'uniform' for uniform distribution or 'normal' for normal distribution: ")
                if distribution == 'uniform':
                    a = int(safe_input("Enter the minimum value (inclusive): "))
                    b = int(safe_input("Enter the maximum value (inclusive): "))
                elif distribution == 'normal':
                    mu = float(safe_input("Enter the mean (mu): "))
                    sigma = float(safe_input("Enter the standard deviation (sigma): "))
                else:
                    print("Invalid distribution type. Please enter 'uniform' or 'normal'.\nRestarting the test")
                    slow_print ("##########################", delay=0.2)
                    print("   RESTART OF THE TEST  ##########################")
                    continue

                if distribution == 'uniform':
                    sample_data = [random.randint(a, b) for _ in range(n)]
                elif distribution == 'normal':
                    sample_data = [int(random.gauss(mu, sigma)) for _ in range(n)]

                sp_stats.print_statistics(sample_data)
                try:
                    sp_gfx.plot_histogram(sample_data, a = min(sample_data), b = max(sample_data))
                except ImportError as e:
                    print(e,"\nRestarting the test")
                    slow_print ("##########################", delay=0.2)
                    print("   RESTART OF THE TEST  ##########################")
            except ValueError:
                print("Invalid input. Please enter numeric values where required.\nRestarting the test")
                slow_print ("##########################", delay=0.2)
                print("   RESTART OF THE TEST  ##########################")
        elif choice == 'ops':
            sp_ops.calculator_interface()
        else:
            print("Invalid choice. Please run the script again and choose 'ops' or 'stats'.\nRestarting the test")
            slow_print ("##########################", delay=0.2)
            print("   RESTART OF THE TEST  ##########################")