"""
Module responsible to handle all the operations regarding
to the DB/JSON file.
"""

# global db_in_memory

import json
import os
from config import config
# from setup_env import setup_env


# def check_value_in_db(hash_source, SOURCE_FILE_PATH):
def check_value_in_db(hash_source):
    """
    This will return True if the hash was found in the structure,
    and False and the hash was not found.
    """

    # Checking the # of operations before dump the data
    # from memory to file (JSON)
    if config.count_valid_insert_operation >= config.max_retries_before_dump_the_data:
        save_db_in_disk()
        config.count_valid_insert_operation = 0

    cont = 0
    for element in config.db_in_memory:
        # print("here")
        if element["hash"] == hash_source:
            # print("hash {} found in {}".format(hash_source, SOURCE_FILE_PATH))
            cont = cont + 1
            # return

    if cont == 0:
        config.count_valid_insert_operation = config.count_valid_insert_operation + 1
        return False
    return True


def return_file_path_from_db(hash_source):
    """
    TODO
    """
    for element in config.db_in_memory:
        # print("here")
        if element["hash"] == hash_source:
            return element["filename"]
        return None


def json_model():
    """
    TODO
    """

    try:
        with open(config.JSON_DB, "r", encoding="utf-8") as file_obj:
            config.db_in_memory = json.load(file_obj)
            # print(json.dumps(aux, indent=4))
    except FileNotFoundError:
        # print("Conf file {} not found. You need to inform the base-dir and crhc-cli path".format(CONF_FILE))
        pass


def save_db_in_disk():
    """
    It will save the information from memory to disk.
    """
    with open(config.JSON_DB, "w", encoding="utf-8") as file_obj:
        file_obj.write(json.dumps(config.db_in_memory, indent=4))


def purge_db_in_disk():
    """
    Removing the JSON file "~/.mo_hash.json" used as a DB at this moment.
    """
    aux = input("Are you sure you would like to purge your db? (y/n): ")

    if aux == "y":

        # Just removing the file
        if os.path.isfile(config.JSON_DB):
            os.remove(config.JSON_DB)

    else:
        print("Leaving your DB untouched!")
