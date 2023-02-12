class UnitTest:
    def __init__(self) -> None:
        self.STATUS_NONE: str = "NONE"
        self.STATUS_FINISH: str = "FINISH"
        self.STATUS_FAILURE: str = "FAILURE"
        self.RESULT_NONE: str = "-"
        self.RESULT_PASSED: str = "PASSED"
        self.RESULT_FAILURE: str = "FAILURE"
        self._status: str = self.STATUS_NONE
        self._result: str = self.RESULT_NONE
        self._results: list[str] = []
        self.test_name: str = "Unit"
        pass

    def __str__(self) -> str:
        res: str = f"UnitTest({self.test_name}) - "
        res += f"Status: {self._status} "
        res += f"Result: {self._result}\n"
        return res
        pass

    def test(self) -> None:
        pass

    def set_status(self, status: str) -> None:
        self._status = status
        pass

    def set_result(self, result: bool) -> None:
        if result:
            self._result = self.RESULT_PASSED
        else:
            self._result = self.RESULT_FAILURE
        pass

    def get_result(self) -> bool:
        if self._result == self.RESULT_PASSED:
            return True
        return False
        pass

    def check_results(self) -> bool:
        for i in self._results:
            if not i:
                return False
                pass
            pass
        return True

    def finish_test(self) -> None:
        if not self.get_result():
            exit(1)
        else:
            exit()
        pass

    pass
