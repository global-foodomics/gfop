# Global FoodOmics package

Current functionality includes generating food counts tables from a molecular network (sample data networked with reference data using classical molecular networking). Follow [Reference Data-Driven Analysis tutorial](https://ccms-ucsd.github.io/GNPSDocumentation/tutorials/rdd/) to run the networking job in GNPS.

## Dependencies
Make sure you have Python 3.6 or newer installed. You will also need the following packages installed:   
* numpy   
    ```
    pip3 install numpy
    ```
* pandas   
    ```
    pip3 install pandas
    ```

## Usage
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
    * The argument `gnps_network` is the path to the tsv file you will have downloaded from your molecular networking job. Be sure to use the absolute path.   
    * The argument `metadata` is the path to your sample metadata (csv or tsv file). It must contain a column with the sample filenames. This will be used to match the files added to G1/G2 in the molecular network. Again, use the absolute path.
    * `filename_col` is the column header in `metadata` that contains the sample filenames.
    * The argument `sample_types` can be one of: `simple`, `complex`, `all`. Simple foods/beverages are those containing a single ingredient (e.g. apple, milk) whereas complex foods contain multiple ingredients (e.g. granola bar, meal preparation). `sample_types = 'all'` will return both simple and complex foods.
    * `all_groups` is the molecular networking group(s) used for your samples.
    * `some_groups` is the molecular networking group(s) used for the reference samples.
    * `level` is an integer from 0-6 and dictates how broad or specific you want your food categories to be. Level 1 uses the most broad groupings (e.g. plant, animal). Level 6 uses the most specific groupings (e.g. strawberry, green grape). Level 0 indicates no groupings, counts will be returned for all individual reference samples. *Note: this will require matching reference sample names to the food metadata*   
   
    You can type `help(gfop.get_dataset_food_counts)` for more information about the required arguments.
6. Save food counts as csv file   

    ```
    f_counts.to_csv('food_counts.csv')
    ```
