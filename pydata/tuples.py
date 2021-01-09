# -*- coding: utf-8 -*-

column_tuples = [("PIC", "Name of Dam"),
                 ("Latitude", "Longitude"),
                 ("Longitude", "Year of Completion"),
                 ("River Basin", "River"),
                 ("Dam Type", "Height above Lowest Foundation Level"),
                 ("Dam Length", "Volume Content of Dam"),
                 ("Volume Content of Dam", "Gross Storage Capacity"),
                 ("Gross Storage Capacity", "Reservoir Area"),
                 ("Reservoir Area", "Effective Storage Capacity"),
                 ("Purpose", "Designed Spillway Capacity")]

regex_tuples = [(r"( [\w \.\,\(\)\-\d\uFFFD]+)", r"({}\d\d\w\w\d\d\d\d)"),
                (r"( \d?\d° ?\d?\d \' ?\d?\d\.?\d*\")", r"(\d?\d° ?\d?\d \' ?\d?\d\.?\d*\")"),
                (r"(\d\d\d\d)", r"(\d?\d° ?\d?\d \' ?\d?\d\.?\d*\")"),
                (r"( [\w ]+)", r"(Godavari|Narmada|Brahmaputra|Subarnarekha|[\w ]+)"),
                (r"( \d+\.?\d*)", r"(\D+)"),
                (r"( \d+\.?\d*)", r"(\d+\.?\d*)"),
                (r"( \d+\.?\d*)", r"(\d+\.?\d*)"),
                (r"( \d+\.?\d*)", r"(\d+\.?\d*)"),
                (r"( \d+\.?\d*)", r"(\d+\.?\d*)"),
                (r"( \d+\.?\d*)", r"([\w/]+)")]

regex_triple = [(r"({}\d\d\w\w\d\d\d\d [\w \.\,\(\)\-\d\uFFFD]+)",
                 r"( [\w \.\,\(\)\-\d\uFFFD]+)",
                 r"({}\d\d\w\w\d\d\d\d)"),
                (r"(\d?\d° ?\d?\d \' ?\d?\d\.?\d*\" \d?\d° ?\d?\d \' ?\d?\d\.?\d*\" ?\d?\d?\d?\d?)",
                 r"( \d?\d° ?\d?\d \' ?\d?\d\.?\d*\" ?\d?\d?\d?\d?)",
                 r"(\d?\d° ?\d?\d \' ?\d?\d\.?\d*\")")]
