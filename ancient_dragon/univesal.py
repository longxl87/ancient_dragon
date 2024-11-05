import pandas as pd
import warnings


def set_float_show(f="{:,.3f}"):
    pd.set_option('display.float_format', f)


def set_warnings(need=True):
    if need:
        warnings.filterwarnings('default')
    else:
        warnings.filterwarnings('ignore')


def set_pd_show(max_rows=500, max_columns=200, max_colwidth=70):
    pd.set_option("display.max_rows", max_rows)
    pd.set_option("display.max_columns", max_columns)
    pd.set_option("display.max_colwidth", max_colwidth)
