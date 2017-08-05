"""
extos.py

Common file operations in Python.
"""

import sys
import io
import json
import logging

def load_json_file(json_file):
    """
    JSON file loader.

    Utility that loads any number of JSON files, providing the correct
    location of the files are given in the args.

    Args:
        json_file: JSON file to load

    Returns:
        data: result of loading JSON.
    """

    python_version = (sys.version[:6])

    if '2.7' in python_version:
        with io.open(json_file, mode='rb') as input_file:
            try:
                return json.load(input_file)
            except (ValueError, FileNotFoundError) as err:
                logging.warn("Something went wrong loading JSON file: " +
                             str(err))

    elif '3.5' in python_version:
        with io.open(json_file, mode='r') as input_file:
            try:
                return json.load(input_file)
            except (FileNotFoundError) as err:
                logging.warn("Something went wrong loading the JSON file: " +
                             str(err))


def write_json_to_file(python_obj, output_path):
    """
    Take a python object and output it into a JSON file format.

    Args:
        python_obj: a python object to convert to JSON.

        output_path: absolute path to write out the JSON py object.
    """

    python_version = (sys.version[:6])

    with open(output_path, 'wb') as json_outf:
        if '2.7' in python_version:
            json_str = json.dumps(python_obj,
                                  json_outf,
                                  encoding="utf-8",
                                  indent=2)

            if isinstance(json_str, str):  # special handing in 2.7
                json_str = json_str.decode("utf-8")

        else:  # python3
            json_str = json.dumps(python_obj,
                                  json_outf,
                                  indent=2)
            json_str = json_str.encode()

        json_outf.write(json_str)
        json_outf.close()
