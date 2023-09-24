
from datetime import datetime
from config import config
import csv

def dump_content_in_csv_file(src):
    output_csv_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    path_normalized = src.replace("/","-")
    with open(config.BASE_REPORT_DIR + "/file_report_" + path_normalized + "_" + output_csv_filename + ".csv", "w", newline='') as file_csv:
        writer = csv.writer(file_csv)
        for row in config.list_files_info:
            writer.writerow(row)


def creating_the_header_of_CSV_file():
    # Creating the header of the CSV files
    list_stage = []
    list_stage.append("timestamp")
    list_stage.append("original_name")
    list_stage.append("checksum")
    list_stage.append("new_name")
    list_stage.append("file_status")
    list_stage.append("copy_state")
    config.list_files_info.append(list_stage)
