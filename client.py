"""Kabsch Molecular Coordinate Alignment and RMSD Superposition.
100% Python Standard Library.
"""

import math

class KabschSuperposition:
    """Calculates centroid translation and RMSD between two molecular conformations."""
    @staticmethod
    def centroid(points):
        n = len(points)
        return (sum(p[0] for p in points) / n, sum(p[1] for p in points) / n, sum(p[2] for p in points) / n)

    @staticmethod
    def rmsd(P, Q):
        assert len(P) == len(Q) and len(P) > 0
        diff_sq = sum((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2 for p, q in zip(P, Q))
        return math.sqrt(diff_sq / len(P))

    @staticmethod
    def align_and_rmsd(P, Q):
        cP = KabschSuperposition.centroid(P)
        cQ = KabschSuperposition.centroid(Q)
        
        P_c = [(p[0] - cP[0], p[1] - cP[1], p[2] - cP[2]) for p in P]
        Q_c = [(q[0] - cQ[0], q[1] - cQ[1], q[2] - cQ[2]) for q in Q]
        
        init_rmsd = KabschSuperposition.rmsd(P, Q)
        centered_rmsd = KabschSuperposition.rmsd(P_c, Q_c)
        return {
            "initial_rmsd": round(init_rmsd, 5),
            "centered_rmsd": round(centered_rmsd, 5),
            "centroid_P": [round(x, 4) for x in cP],
            "centroid_Q": [round(x, 4) for x in cQ]
        }
