def return_source_file_check_metadata_status(file_type, obj_to_check):
    """
        file_type: "video||picture"
        obj_to_check: The object with all the metadata info
    """

    if file_type == "video":
        file_check = False
        try:
            if obj_to_check['QuickTime:CreateDate']:
                file_check = True
        except KeyError:
            file_check = False

        return file_check

    if file_type == "picture":
        file_check = False
        try:
            if obj_to_check['datetime_original']:
                file_check = True
        except AttributeError:
            file_check = False
        except KeyError:
            file_check = False

        return file_check