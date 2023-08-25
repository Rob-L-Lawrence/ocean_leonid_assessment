# README

This is a project written by Robert Lawrence for the purposes of the Ocean Leonid assessment.

## Distribution

**Github**

To get started with the raw code, clone the repo and then run the following commands:

```shell
pip install poetry
poetry install
python ./ocean_leonid/run.py
```

The dash app is now available on your browser at `http://localhost:8050`.

**Docker**

To deploy the dash app using docker use the following commands:

```shell
docker build . -t ocean_leonid
docker container run -p 8050:8050  ocean_leonid
```

The dash app is now available on your browser at `http://localhost:8050`.

## Tests

## External Dependencies

The external dependencies of this solution are the 2 API's that are called to get the data for the graph.

## Design Decisions