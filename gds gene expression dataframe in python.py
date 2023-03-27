import GEOparse

gse2 = GEOparse.get_GEO(geo="GSE1563", destdir="./")

gse_data = gse2.pivot_samples('VALUE')

gse_data

#with gds dataset instead of gse

import GEOparse
import pandas as pd

gds = GEOparse.get_GEO(geo="GDS5614", destdir="./")
data = gds.table
data

data_col = data.filter(regex=("GSM.*"))

data_col2 = data_col[data_col.filter(regex=("GSM*")) != 'NaN']
data_col2
