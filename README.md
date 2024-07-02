# 2024-PTGR1

## AMBERMD Input Files

### 1. PTGR1 + NADPH
#### 1.1. Topology
- **File:** PTGR1-NADPH.parm7

#### 1.2. Coordinates
- **File:** PTGR1-NADPH.rst7

#### 1.3. System Initial Structure
- **File:** PTGR1-NADPH.pdb

### 2. PTGR1 + Non-covalent Licochalcone A 
#### 2.1. Topology
- **File:** PTGR1-LicA-NC.parm7

#### 2.2. Coordinates
- **File:** PTGR1-LicA-NC.rst7

#### 2.3. System Initial Structure
- **File:** PTGR1-LicA-NC.pdb

#### 2.4. Non-covalent Licochalcone A Params
- **File:** LicA-NC.lib
- **File:** LicA-NC.frcmod

### 3. PTGR1 + Covalent Licochalcone A
#### 3.1. Topology
- **File:** PTGR1-LicA-C.parm7

#### 3.2. Coordinates
- **File:** PTGR1-LicA-C.rst7

#### 3.3. System Initial Structure
- **File:** PTGR1-LicA-C.pdb

#### 3.4. Covalent Licochalcone A Params
- **File:** LicA-C.prepin
- **File:** LicA-C.frcmod

## Scripts

- **00_align_trajectories.cpptraj:** General trajectory alignment script.
- **01_autocorrelation.sh:** A script that analyzes dihedral angles in a molecular trajectory, processes their magnitudes, and computes their autocorrelation.
- **02_RMSD_RoG.cpptraj:** A script that computes RMSD to a reference structure, and calculates the radius of gyration.
- **03_contacts.cpptraj:** A script that calculates native contacts between specific residue ranges in a molecular trajectory.
- **04_hbonds.cpptraj:** A script that analyzes hydrogen bonds between specific residues in a molecular trajectory.
- **05_process_contacs-hbonds.py:** A script that processes a residue contact time series file, calculates averages, and saves the results in a CSV file.
- **06_lovofit.sh:** A script that calculates RMSD using mdlovofit and performs a fitting procedure on specific atoms with additional parameters, saving the results to files.
- **07_FE_landscape.ipynb:** A script that analyzes data using PCA, plots a KDE for the first component, and generates a free energy landscape plot.
- **08_FE_landscape_Markov.ipynb:** A script that analyzes data using PCA, plots a KDE for the first component, and generates a free energy landscape Markov plot.
- **filter_fasta.py:** Script to retrieve unique sequences of vertabrate PTGR1 orthologs from UniProt database.

## Python Libraries

## Python Libraries
- **pandas**
- **numpy**
- **matplotlib**
- **sklearn**
- **mdshare**
- **seaborn**
- **pyemma**
