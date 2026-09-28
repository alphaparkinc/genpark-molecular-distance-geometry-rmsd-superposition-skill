"""Example demonstrating molecular RMSD calculation."""
from client import KabschSuperposition

def main():
    P = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    Q = [(10.0, 10.0, 10.0), (11.0, 10.0, 10.0), (10.0, 11.0, 10.0)]
    res = KabschSuperposition.align_and_rmsd(P, Q)
    print("RMSD Analysis Results:")
    print("  Initial RMSD:", res["initial_rmsd"])
    print("  Centered RMSD:", res["centered_rmsd"])

if __name__ == "__main__":
    main()
