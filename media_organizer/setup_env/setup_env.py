"""
This module is responsible for the basic configuration.
"""
import os
import json
import sys
from shutil import which
from media_organizer.config import config


def check_requirements():
    """
    TODO
    """
    binary_path = which("exiftool")
    if binary_path is None:
        print("You need to install exiftool")
        print("Please, check the link below for more details")
        print("https://github.com/MultiMedia-Management/media-organizer")
        sys.exit()


def standard_conf_file():
    """
    TODO
    """
    # print("standard conf file")
    dic_conf = {"base_dir": ""}

    if not os.path.exists(config.CONF_FILE):
        # print("conf file doesnt exist")
        with open(config.CONF_FILE, "w") as file_obj:
            file_obj.write(json.dumps(dic_conf, indent=4))
    else:
        # print("conf file is there")
        pass


def standard_report_dir():
    """
    TODO
    """

    if not os.path.isdir(config.BASE_REPORT_DIR):
        print("The directory {} it's not ready, creating it.".format(config.BASE_REPORT_DIR))
        os.makedirs(config.BASE_REPORT_DIR)


def setup_target_dir():
    """
    TODO
    """
    print("setup basedir path")
    home_dir = os.path.expanduser("~")

    base_dir = input("Please, type the path to the dir that will be used to store the data [~/my_memories]: ")
    if base_dir == "":
        base_dir = home_dir + "/my_memories"

    print(base_dir)

    if os.path.exists(base_dir) and os.path.isdir(base_dir):
        print("the dir is present")
        update_conf_file("base_dir", base_dir)
    else:
        print("please, fix the base_dir path")


def update_conf_file(field, path):
    """
    TODO
    """
    print("updating conf file")
    with open(config.CONF_FILE, "r") as file_obj:
        current_value_dic = json.load(file_obj)

    if field == "base_dir":
        current_value_dic['base_dir'] = path

        with open(config.CONF_FILE, "w") as file_obj:
            file_obj.write(json.dumps(current_value_dic, indent=4))


def view_current_conf():
    """
    TODO
    """
    # print("view the current configuration")

    try:

        with open(config.CONF_FILE, "r") as file_obj:
            aux = json.load(file_obj)
            # print(json.dumps(aux, indent=4))
            return aux
    except FileNotFoundError:
        print("Conf file {} not found. You need to inform the base-dir and crhc-cli path".format(config.CONF_FILE))


def check_target_dir():
    """
    TODO
    """
    target_dir = view_current_conf()['base_dir']
    if not os.path.exists(target_dir):
        print("The target_dir {} it's not present, please, fix it!!!".format(target_dir))
        print("")
        print("Execute './photo_organizer setup view' to check the current configuration and")
        print("'./photo_organizer setup target-dir' to setup properly the target directory.")
        print("exiting ...")
        sys.exit()

    return target_dir
