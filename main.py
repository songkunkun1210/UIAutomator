import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v'])
    os.system("allure generate ./temps -o ./reports --clean")
