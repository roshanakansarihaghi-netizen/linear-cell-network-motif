# Linear Cell Network Motif Analysis

This repository contains Python scripts developed to generate random linear cell networks with different intercellular tube-formation probabilities and calculate the average proportions of different network motifs.

The primary purpose of these scripts is to quantify the distribution of network motifs across randomly generated linear cell networks at different tube-formation probabilities. The resulting motif proportions were used in conjunction with COMSOL Multiphysics simulation results in the associated study to investigate the effects of intercellular electrical connectivity on membrane electric fields in linear cell networks.

## Repository Contents

This repository contains two Python scripts:

### 1. `generate_linear_cell_network_motifs.py`

This script generates random linear cell networks based on specified intercellular connection probabilities and calculates the occurrence of different network motifs.

The analysis includes:

- Generation of random linear cell networks.
- Identification of connected and unconnected cell arrangements.
- Calculation of distances between consecutive intercellular connections.
- Counting of different network motifs, including single cells, double-cell motifs, and larger multicellular motifs.

### 2. `func_calculate_average_motif_proportions.py`

This script performs repeated simulations using the network-generation and motif-counting functions.

It calculates the proportion of each motif relative to the total number of cells in the network and determines the average motif proportions across repeated simulations. These average proportions provide a quantitative description of the network configurations at different intercellular tube-formation probabilities.

The resulting data were used in combination with the COMSOL Multiphysics simulation results in the associated study.

## Model Parameters

The simulations are controlled by parameters defined in the Python scripts, including:

- **Number of cells (`Ncells`):** The total number of cells in each linear network.
- **Number of bonds (`Nbonds`):** The number of possible intercellular connections between neighboring cells.
- **Connection probability (`Pp`):** The probability of an intercellular connection being present.
- **Complementary probability (`Pq`):** The probability of an intercellular connection being absent.
- **Number of repetitions:** The number of independent simulations used to calculate average motif proportions.

These parameters can be modified in the scripts to investigate different network configurations and intercellular connection probabilities.

## Requirements

- Python 3.x

The scripts use Python modules specified in their source files. Any required external packages should be installed before execution.

## Usage

1. Download or clone this repository.
2. Make sure the required Python packages are installed.
3. Adjust the simulation parameters in the scripts as needed.
4. Run the simulation and motif-analysis script:

```bash
python func_calculate_average_motif_proportions.py
```

The script performs repeated random network simulations, calculates the proportions of the identified motifs, and saves the results in output files.

## Reproducibility

The results depend on the specified network parameters and the random generation of intercellular connections. Different simulation runs may therefore produce different results unless a random seed is specified.

## Citation

If you use these scripts in your research, please cite the associated study:

**Effects of intercellular electrical connectivity on membrane electric fields in linear cell networks.**

The full bibliographic reference and DOI will be added to this section once the study is published.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/roshanakansarihaghi-netizen/linear-cell-network-motif/blob/main/LICENSE) file for details.
