# Farm uncertainty
This repository contains the code to run a model of farmer uptake of subsidies for agri-environmental schemes under future climate uncertainty
## Content
- [Quickstart](#quickstart)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Basic usage](#basic-usage)
  - [Notebooks](#notebooks)
- [Development](#development)
  - [Tests](#tests)
- [Overview](#overview)
  - [Modules](#modules)
  - [Types](#types)
## Quickstart

### Prerequisites
- A [`Python`](https://www.python.org/) installation (3.9+).

### Installation

### Basic usage

### Notebooks

## Development
To set up the repository on your local machine to contribute to its development do the following:
- Install [Poetry](https://python-poetry.org/) in your base python: `pip install poetry`
- Clone the repository with the following command:
`git clone https://github.com/mcmancini/FarmUncertainty.git`.
Make sure to navigate to the correct location where you want the repository to be cloned into.
- Navigate to the directory: `cd FarmUncertainty`
- install required dependencies: `poetry install`
- Activate the virtual environment: `poetry shell`
- For the first time, install pre-commit hooks: `pre-commit install`. This needs to be done only the first time that the repository is being set up locally.

**N.B.**
- The virtual environment is activated with `poetry shell` and deactivated with `exit`
- To install dependencies in the virtual environment:
`poetry add -group dev name_of_dependency` if the dependency is for development purposes only;
`poetry add name_of_dependency` for main dependencies
### Tests

## Overview

### Modules

### Types
