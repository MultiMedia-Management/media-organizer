"""
Module responsible for reporting purposes
"""

import csv
from datetime import datetime
from config import config


def create_script_to_remove_new_files(output_csv_filename):
    """
    Script that will help the customer to remove
    all the new and copied files in a single click/shot
    """
    new_list = []
    new_list_final_lnx = []
    new_list_final_win = []

    for row in config.list_files_info:
        if (row[4] == "new_file" and row[5] == "copied") or (row[4] == "new_file_with_pos" and row[5] == "copied"):
            new_list.append(row)

    for row in new_list:
        file_to_remove = row[1]
        new_list_final_lnx.append(["rm -f", file_to_remove])
        # print(new_list_final_lnx)

        new_list_final_win.append(["del", file_to_remove])
        # print(new_list_final_win)

    if len(new_list_final_lnx) > 0:
        with open(config.BASE_REPORT_DIR + "/delete_copied_new_files__" + output_csv_filename + ".sh", "w", newline='', encoding="utf-8") as file:
            for b in new_list_final_lnx:
                file.write("{} '{}'\n".format(b[0], b[1]))

    if len(new_list_final_win) > 0:
        with open(config.BASE_REPORT_DIR + "/delete_copied_new_files__" + output_csv_filename + ".bat", "w", newline='', encoding="utf-8") as file:
            for b in new_list_final_win:
                file.write("{} '{}'\n".format(b[0], b[1]))


def create_script_to_remove_duplicated_files(output_csv_filename):
    """
    Script that will help the customer to remove
    all the duplicated and skipped files in a single click/shot
    """
    new_list = []
    new_list_final_lnx = []
    new_list_final_win = []

    for row in config.list_files_info:
        if row[4] == "duplicated" and row[5] == "skipped":
            new_list.append(row)

    for row in new_list:
        file_to_remove = row[1]
        new_list_final_lnx.append(["rm -f", file_to_remove])
        # print(new_list_final_lnx)

        new_list_final_win.append(["del", file_to_remove])
        # print(new_list_final_win)

    if len(new_list_final_lnx) > 0:
        with open(config.BASE_REPORT_DIR + "/duplicated_skipped_files__" + output_csv_filename + ".sh", "w", newline='', encoding="utf-8") as file:
            for b in new_list_final_lnx:
                file.write("{} '{}'\n".format(b[0], b[1]))

    if len(new_list_final_win) > 0:
        with open(config.BASE_REPORT_DIR + "/duplicated_skipped_files__" + output_csv_filename + ".bat", "w", newline='', encoding="utf-8") as file:
            for b in new_list_final_win:
                file.write("{} '{}'\n".format(b[0], b[1]))


def dump_content_in_csv_file(src):
    """
    Responsible for the creation of the CSV report, which will help
    the end user to undertand what was done during the whole
    check/triage process handled by mo module
    """
    output_csv_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Replace modified in order to cover windows path,
    # now it's working on both Operating Systems.
    path_normalized = src.replace("/", "-").replace("\\", "-").replace(":", "")
    with open(config.BASE_REPORT_DIR + "/file_report_" + path_normalized + "_" + output_csv_filename + ".csv", "w", newline='', encoding="utf-8") as file_csv:
        writer = csv.writer(file_csv)
        for row in config.list_files_info:
            writer.writerow(row)

    # The calls below will create the scripts under ~/mo_reports that
    # will help the end user to delete the copied files and also the
    # duplicated files. It will be created two files, one for linux
    # ".sh" and another one for windows ".bat"
    create_script_to_remove_new_files(output_csv_filename)
    create_script_to_remove_duplicated_files(output_csv_filename)


def creating_the_header_of_CSV_file():
    """
    Just for the header creation.

    We could use the list.appened(["fields1", "field2", ...])
    However, it will reorder using the alphabetic order, which
    is not good on this case. That said, we created a local list,
    added all the elements in the order we need, and append it
    in the end.
    """
    # Creating the header of the CSV files
    list_stage = []
    list_stage.append("timestamp")
    list_stage.append("original_name")
    list_stage.append("checksum")
    list_stage.append("new_name")
    list_stage.append("file_status")
    list_stage.append("copy_state")
    config.list_files_info.append(list_stage)
