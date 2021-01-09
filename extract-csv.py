#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains a function to extract CSV files from a PDF file."""
import camelot
import pandas as pd
import os

from pydata.pages_dict import pages_dict


file = "http://cwc.gov.in/sites/default/files/nrld06042019.pdf"


def extract_csv(file, pages_dict):
    """Extract CSV files."""
    path = "camelot/raw/nrld_{}_{}.csv"
    if not os.path.exists("camelot/raw"):
        os.makedirs("camelot/raw")
    for key, value in pages_dict.items():
        tables = camelot.read_pdf(file, pages=value)
        if len(tables) > 1:
            tables_list = [tables[number].df if number == 0
                           else tables[number].df[1:]
                           for number in range(len(tables))]
            tables_concat = pd.concat(tables_list)
            tables_concat.to_csv(path.format(key, value),
                                 header=False, index=False)
        else:
            tables[0].to_csv(path.format(key, value),
                             header=False, index=False)
    return None


if __name__ == '__main__':
    # code below is only executed when the module is run directly
    extract_csv(file, pages_dict)
