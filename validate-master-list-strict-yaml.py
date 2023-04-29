#!/usr/bin/env python

# Verifies that the the yaml file is valid StrictYAML syntax

from strictyaml import load, Map, Str, Int, Seq, YAMLError
# import yaml

# schema = Map({"a": Int(), Optional("b", default={}): Map(), })

with open("bss-master-list.yaml", "r") as stream:
    try:
        # person = load(stream, schema)
        person = load(stream)

        print(person)
    except YAMLError as error:
        print(error)
