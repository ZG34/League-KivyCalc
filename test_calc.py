import pytest

from calc import Calculator, CalculatorError

"""
UNIT TESTING WITH PYTEST - testing each small part of the program, independently

Testing structure:
    Arrange
    Act
    Assert

"""


def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5


def test_add_fail():
    calculator = Calculator()

    with pytest.raises(CalculatorError):
        result = calculator.add("two", 3)


def test_add_fail2():
    calculator = Calculator()

    with pytest.raises(CalculatorError) as context:
        result = calculator.add("two", "four")

    # assert str(context.value) == "wrong"


def test_resists():
    calculator = Calculator()

    result = calculator.resists(100, 30)

    assert result == 77


def test_resists_fail():
    calculator = Calculator()

    result = calculator.resists("onehundred", 0)

    assert result is False


def test_resists_auto_converted():
    calculator = Calculator()

    result = calculator.resists("100", "10")

    assert result == 91


def test_effective_hp():
    calculator = Calculator()

    result = calculator.ehp(200, 1000)

    assert result == 3000

    result = calculator.ehp(5, 5)

    assert result == 5.25


def test_runner_automatic_quitting(monkeypatch):
    calculator = Calculator()

    monkeypatch.setattr("builtins.input", lambda _: "q")

    result = calculator.runner()

    assert result is None


def test_converter():
    calculator = Calculator()

    result = calculator._converter(200)

    assert result == 200


def test_converter_fail():
    calculator = Calculator()

    with pytest.raises(CalculatorError) as context:
        result = calculator._converter("two hundred")


# this would allow me to enter the required inputs manually (the following 2 blocks of code)
@pytest.fixture
def suspend_capture(pytestconfig):
    class suspend_guard:
        def __init__(self):
            self.capmanager = pytestconfig.pluginmanager.getplugin("capturemanager")

        def __enter__(self):
            self.capmanager.suspend_global_capture(in_=True)

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.capmanager.resume_global_capture()

    yield suspend_guard()


# def test_runner_manual(suspend_capture):
#     calculator = Calculator()
#
#     with suspend_capture:
#         result = calculator.runner()
#
#     # expects user to quit by pressing 'q'
#     assert result is None
