# Run: jupyter nbconvert --to notebook --inplace --allow-errors --execute --config config.py
# Clear: jupyter nbconvert --clear-output --to notebook --inplace --config config.py
# If using docker jupyter notebook prefix with: docker run --rm -v $PWD:/opt/app/data --workdir /opt/app/data jdelemar/jupyterlab-dotnet:6.0.202

c = get_config()
c.NbConvertApp.notebooks = [
  "CSharp/Filter, map, reduce - Where, Select, Aggregate.ipynb",
  "JavaScript/Maintainable JavaScript with Functional Patterns.ipynb",
  "TypeScript/Design Patterns/Behavioral/Observer.ipynb",
  "TypeScript/Design Patterns/Behavioral/Strategy.ipynb",
  "TypeScript/Design Patterns/Structural/Decorator.ipynb",
]
