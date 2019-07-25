from main import main


TEST_DATA = "5 5 \n" \
            "1 2 N \n" \
            "LMLMLMLMM \n" \
            "3 3 E \n" \
            "MMRMMRMRRM \n"

RESULT = "1 3 N \n"\
         "5 1 E"


def test_main():
    result = main(TEST_DATA)
    assert result == result


