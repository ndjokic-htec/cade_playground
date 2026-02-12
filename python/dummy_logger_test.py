import subprocess
from python.random_print_library.random_print_library import get_random_word

def test_dummy_logger_runs():
    
    output = subprocess.check_output(["/app/timestamp_provider"]).decode('ascii').rstrip()
    assert output

    word = get_random_word()
    assert isinstance(word, str)