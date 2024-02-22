"""
Module responsible for all the files operation
"""
import hashlib
import os
import shutil
from media_organizer.setup_env import setup_env
from media_organizer.db_operation import db_operation
from media_organizer.config import config
from media_organizer.general_format import general_format


def return_hash_from_file(FILE_PATH):
    """
    TODO
    """
    with open(FILE_PATH, "rb") as f1:
        digest_source = hashlib.file_digest(f1, "sha256")
        hash_from_file = digest_source.hexdigest()
    return hash_from_file


def create_structure_dir(file_type, year, month):
    """
    TODO
    """
    base_dir = setup_env.view_current_conf()['base_dir']

    if file_type == "video":
        DESTINATION_DIR = base_dir + "/" + "MO_DIR" + "/" + year + "/" + month + "/" + "VIDEO"
    if file_type == "picture":
        DESTINATION_DIR = base_dir + "/" + "MO_DIR" + "/" + year + "/" + month + "/" + "PICTURE"
    if file_type == "picture_no_exif":
        DESTINATION_DIR = base_dir + "/" + "MO_DIR" + "/" + "UNKNOWN" + "/" + "PICTURE"
    if file_type == "video_no_exif":
        DESTINATION_DIR = base_dir + "/" + "MO_DIR" + "/" + "UNKNOWN" + "/" + "VIDEO"

    if not os.path.isdir(DESTINATION_DIR):
        print("The directory {} it's not ready, creating it.".format(DESTINATION_DIR))
        os.makedirs(DESTINATION_DIR)


def copy_file(file_type, SOURCE_FILE_PATH, year, month, final_file_name):
    """
    TODO
    """

    # global db_in_memory

    base_dir = setup_env.view_current_conf()['base_dir']

    if file_type == "video":
        DEST_FILE_PATH = base_dir + "/" + "MO_DIR" + "/" + year + "/" + month + "/" + "VIDEO" + "/" + final_file_name
    if file_type == "picture":
        DEST_FILE_PATH = base_dir + "/" + "MO_DIR" + "/" + year + "/" + month + "/" + "PICTURE" + "/" + final_file_name
    if file_type == "picture_no_exif":
        DEST_FILE_PATH = base_dir + "/" + "MO_DIR" + "/" + "UNKNOWN" + "/" + "PICTURE" + "/" + final_file_name
    if file_type == "video_no_exif":
        DEST_FILE_PATH = base_dir + "/" + "MO_DIR" + "/" + "UNKNOWN" + "/" + "VIDEO" + "/" + final_file_name

    hash_source = return_hash_from_file(SOURCE_FILE_PATH)

    # if db_operation.check_value_in_db(hash_source, SOURCE_FILE_PATH):
    if db_operation.check_value_in_db(hash_source):
        # print("Found in the db. {} and {}".format(hash_source, SOURCE_FILE_PATH))
        general_format.formated_output("duplicated", hash_source, SOURCE_FILE_PATH, "")
    else:
        # print("Not found in the db. {} and {}".format(hash_source, SOURCE_FILE_PATH))

        # Checking for the file currently in the target directory
        if os.path.isfile(DEST_FILE_PATH):
            count = 0
            filename = DEST_FILE_PATH.split("/")[-1].split(".")[0]
            extension = DEST_FILE_PATH.split("/")[-1].split(".")[1]
            while True:
                count = count + 1
                new_filename = filename + "_" + str(count) + "." + extension
                DEST_FILE_NEW_PATH = DEST_FILE_PATH.replace(filename + "." + extension, new_filename)

                if not os.path.isfile(DEST_FILE_NEW_PATH):
                    # print("copy file from {} to {}".format(SOURCE_FILE_PATH, DEST_FILE_NEW_PATH))
                    general_format.formated_output("new_file_with_pos", hash_source, SOURCE_FILE_PATH, DEST_FILE_NEW_PATH)
                    shutil.copy(SOURCE_FILE_PATH, DEST_FILE_NEW_PATH)
                    # db_in_memory.append({'filename': DEST_FILE_PATH, 'hash': hash_destination})
                    config.db_in_memory.append({'filename': DEST_FILE_NEW_PATH, 'hash': hash_source})
                    return False
        else:
            # Adding the file when the same it's a brand new version
            # print("copy file from {} to {}".format(SOURCE_FILE_PATH, DEST_FILE_PATH))
            general_format.formated_output("new_file", hash_source, SOURCE_FILE_PATH, DEST_FILE_PATH)
            shutil.copy(SOURCE_FILE_PATH, DEST_FILE_PATH)
            # hash_destination = return_hash_from_file(DEST_FILE_PATH)
            config.db_in_memory.append({'filename': DEST_FILE_PATH, 'hash': hash_source})
