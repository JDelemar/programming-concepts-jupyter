import os
import argparse

# create an argument parser to parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--clear', action='store_true', help='clear notebook outputs')
args = parser.parse_args()

# list of notebook filenames to execute
notebook_filenames = [
  'CSharp/Filter, map, reduce - Where, Select, Aggregate.ipynb',
  'JavaScript/Maintainable JavaScript with Functional Patterns.ipynb',
  'TypeScript/Design Patterns/Behavioral/Observer.ipynb',
  'TypeScript/Design Patterns/Behavioral/Strategy.ipynb',
  'TypeScript/Design Patterns/Structural/Decorator.ipynb',
  ]

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
