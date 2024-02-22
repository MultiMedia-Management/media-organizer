from media_organizer.config import config
from media_organizer.db_operation import db_operation
from datetime import datetime



def formated_output(state, hash_source, SOURCE_FILE_PATH, DEST_FILE_PATH):
    """
    TODO
    """
    pass

    # global list_files_info

    # file_status
    #     - new_file - ok
    #     - duplicated - ok
    #     - new_file_with_pos
    #     - not_supported

    # copy_state
    #     copy_file
    #     skip_file

    # timestamp, original_name, checksum, new_name, file_status, copy_state, final_name
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # list_files_info.append({"timestamp","original_name","checksum","new_name","file_status","copy_state","final_name"})

    if state == "duplicated":
        target_path = db_operation.return_file_path_from_db(hash_source)
        # print("{},\"{}\",{},\"{}\",{},skipped,,".format(current_time, SOURCE_FILE_PATH, hash_source, target_path, state))
        aux = (current_time, SOURCE_FILE_PATH, hash_source, target_path, state, "skipped", "",)
        config.list_files_info.append(aux)
        print(aux)

    if state == "new_file":
        # print("{},\"{}\",{},\"{}\",{},copied,,".format(current_time, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state))
        aux = (current_time, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state, "copied", "",)
        config.list_files_info.append(aux)
        print(aux)

    if state == "new_file_with_pos":
        # print("{},\"{}\",{},\"{}\",{},copied,,".format(current_time, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state))
        aux = (current_time, SOURCE_FILE_PATH, hash_source, DEST_FILE_PATH, state, "copied", "",)
        config.list_files_info.append(aux)
        print(aux)

    if state == "not_supported":
        # print("{},\"{}\",,,{},skipped,,".format(current_time, SOURCE_FILE_PATH, state))
        aux = (current_time, SOURCE_FILE_PATH, "", "", state, "skipped", "",)
        config.list_files_info.append(aux)
        print(aux)

    if state == "no_exif":
        # print("{},\"{}\",,,{},skipped,,".format(current_time, SOURCE_FILE_PATH, state))
        aux = (current_time, SOURCE_FILE_PATH, "", "", state, "skipped", "",)
        config.list_files_info.append(aux)
        print(aux)

    if state == "current_media":
        # print("{},\"{}\",,,{},skipped,,".format(current_time, SOURCE_FILE_PATH, state))
        aux = (current_time, "", hash_source, DEST_FILE_PATH, state, "nothing_to_do", "",)
        config.list_files_info.append(aux)
        print(aux)