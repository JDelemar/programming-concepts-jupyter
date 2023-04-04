import argparse
import glob
import os

# create an argument parser to parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--clear', action='store_true', help='clear notebook outputs')
args = parser.parse_args()

# find all notebook files in current and subdirectories
notebook_filenames = glob.glob('**/*.ipynb', recursive=True)

# loop through each notebook filename
for filename in notebook_filenames:
    # construct the command to execute or clear the notebook
    if args.clear:
      command = f'jupyter nbconvert --clear-output --to notebook --inplace "{filename}"'
    else:
      command = f'jupyter nbconvert --to notebook --inplace --allow-errors --execute "{filename}"'
    # execute the command in the system shell
    # print(command)
    os.system(command)
