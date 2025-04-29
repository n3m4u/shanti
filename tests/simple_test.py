import unittest
import pandas as pd
from shanti import load_data, make_histogram

class TestShantiPackage(unittest.TestCase):

    def test_load_data(self):
        # This test assumes a sample file is available; here we mock behavior
        try:
            df = load_data(
                file_path="shanti/data/Shanti_Test_Proteins.xlsx",
                sheet_name=0,
                alpha=0.05,
                dfn=10,
                dfd=10,
                loc=0,
                scale=1,
                two_sided=False,
                fc_lim=0.25,
                l2fc_col="KO_WT_l2FC",
                pAdj_col="KO_WT_pAdj"
            )
            self.assertIsInstance(df, pd.DataFrame)
        except FileNotFoundError:
            self.skipTest("Data file not found, skipping load_data test.")

    def test_make_histogram(self):
        # Same here, we skip if file isn't available
        try:
            df = load_data(
                file_path="shanti/data/Shanti_Test_Proteins.xlsx",
                sheet_name=0,
                alpha=0.05,
                dfn=10,
                dfd=10,
                loc=0,
                scale=1,
                two_sided=False,
                fc_lim=0.25,
                l2fc_col="KO_WT_l2FC",
                pAdj_col="KO_WT_pAdj"
            )
            result = make_histogram(df, hist_col="AN_KO_Mean", title="Test", visible=True, x_axis_label="test")
            self.assertEqual(len(result), 5)
        except FileNotFoundError:
            self.skipTest("Data file not found, skipping make_histogram test.")

if __name__ == '__main__':
    unittest.main()
