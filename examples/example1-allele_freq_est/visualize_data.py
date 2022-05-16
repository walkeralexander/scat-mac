import csv

from typing import List, Tuple, Set, Dict, Any

import matplotlib.pyplot as plt
import pandas_bokeh as pbk
import geopandas as gpd
import seaborn as sns
import pandas as pd


def visualize_freqs(fpath: str) -> None:
    # Read in the data.
    with open(fpath, "r") as fid:
        data = fid.readlines()
        data = list(map(lambda x: x.strip(), data))
    # Find the locations of the posterior & empirical estimates.
    i_pos = data.index("Posterior Mean Freqs:")
    i_emp = data.index("Empirical Freqs:")
    # Actually pull out those chunks.
    pos_freqs = data[i_pos + 1:i_emp]
    emp_freqs = data[i_emp + 1:]
    # Parse each of the chunks...
    import ipdb; ipdb.set_trace()
    pos_freqs, emp_freqs = map(parse_freqs, [pos_freqs, emp_freqs])


def parse_freqs(freqs: List[str]) -> pd.DataFrame:
    i_locii = [(i, v) for i, v in enumerate(freqs) if "Locus " in v]
    print(i_locii)
    locii_dict = {}
    while True:
        i, v = i_locii.pop(0)
        if len(i_locii) == 0:
            locii_dict.update({v: freqs[i + 1:]})
            break
        else:
            locii_dict.update({v: freqs[i + 1: i_locii[0][0]]})
    from pprint import pprint
    pprint(locii_dict)


def gen_locus_list(freqs: List[str]) -> Dict[str, List[str]]:
    I = [(i, v) for i, v in enumerate(freqs) if "Locus " in v]
    return {v: freqs[i + 1:I[j + 1][0]] for j, (i, v) in enumerate(I)}
    print(I)


if __name__ == "__main__":
    freq_fpath = "./Output_freqs"
    visualize_freqs(freq_fpath)
