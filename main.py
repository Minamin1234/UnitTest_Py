from unittest_py import UnitTest_Py


# テスト対象のクラス
class SampleClass:
    def __init__(self) -> None:
        pass

    def add(self, x: int, y: int) -> int:
        return x + y
        pass

    def slicestr(self, s: str):
        return s.split()
        pass

    def logic_and(self, x: bool, y: bool) -> bool:
        return (x and y)
        pass

    pass


# テスト対象クラスをテストするクラス
class Test(UnitTest_Py.UnitTest):
    def __init__(self) -> None:
        super().__init__()
        self.test_name = "Test_01"  # テスト名
        pass

    # テスト対象クラスのそれぞれのメゾットをテストする。入力例に対する出力が想定する出力と一致すれば合格
    def test_method1(self) -> bool:
        cl: SampleClass = SampleClass()
        return cl.add(1, 1) == 2
        pass

    def test_method2(self) -> bool:
        cl: SampleClass = SampleClass()
        return cl.slicestr("Hello World") == ["Hello", "World"]
        pass

    def test_method3(self) -> bool:
        cl: SampleClass = SampleClass()
        return cl.logic_and(True, True) is True
        pass

    def test(self) -> None:
        self._results.append(self.test_method1())
        self._results.append(self.test_method2())
        self._results.append(self.test_method3())
        self.set_result(self.check_results())
        self.set_status(self.STATUS_FINISH)
        pass
    pass


# テストを行う
test: Test = Test()
test.test()
print(test)
test.finish_test()
