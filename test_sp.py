###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###
import simple_package.operations as sp_ops
import simple_package.statistics as sp_stats
import simple_package.graphics as sp_gfx
import random

if __name__ == "__main__":
    print("Select if you want to test operations or statistics:")
    choice = input("Enter 'ops' for operations or 'stats' for statistics: ").strip().lower()
    if choice == 'stats':
        sample_data = [random.randint(1, 10) for _ in range(20)]
        sp_stats.print_statistics(sample_data)
        try:
            sp_gfx.plot_histogram(sample_data)
        except ImportError as e:
            print(e)
    elif choice == 'ops':
        sp_ops.calculator_interface()
    else:
        print("Invalid choice. Please run the script again and choose 'ops' or 'stats'.")