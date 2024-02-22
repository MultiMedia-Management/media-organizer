import json
import click
from media_organizer.execution import execution
from media_organizer.setup_env import setup_env
from media_organizer.db_operation import db_operation
from media_organizer.db_operation import db_reload

setup_env.standard_conf_file()
setup_env.standard_report_dir()
setup_env.check_requirements()

@click.group()
def main():
    """
    Photo Organizer! Your friend in Memories Management!
    """
    pass


@main.group()
def db():
    """
    Database Operations
    """

@db.command()
def purge():
    """
    Release all the DB information
    """
    db_operation.purge_db_in_disk()

@db.command()
def reload():
    """
    Reload the DB based on your files from target-dir
    """
    db_reload.reload_db_from_target_dir()


@main.group()
def setup():
    """
    Setup the basic configuration
    """
    pass


@setup.command()
def target_dir():
    """
    Set the target directory where your pictures will be stored
    """
    setup_env.setup_target_dir()


@setup.command()
def view():
    """
    View the current configuration
    """
    response = setup_env.view_current_conf()
    print(json.dumps(response, indent=4))


@main.group()
def import_files():
    """
    Import pictures and/or videos
    """


@import_files.command()
@click.argument('src_dir', nargs=1)
def source_dir(src_dir):
    """
    Directory where your pictures/vides are located
    """
    execution.import_content(src_dir)
