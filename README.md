# refactored-octo-broccoli
This Python script automates molecular docking using AutoDock Vina, enabling batch processing of multiple ligands against a given protein target. Developed by Dr. Fatima, this script simplifies virtual screening for computational chemists and bioinformaticians.
Features
✅ Batch Docking: Automates docking for multiple ligands.
✅ AutoDock Vina Integration: Runs vina for molecular docking.
✅ Automated Output Handling: Generates docking output and log files.
✅ Error Handling: Basic exception handling for input issues.

Usage
Run the script as:

bash
Copy
Edit
python3 docking_script.py protein.pdbqt ligand_list.txt config.txt
protein.pdbqt → Prepared receptor file.
ligand_list.txt → List of ligand files (e.g., ligand1.pdbqt, ligand2.pdbqt).
config.txt → Vina configuration file.
Example Input (ligand_list.txt)
Copy
Edit
ligand1.pdbqt  
ligand2.pdbqt  
ligand3.pdbqt  
The script generates:

ligand1_docking_output.pdbqt, ligand1_logfile.txt, etc.
Requirements
Python 3
AutoDock Vina (Ensure vina is installed and accessible)
Troubleshooting
🔹 Verify vina is installed and configured correctly.
🔹 Ensure input files are properly formatted.

This script streamlines high-throughput docking, making it a valuable tool for drug discovery workflows. 🚀
