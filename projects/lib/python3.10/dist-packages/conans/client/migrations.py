import os

from conan.api.output import ConanOutput
from conans.client.cache.cache import ClientCache
from conans.migrations import Migrator
from conans.util.files import load, save

CONAN_GENERATED_COMMENT = "This file was generated by Conan"


def update_file(file_path, new_content):
    """
    Update any file path given with the new content.
    Notice that the file is only updated whether it contains the ``CONAN_GENERATED_COMMENT``.

    :param file_path: ``str`` path to the file.
    :param new_content: ``str`` content to be saved.
    """
    out = ConanOutput()
    file_name = os.path.basename(file_path)

    if not os.path.exists(file_path):
        save(file_path, new_content)
    else:
        content = load(file_path)

        first_line = content.lstrip().split("\n", 1)[0]

        if CONAN_GENERATED_COMMENT in first_line and content != new_content:
            save(file_path, new_content)
            out.success(f"Migration: Successfully updated {file_name}")


class ClientMigrator(Migrator):

    def __init__(self, cache_folder, current_version):
        self.cache_folder = cache_folder
        super(ClientMigrator, self).__init__(cache_folder, current_version)

    def _apply_migrations(self, old_version):
        # Migrate the settings if they were the default for that version
        cache = ClientCache(self.cache_folder)
        # Time for migrations!
        # Update settings.yml
        from conans.client.conf import migrate_settings_file
        migrate_settings_file(cache)
        # Update compatibility.py, app_compat.py, and cppstd_compat.py.
        from conans.client.graph.compatibility import migrate_compatibility_files
        migrate_compatibility_files(cache)
        # Update profile plugin
        from conans.client.profile_loader import migrate_profile_plugin
        migrate_profile_plugin(cache)