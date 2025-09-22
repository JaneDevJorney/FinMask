from src.decorators import log

def test_log_ok_prints_to_stdout(capfd):
    @log()
    def plus(a, b):
        return a + b

    assert plus(1, 2) == 3
    out, err = capfd.readouterr()
    assert "plus ok" in out
    assert err == ""


def test_log_error_prints_and_raises(capfd):
    @log()
    def div(a, b):
        return a / b

    try:
        div(1, 0)
        assert False, "div should raise ZeroDivisionError"
    except ZeroDivisionError:
        out, _ = capfd.readouterr()
        assert "div error: ZeroDivisionError" in out
        assert "Inputs: (1, 0), {}" in out


def test_log_writes_to_file(tmp_path):
    log_path = tmp_path / "custom.log"

    @log(filename=str(log_path))
    def mul(a, b):
        return a * b

    assert mul(2, 5) == 10
    text = log_path.read_text(encoding="utf-8")
    assert "mul ok" in text