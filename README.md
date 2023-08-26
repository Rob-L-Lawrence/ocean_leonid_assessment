# README

This is a project written by Robert Lawrence for the purposes of the Ocean Leonid assessment.

## Distribution

**Github**

To get started with the raw code, clone the repo and then run the following commands:

```shell
pip install poetry
poetry install
python main.py
```

The dash app is now available on your browser at `http://localhost:8050`.

**Docker**

To deploy the dash app using docker use the following commands:

```shell
docker build . -t ocean_leonid
docker container run -p 8050:8050  ocean_leonid
```

The dash app is now available on your browser at `http://localhost:8050`.

**Pip package**

I have created the module as [PyPi package](https://pypi.org/project/ocean-leonid/) that can be installed.

```shell
pip install ocean-leonid
```

```py
from ocean_leonid import show_viz

show_viz()
```

## Tests

The testing is done using pytest

The configuration is in pyproject.toml.

To run the tests use:
```shell
pytest
```

## External Dependencies

The external dependencies of this solution are the 2 API's that are called to get the data for the graph.
