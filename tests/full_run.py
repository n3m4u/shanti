# Example usage
import shanti
from shanti import load_data, make_histogram, create_interactive_dashboard

# Load data with custom parameters
source = load_data(
    file_path = "Shanti_Test_Proteins.xlsx",
    sheet_name=0,
    alpha = 0.05,
    dfn = 10,
    dfd = 10,
    loc = 0,
    scale = 1,
    two_sided=False,
    fc_lim = 0.25,
    l2fc_col = "KO_WT_l2FC",
    pAdj_col = "KO_WT_pAdj"
)

hist1, hist1_data_filtered, hist1_bin_edges_log, hist1_bottoms, hist1_bar_height = make_histogram(source=source, hist_col="AN_KO_Mean", title= "KO dTAG", visible=True, x_axis_label="protein count")

hist2, hist2_data_filtered, hist2_bin_edges_log, hist2_bottoms, hist2_bar_height = make_histogram(source, hist_col="AN_WT_Mean", title= "DMSO", visible=True, x_axis_label="protein count")

dashboard_path = create_interactive_dashboard(
    source,
    l2fc_col="KO_WT_l2FC",
    pAdj_col="KO_WT_pAdj",
    html_title="Shanti Tool",
    color_column="color",
    volcano_title="KO dTAG vs DMSO Comparison",
    volcano_tools="pan, box_zoom, wheel_zoom, tap, box_select, reset, save",
    plot2=hist1,
    plot3=hist2,
    hist1_data_filtered=hist1_data_filtered,
    hist2_data_filtered=hist2_data_filtered,
    hist1_bin_edges_log=hist1_bin_edges_log,
    hist2_bin_edges_log=hist1_bin_edges_log,
    hist1_bottoms=hist1_bottoms,
    hist2_bottoms=hist1_bottoms,
    hist1_bar_height = hist1_bar_height,
    hist2_bar_height = hist1_bar_height,
    hist1_col="AN_KO_Mean",
    hist2_col="AN_WT_Mean",
    table_columns=["UniProtID", "Gene", "Description", "Peptides", "PeptidesU", "PSMs"],
    peptides_file="Shanti_Test_PeptideGroups.xlsx",
    peptide_columns=["UniProtID", "Sequence", "ProteinGroups", "Proteins", "PSMs", "Position", "MissedCleavages", "QuanInfo"],
    output_path="dashboard.html"
)

print(f"✅{dashboard_path} succesfully created!")


