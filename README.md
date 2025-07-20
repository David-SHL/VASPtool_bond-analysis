# VASPtool_bond-analysis
This script allows users to extract all bond distances between two specified atomic species (e.g., Fe–O, O–H) within a user-defined distance cutoff. It supports VASP and CIF structure formats and outputs results as a CSV file.

## 🔧 Features

- Extracts all distances between two atom types (e.g., Fe–O, Fe–H, O–H)
- Supports VASP structure files (CONTCAR, POSCAR) and CIF format
- Distance cutoff defined interactively by the user
- Outputs a clean `.csv` file with all matching bond pairs and their lengths

## 🧪 Requirements

- Python 3.6+
- [ASE (Atomic Simulation Environment)](https://wiki.fysik.dtu.dk/ase/)
- pandas
- numpy

