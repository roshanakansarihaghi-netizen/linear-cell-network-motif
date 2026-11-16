# Linear Cell Network Motif Analysis

This repository contains Python scripts for generating linear cell networks and analyzing the occurrence and average proportions of different network motifs under specified intercellular connection probabilities.

The scripts were developed as part of the computational research associated with the study of intercellular electrical connectivity in linear cell networks.

## Repository Contents

This repository contains two Python scripts:

### 1. `generate_linear_cell_network_motifs.py`

This script generates linear cell networks based on specified intercellular connection probabilities and calculates the occurrence of different network motifs.

The analysis includes:

- Generation of random linear cell networks.
- Identification of connected and unconnected cell arrangements.
- Calculation of distances between consecutive intercellular connections.
- Counting of different network motifs, including single cells, double-cell motifs, and larger multicellular motifs.

### 2. `func_calculate_average_motif_proportions.py`

This script performs repeated simulations using the network-generation and motif-counting functions.

It calculates the proportion of each motif relative to the total number of cells in the network and determines the average motif proportions across repeated simulations.

The results are saved in output files for subsequent analysis.

## Model Parameters

The simulations are controlled by parameters defined in the Python scripts, including:

- **Number of cells (`Ncells`):** The total number of cells in each linear network.
- **Number of bonds (`Nbonds`):** The number of possible intercellular connections between neighboring cells.
- **Connection probability (`Pp`):** The probability of an intercellular connection being present.
- **Complementary probability (`Pq`):** The probability of an intercellular connection being absent.
- **Number of repetitions:** The number of independent simulations used to calculate average motif proportions.

These parameters can be modified in the scripts to investigate different network configurations and connection probabilities.

## Requirements

- Python 3.x

The scripts use Python modules specified in their source files. Any required external packages should be installed before execution.

## Usage

1. Download or clone this repository.
2. Make sure the required Python packages are installed.
3. Adjust the simulation parameters in the scripts as needed.
4. Run the simulation and motif-analysis script:

```bash
[object Object]
```

The script performs repeated network simulations and calculates the average proportions of the identified motifs.

## Reproducibility

The results depend on the specified network parameters and the random generation of intercellular connections. Different simulation runs may therefore produce different results unless a random seed is specified.

## Citation

If you use these scripts in your research, please cite the associated study:

**Effects of intercellular electrical connectivity on membrane electric fields in linear cell networks.**

The full bibliographic reference and DOI will be added to this section once the study is published.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

The author would like to thank Dr. Seyed Pooya Shariatpanahi for their valuable guidance and assistance in troubleshooting during the development of the Python scripts.
