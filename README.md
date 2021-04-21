# Global FoodOmics package

Current functionality includes generating food counts tables from a molecular network (sample data networked with reference data using classical molecular networking). Follow [Reference Data-Driven Analysis tutorial](https://docs.google.com/document/d/15PzVIoDcONCCaAe8GDEM8YBGTdrgDTFA-7VqWjrqEFM/edit?usp=sharing) to run the networking job in GNPS.

## Usage:
1. Clone `main` branch of this repository

    ```
    git clone -b main https://github.com/ka-west/gfop.git
    ```

2. Navigate to the package directory

    ```
    cd gfop
    ```

3. Start Python

    ```
    python
    ```

4. Import functions

    ```
    import gfop.get_food_counts as gfop
    ```

5. Generate food counts table.

    ```
    f_counts = gfop.get_dataset_food_counts(gnps_network = 'METABOLOMICS-SNETS-V2-07f85565-view_all_clusters_withID_beta-main.tsv',
                                            metadata = 'sample_metadata.csv',
                                            filename_col = 'filenames',
                                            sample_types = 'simple',
                                            all_groups = ['G1'],
                                            some_groups = ['G4'],
                                            level = 5)
    ```
    
    You can type `help(gfop.get_dataset_food_counts)` for more information about the required arguments.
