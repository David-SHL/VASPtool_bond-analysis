# VASPtool_bond-analysis
This script allows users to extract all bond distances between two specified atomic species (e.g., Fe–O, O–H) within a user-defined distance cutoff. It supports VASP and CIF structure formats and outputs results as a CSV file.

## Features

- Extracts all distances between two atom types (e.g., Fe–O, Fe–H, O–H)
- Supports VASP structure files (CONTCAR, POSCAR) and CIF format
- Distance cutoff defined interactively by the user
- Outputs a clean `.csv` file with all matching bond pairs and their lengths

## Requirements

- Python 3.6+
- [ASE (Atomic Simulation Environment)](https://wiki.fysik.dtu.dk/ase/)
- pandas
- numpy

## Usage

- Place your structure file (e.g., CONTCAR, structure.cif) in the same directory.
- Run the script: bond.py
- Follow the prompts:

Enter structure file name (e.g., CONTCAR or structure.cif): CONTCAR
Enter element symbol of atom 1 (e.g., Fe): Fe
Enter element symbol of atom 2 (e.g., O): O
Enter maximum bond length (in Å): 3.0

The script will generate a file named Fe_O_bond_lengths.csv containing all matching bond pairs and their distances.

