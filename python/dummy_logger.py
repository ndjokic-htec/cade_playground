import os
import subprocess
from python.random_print_library.random_print_library import get_random_word


def main():
    runfiles_dir = os.environ.get("RUNFILES_DIR") or os.environ.get("TEST_SRCDIR", "")
    workspace_name = os.environ.get("TEST_WORKSPACE", "_main")
    
    timestamp_provider_bin = os.path.join(
        runfiles_dir,
        workspace_name,
        "c/timestamp_provider/timestamp_provider"
    )
    
    output = subprocess.check_output([timestamp_provider_bin]).decode('ascii').rstrip()
    return f"{output}: {get_random_word()}"


if __name__ == "__main__":
    print(main())