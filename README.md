# Programming Concepts with Jupyter

Programming Concepts with Jupyter

## Quick start

- Quick start
  - Ensure you have the requirements (see below)
  - Clone this repository
  - Start the Jupyter server `docker run -p 8888:8888 jdelemar/jupyterlab-dotnet:6`
    - Copy the token from the Jupyter server output
  - Open a notebook - `.ipynb` file
  - In the bottom right of VSCode select `Jupyter Server` to input the server URI (e.g. `http://localhost:8888?token=placeYourTokenHere`)
  - Run / edit / change the notebook as you see fit

## Requirements

- Requirements
  - Docker
  - Jupyterlab with .NET
  - Visual Studio Code with Microsoft Jupyter extension (ms-toolsai.jupyter)
  - (optional) Markdown Preview Mermaid Support (bierner.markdown-mermaid) for markdown with mermaid

### Notebooks

#### CSharp

Name | Description
---|---
[Map, Reduce, Filter in CSharp](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/CSharp/Filter%2C%20map%2C%20reduce%20-%20Where%2C%20Select%2C%20Aggregate.ipynb) | JavaScript map, reduce, filter == CSharp Where, Select, Aggregate

#### JavaScript

Name | Description
---|---
[Maintainable JavaScript with Functional Patterns](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/JavaScript/Maintainable%20JavaScript%20with%20Functional%20Patterns.ipynb)

#### TypeScript

Name | Description
---|---
[Design Patterns: Abstract Factory](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/TypeScript/Design%20Patterns/Creational/Abstract%20Factory.ipynb) | Abstract Factory examples
[Design Patterns: Factory Method](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/TypeScript/Design%20Patterns/Creational/Factory%20Method.ipynb) | Factory Method examples
[Design Patterns: Decorator](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/TypeScript/Design%20Patterns/Structural/Decorator.ipynb) | Decorator Pattern examples
[Design Patterns: Observer Pattern](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/TypeScript/Design%20Patterns/Behavioral/Observer.ipynb) | Observer Pattern examples
[Design Patterns: Strategy Pattern](https://github.com/JDelemar/programming-concepts-jupyter/blob/main/TypeScript/Design%20Patterns/Behavioral/Strategy.ipynb) | Strategy Pattern examples

### Notes

- Notes
  - **TODO**
    - TypeScript examples - using types
    - CSharp
      - check if nuget packages work - NewtonSoft.Json
      - programming tips - LINQ, AutoMapper
      - language version differences 6, 7, 8, 9, 10
    - How to show lines for cells?
    - Fix Mermaid not displaying properly in GitHub repo
  - Useful commands
    - Command Palette
      - `Notebook: Clear cell outputs`
      - `Notebook: Run all`

### Workflow

- Workflow
  - Do not work on the main branch
  - Work on develop or some other branch
  - Updating
    - After updating notebook(s)
      - Prepare
        - develop
          - Ensure all cell outputs have been cleared
          - Ensure all changes have been committed
      - Update
        - main
          - Switch to the main branch
          - Remove the `🎨Execute notebook` commit `git reset --hard HEAD^`
          - Force update main branch `git push --force`
          - Merge develop into main `git merge develop`
          - Execute all cell outputs - can use `./nbconvert`
          - Create `🎨Execute notebook` commit

#### References

- References
  - [Jupyter Notebooks in a Git Repository](https://mg.readthedocs.io/git-jupyter.html)
  - [Jupyter Notebook gitignore](https://github.com/jupyter/notebook/blob/main/.gitignore)
