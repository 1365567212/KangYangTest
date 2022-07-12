import pytest

class TestCase:
    def test_01(self):
        print('第一条用例')
        assert 1 == 1

    def test_02(self):
        print('第二条用例')
        assert 2 == 3

if __name__ == '__main__':
