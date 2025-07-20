import numpy as np
import pandas as pd
from ase.io import read

# === User input section ===
filename = input("Enter structure file name (e.g., CONTCAR or structure.cif): ").strip()
atom1 = input("Enter element symbol of atom 1 (e.g., Fe): ").strip()
atom2 = input("Enter element symbol of atom 2 (e.g., O): ").strip()
cutoff = float(input("Enter maximum bond length (in Å): "))

output_file = f"{atom1}_{atom2}_bond_lengths.csv"

# === Read structure ===
atoms = read(filename)
symbols = atoms.get_chemical_symbols()
dists = atoms.get_all_distances(mic=True)

rows = []

for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):  # Avoid duplicates
        dist = dists[i, j]
        if dist < cutoff:
            pair = (symbols[i], symbols[j])
            if pair == (atom1, atom2) or pair == (atom2, atom1):
                rows.append({
                    "Atom 1 index": i,
                    "Atom 1 element": symbols[i],
                    "Atom 2 index": j,
                    "Atom 2 element": symbols[j],
                    "Distance (Å)": round(dist, 4)
                })

# === Save to CSV ===
if rows:
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"✅ Found {len(rows)} {atom1}–{atom2} bonds. Results saved to: {output_file}")
else:
    print(f"⚠️ No {atom1}–{atom2} bonds found within {cutoff} Å.")
