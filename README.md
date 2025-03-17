# BBB-Hackathon
## Transcriptome Atlas

## Installation

### 1. Install conda

Install [miniforge](https://github.com/conda-forge/miniforge)

```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

### 2. Install the environment

Install the `ta` conda environment

```
conda env create -f environment.yaml
conda activate ta
```

### 3. Run jupyter notebook

Try running a query using the jupyter [notebook](QueryLLM.ipynb) (`QueryLLM.ipynb`)