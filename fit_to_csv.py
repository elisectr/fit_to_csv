import os
from pydantic import FilePath, DirectoryPath
from utils.load_config import load_config
from utils.process_fit_file import process_fit_file
from utils.save_module_to_csv import save_module_to_csv


def process_fit_to_csv(fit_path: FilePath, output_dir: DirectoryPath,  yaml_path: FilePath = "config.yaml") -> None:
    """
    Process a .fit file to export specific modules as .csv files based on a YAML configuration file.

    Args:
        fit_path (FilePath): Path to the .fit file.
        yaml_path (FilePath): Path to the YAML configuration file specifying modules to export.
        output_dir (DirectoryPath): Directory where output folders and CSV files will be created.

    Raises:
        ValidationError: If the configuration YAML is invalid.
        KeyError: If a specified module in the config does not exist in the FIT file.
    """
    try:
        # Load configuration from YAML
        config = load_config(yaml_path)

        # Process FIT file
        modules = process_fit_file(fit_path, config.modules_to_export)

        # for module_name in modules.keys():
        #     print(module_name)
        for module in config.modules_to_export:
            if module not in modules:
                print(f"Module '{module}' not found in the FIT file {os.path.basename(fit_path)}.")
        

        # Create the new folder for this activity
        new_dir = os.path.join(output_dir, os.path.splitext(os.path.basename(fit_path))[0])
        os.makedirs(new_dir, exist_ok=True)

        # Export each module to a CSV in its own folder
        for module_name, records in modules.items():
            save_module_to_csv(module_name, records, new_dir)

    except Exception as e:
        raise e
