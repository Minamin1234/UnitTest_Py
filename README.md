# UnitTest_Py
## 概要
Pythonプログラムの単体テストを行うためのテストプログラム。

## サンプル
```py
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


# テスト対象をテストするクラス
class Test(UnitTest_Py.UnitTest):
    def __init__(self) -> None:
        super().__init__()
        self.test_name = "Test_01"  # テスト名
        pass

    # テスト対処クラスのそれぞれのメゾットをテストする。入力例と出力例が一致すれば合格
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

```
## 使用法
例として、以下のようなクラスを単体テストにかけるとします。
```py
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
```

`UnitTest_Py.UnitTest`クラスを継承してテスト用クラスを作成します。
```py
from unittest_py import UnitTest_Py


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
```
テストするクラスのメゾットをそれぞれテストを行う関数を追加実装し、`test()`関数でそれらの結果を配列に追加します。テスト後にはテスト結果と状態を更新します。
```py
def test(self) -> None:
    self._results.append(self.test_method1())
    self._results.append(self.test_method2())
    self._results.append(self.test_method3())
    self.set_result(self.check_results())
    self.set_status(self.STATUS_FINISH)
    pass
```

あとは、テストプログラムが実行されるように実装するだけです。
```py
# テストを行う
test: Test = Test()
test.test()
print(test)
test.finish_test()

```

```powershell
> python ./main.py
UnitTest(Test_01) - Status: FINISH Result: PASSED
```

テストに合格すれば`Result`が`PASSED`になり、不合格であれば`FAILURE`を表示します。また、不合格だった場合は終了コード`1`を返します。