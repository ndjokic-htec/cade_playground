import os
import subprocess
import unittest
from python.dummy_logger import main as dummy_logger_main
from python.random_print_library.random_print_library import get_random_word


class TestDummyLogger(unittest.TestCase):
    def test_dummy_logger(self):
        runfiles_dir = os.environ.get("RUNFILES_DIR") or os.environ.get("TEST_SRCDIR", "")
        workspace_name = os.environ.get("TEST_WORKSPACE", "_main")
        
        timestamp_provider_bin = os.path.join(
            runfiles_dir,
            workspace_name,
            "c/timestamp_provider/timestamp_provider"
        )

        output = subprocess.check_output([timestamp_provider_bin]).decode('ascii').rstrip()
        print(output)
        assert output

        word = get_random_word()
        assert isinstance(word, str)

        result = dummy_logger_main()
        assert isinstance(result, str)
        assert ":" in result


if __name__ == "__main__":
    unittest.main()