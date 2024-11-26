# 2024-PTGR1

## AMBERMD Input Files

### 1. PTGR1 + NADPH
#### 1.1. **PTGR1-NADPH.tar.xz**
- **Topology File:** `PTGR1-NADPH.parm7`
- **Coordinates File:** `PTGR1-NADPH.rst7`
- **System Initial Structure:** `PTGR1-NADPH.pdb`

### 2. PTGR1 + Non-covalent Licochalcone A
#### 2.1. **PTGR1-LicA_NO_covalent.tar.xz**
- **Topology File:** `PTGR1-LicA_NO_covalent.parm7`
- **Coordinates File:** `PTGR1-LicA_NO_covalent.rst7`
- **System Initial Structure:** `PTGR1-LicA_NO_covalent.pdb`
- **Non-covalent Licochalcone A Parameters:**
  - `LicA_NO_covalent.lib`
  - `LicA_NO_covalent.frcmod`

### 3. PTGR1 + Covalent Licochalcone A
#### 3.1. **PTGR1-LicA_covalent.tar.xz**
- **Topology File:** `PTGR1-LicA_covalent.parm7`
- **Coordinates File:** `PTGR1-LicA_covalent.rst7`
- **System Initial Structure:** `PTGR1-LicA_covalent.pdb`
- **Covalent Licochalcone A Parameters:**
  - `LicA_covalent.prepin`
  - `LicA_covalent.frcmod`

### 4. PTGR1 + NADPH (Monomer)
#### 4.1. **PTGR1-monomer_NADPH.tar.xz**
- **Topology File:** `PTGR1-monomer_NADPH.parm7`
- **Coordinates File:** `PTGR1-monomer_NADPH.rst7`
- **System Initial Structure:** `PTGR1-monomer_NADPH.pdb`

### 5. PTGR1 (Apo Form)
#### 5.1. **PTGR1-apo.tar.xz**
- **Topology File:** `PTGR1-apo.parm7`
- **Coordinates File:** `PTGR1-apo.rst7`
- **System Initial Structure:** `PTGR1-apo.pdb`

---

## Scripts

- **00_align_trajectories.cpptraj:** Aligns molecular trajectories.
- **01_autocorrelation.sh:** Analyzes dihedral angles and computes their autocorrelation in molecular trajectories.
- **02_RMSD_RoG.cpptraj:** Computes RMSD and radius of gyration for trajectory analysis.
- **03_contacts.cpptraj:** Calculates native contacts between specific residue ranges in a molecular trajectory.
- **04_hbonds.cpptraj:** Analyzes hydrogen bonds between specific residues in a molecular trajectory.
- **05_process_contacts_hbonds.py:** Processes residue contact time series, calculates averages, and outputs results in a CSV file.
- **06_lovofit.sh:** Performs RMSD fitting with mdlovofit for selected atoms and saves results.
- **07_FE_landscape.ipynb:** Analyzes data using PCA, plots a KDE for the first component, and generates a free energy landscape plot.
- **08_FE_landscape_Markov.ipynb:** Analyzes data with PCA, plots a KDE, and generates a Markov free energy landscape plot.
- **filter_fasta.py:** Retrieves unique sequences of vertebrate PTGR1 orthologs from the UniProt database.

---

## Python Libraries

- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations.
- **matplotlib**: Plotting and visualization.
- **sklearn**: Machine learning tools.
- **mdshare**: Utilities for molecular dynamics data.
- **seaborn**: Statistical data visualization.
- **pyemma**: For analyzing Markov models in molecular dynamics data.

