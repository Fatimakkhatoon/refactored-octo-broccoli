'''
This script is prepared by Dr. Fatima, and it is a part of the course teaches by Dr. Fatima.
***********************************
Usage:
            python3 python_script_name.py protein.pdbqt file_having_list_of_ligands.txt config.txt

***********************************
'''

import os
import sys

if __name__ == "__main__":
    try:
        c_dir = os.getcwd()
        receptor = sys.argv[1]
        input_ligand_list = sys.argv[2]
        configuration_file = sys.argv[3]
        f = open(input_ligand_list)
        for lines in f:
            line_data = lines.strip()
            line_data_splitting = line_data.split(".")
            ligand_name = line_data_splitting[0]
            out_file = ligand_name + "_docking_output.pdbqt"
            logfile_name = ligand_name + "_logfile.txt"
            os.system(f"./vina --config {configuration_file} --receptor {receptor} --ligand {line_data} --out {out_file} --log {logfile_name}")


    except Exception as e:
        print(f"Something went wrong..")
