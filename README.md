# Molecular RMSD Superposition Skill

Geometric coordinate superposition and Root Mean Square Deviation (RMSD) tool for comparative structural chemistry and biology.

```mermaid
flowchart LR
    P["Conformation P (x, y, z)"] --> CentroidP["Compute Centroid P_c"]
    Q["Conformation Q (x, y, z)"] --> CentroidQ["Compute Centroid Q_c"]
    CentroidP --> Translate["Translate Centroids to Origin"]
    CentroidQ --> Translate
    Translate --> Diff["Compute Euclidean Difference Norm"]
    Diff --> RMSD["RMSD Value Output"]
```

## Features
- **100% Python Standard Library**: Pure Euclidean geometry.
- **Centroid Centering**: Invariance to spatial coordinates translation.
- **Fast Atom Superposition**: Instant scoring for molecular docking and dynamics.
