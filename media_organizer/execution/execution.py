"""
TODO
"""

import csv
import json
import sys
import shutil
import os
import os.path
import hashlib
from datetime import datetime
import plum
import exiftool
from exif import Image
from media_organizer.setup_env import setup_env
from media_organizer.db_operation import db_operation
from media_organizer.file_operation import file_operation
from media_organizer.general_format import general_format
from media_organizer.report import report
from media_organizer.config import config
from media_organizer.metadata import metadata
from media_organizer.utils import utils

def import_content(src):
    """
        src: Full path to the source file
    """

    # Responsible to check if the target dir is present
    setup_env.check_target_dir()

    # load in memory all the data
    db_operation.json_model()

    SUPPORTED_EXT_PICTURE = ["jpg", "jpeg", "JPG", "JPEG"]
    SUPPORTED_EXT_VIDEO = ["mp4", "MP4", "mov", "MOV"]

    # Creating the header of the CSV file
    report.creating_the_header_of_CSV_file()

    for root, dirs, files in os.walk(src):
        for file in files:
            # print(file)
            SOURCE_FILE_PATH = root + "/" + file
            FILE_EXT = SOURCE_FILE_PATH.split(".")[-1]
            if FILE_EXT in SUPPORTED_EXT_PICTURE:
                import_picture(SOURCE_FILE_PATH)
            elif FILE_EXT in SUPPORTED_EXT_VIDEO:
                import_videos(SOURCE_FILE_PATH)
            else:
                # Printing that this format it's not supported
                general_format.formated_output("not_supported", "", SOURCE_FILE_PATH, "")

    # Saving all the files information (hash and path) to the .JSON file in
    # the home directory
    db_operation.save_db_in_disk()

    # Creating the CSV with all the operations
    report.dump_content_in_csv_file(src)


def import_videos(SOURCE_FILE_PATH):
    """
    TODO
    """
    file_type = "video"

    with exiftool.ExifToolHelper() as et:

        try:
            my_video = et.get_metadata(SOURCE_FILE_PATH)[0]
        except plum.exceptions.UnpackError:
            print("Corrupt file - {}".format(SOURCE_FILE_PATH))
            return None
        except exiftool.exceptions.ExifToolExecuteError:
            print("Empty file - {}".format(SOURCE_FILE_PATH))
            return None

        # Checking if the file has a valid metadata
        file_check = metadata.return_source_file_check_metadata_status(file_type, my_video)

        # datatime_original_from_file = time.ctime(os.path.getctime(SOURCE_FILE_PATH))
        # Expected format
        # 2014:12:20 16:13:50
        stage_file_timestamp = datetime.fromtimestamp(os.path.getctime(SOURCE_FILE_PATH))
        datatime_original_from_file = str(stage_file_timestamp).replace("-", ":").split(".")[0]

        # if len(my_video) > 0:
        if file_check:    
            try:
                if my_video['QuickTime:CreateDate']:
                    datetime_original = my_video['QuickTime:CreateDate']
            except KeyError:
                datetime_original = datatime_original_from_file

            try:
                if my_video['QuickTime:MediaCreateDate']:
                    datetime_original = my_video['QuickTime:MediaCreateDate']
            except KeyError:
                datetime_original = datatime_original_from_file

            # Setting the file name properly
            final_file_name = utils.return_final_file_name(file_type, datetime_original, SOURCE_FILE_PATH)

            year_original = datetime_original.split(":")[0]
            month_original = datetime_original.split(":")[1]

            # create dir with the year-month
            file_operation.create_structure_dir(file_type, year_original, month_original)

            # Copy the file to the destination folder
            file_operation.copy_file(file_type, SOURCE_FILE_PATH, year_original, month_original, final_file_name)
        else:
            # Setting the file type
            file_type = "video_no_exif"

            # create dir with the year-month
            file_operation.create_structure_dir(file_type, "", "")

            # Setting the file name properly
            final_file_name = utils.return_final_file_name(file_type, "", SOURCE_FILE_PATH)

            # copy_file(file_type, SOURCE_FILE_PATH, year_original, month_original, final_file_name)
            file_operation.copy_file(file_type, SOURCE_FILE_PATH, "", "", final_file_name)



def import_picture(SOURCE_FILE_PATH):
    """
    TODO
    """

    file_type = "picture"

    with open(SOURCE_FILE_PATH, 'rb') as image_file:

        try:
            my_image = Image(image_file)
        except plum.exceptions.UnpackError:
            print("Corrupt file - {}".format(SOURCE_FILE_PATH))
            return None

        # Checking if the file has a valid metadata
        file_check = metadata.return_source_file_check_metadata_status(file_type, my_image)

        # datatime_original_from_file = time.ctime(os.path.getctime(SOURCE_FILE_PATH))
        # Expected format
        # 2014:12:20 16:13:50
        stage_file_timestamp = datetime.fromtimestamp(os.path.getctime(SOURCE_FILE_PATH))
        datatime_original_from_file = str(stage_file_timestamp).replace("-", ":").split(".")[0]

        # if my_image.has_exif:
        if file_check:

            try:
                if my_image['datetime_original']:
                    datetime_original = my_image['datetime_original']
            except AttributeError:
                datetime_original = datatime_original_from_file

            year_original = datetime_original.split(":")[0]
            month_original = datetime_original.split(":")[1]

            # Setting the file name properly
            final_file_name = utils.return_final_file_name(file_type, datetime_original, SOURCE_FILE_PATH)

            # create dir with the year-month
            file_operation.create_structure_dir(file_type, year_original, month_original)

            # Copy the file to the destination folder
            file_operation.copy_file(file_type, SOURCE_FILE_PATH, year_original, month_original, final_file_name)
        else:
            # Setting the file type
            file_type = "picture_no_exif"

            # create dir with the year-month
            file_operation.create_structure_dir(file_type, "", "")

            # Setting the file name properly
            final_file_name = utils.return_final_file_name(file_type, "", SOURCE_FILE_PATH)

            # copy_file(file_type, SOURCE_FILE_PATH, "", "", final_file_name)
            file_operation.copy_file(file_type, SOURCE_FILE_PATH, "", "", final_file_name)
