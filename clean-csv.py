#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains functions to correct data errors in the CSV file."""
import pandas as pd
import numpy as np
import os

from pydata.pages_dict import pages_dict
from pydata.columns import columns
from pydata.tuples import column_tuples as col_tuples
from pydata.tuples import regex_tuples as re_tuples
from pydata.tuples import regex_triple as re_triple


def read_and_clean(pages_dict, col_tuples, re_tuples, re_triple):
    """Read extracted CSV files, correct data errors, and unify dataframes."""
    data_list = []
    for key, value in pages_dict.items():
        path = "camelot/raw/nrld_{}_{}.csv"
        data = pd.read_csv(path.format(key, value))
        data.columns = columns
        data = data.replace(r"\n", " ", regex=True)
        data = clean_data(data, key, col_tuples, re_tuples, re_triple)
        # each_to_csv(data, key, value)
        data_list = make_one_table(data, data_list, key, "AN")
    return data_list


def clean_data(data, key, col_tuples, re_tuples, re_triple):
    """Replace misplaced data."""
    cnt = 0
    for col_tuple in col_tuples:
        data = right_to_left(data, key, col_tuple, col_tuples,
                             re_tuples, re_triple, cnt)
        data = left_to_right(data, key, col_tuple, col_tuples,
                             re_tuples, cnt)
        cnt += 1
    data = data.replace(r"\bnan\b", np.nan, regex=True)
    return data


def right_to_left(data, key, col_tuple, col_tuples, re_tuples,
                  re_triple, cnt):
    """Transfer misplaced data from a column to its left neighbour."""
    first_col = col_tuples[0]
    second_col = col_tuples[1]
    if col_tuple == first_col or col_tuple == second_col:
        if col_tuple == first_col:
            data["tmp_0"] = data[col_tuple[1]].astype(str).str.extract(re_triple[cnt][0].format(key),
                                                                       expand=True)
        else:
            data["tmp_0"] = data[col_tuple[1]].astype(str).str.extract(re_triple[cnt][0],
                                                                       expand=True)
        data["tmp_1"] = data["tmp_0"].str.extract(re_triple[cnt][1],
                                                  expand=True)
        if col_tuple == first_col:
            regex = re_triple[cnt][2].format(key)
            data["tmp_0"] = data["tmp_0"].str.extract(regex, expand=True)
        else:
            regex = re_triple[cnt][2]
            data["tmp_0"] = data["tmp_0"].str.extract(regex, expand=True)
        tmp_0_clean = data["tmp_0"].str.strip()
        data[col_tuple[0]] = data[col_tuple[0]].fillna(tmp_0_clean)
        if col_tuple == first_col:
            data[col_tuple[1]] = data[col_tuple[1]].replace(re_triple[cnt][0].format(key),
                                                            np.NaN, regex=True)
        else:
            data[col_tuple[1]] = data[col_tuple[1]].replace(re_triple[cnt][0][:-15]+")",
                                                            np.NaN, regex=True)
        data[col_tuple[1]] = data[col_tuple[1]].replace(re_triple[cnt][0],
                                                        np.NaN, regex=True)
        tmp_1_clean = data["tmp_1"].str.strip()
        data[col_tuple[1]] = data[col_tuple[1]].fillna(tmp_1_clean)
        data = data.drop(columns="tmp_0")
        data = data.drop(columns="tmp_1")
    return data


def left_to_right(data, key, col_tuple, col_tuples, re_tuples, cnt):
    """Transfer misplaced data from a column to its right neighbour."""
    if cnt == 0:
        data["tmp"] = data[col_tuple[0]].astype(str).str.extract(re_tuples[cnt][0],
                                                                 expand=True)
        data[col_tuple[1]] = data[col_tuple[1]].fillna(data["tmp"].str.strip())
        data[col_tuple[0]] = data[col_tuple[0]].astype(str).str.extract(re_tuples[cnt][1].format(key),
                                                                        expand=True)
        data = data.drop(columns="tmp")
        return data
    else:
        data["tmp"] = data[col_tuple[0]].astype(str).str.extract(re_tuples[cnt][0],
                                                                 expand=True)
        data[col_tuple[1]] = data[col_tuple[1]].fillna(data["tmp"].str.strip())
        data[col_tuple[0]] = data[col_tuple[0]].astype(str).str.extract(re_tuples[cnt][1],
                                                                        expand=True)
        data = data.drop(columns="tmp")
        return data


def each_to_csv(data, key, value):
    """Create CSV file for each dataframe."""
    data.to_csv("camelot/clean/nrld_{}_{}.csv".format(key, value), index=False)
    return data


def make_one_table(data, data_list, key, first_key):
    """Create a single table from all dataframes."""
    if key == first_key:
        data_list.append(data)
    else:
        data_list.append(data)
    return data_list


def create_main_csv(data_list):
    """Create a CSV file from the unified dataframes."""
    path = "camelot/clean/CWC_National-Register-of-Large-Dams_2019.csv"
    if not os.path.exists("camelot/clean"):
        os.makedirs("camelot/clean")
    data_concat = pd.concat(data_list)
    data_concat.reset_index(drop=True).to_csv(path, index=True)


if __name__ == '__main__':
    # code below is only executed when the module is run directly
    data_list = read_and_clean(pages_dict, col_tuples, re_tuples,
                               re_triple)
    create_main_csv(data_list)
