import pandas as pd

import sys
sys.path.insert(0, "../gfop/")

import get_food_counts

def test():
    input_net = "data/mol_net.tsv"
    input_meta = "data/sample_metadata.csv"

    test_output = pd.read_csv("data/food_counts_noLevels.csv", index_col=0)

    f_counts = get_food_counts.get_dataset_food_counts(gnps_network = input_net,
                                            metadata = input_meta,
                                            filename_col = 'filename',
                                            sample_types = 'all',
                                            all_groups = ['G1'],
                                            some_groups = ['G4'],
                                            level = 0)

    pd.testing.assert_frame_equal(test_output, f_counts)

if __name__ == "__main__":
    test()
    print("Passed")
