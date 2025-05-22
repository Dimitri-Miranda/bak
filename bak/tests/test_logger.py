from bak.logger import log_info ,log_ok, log_warn, log_error

def test_log_info():
    msg = "teste"
    result = log_info(msg)
    assert "teste" in result  # ou uma verificação mais específica

def test_log_ok(capsys):
    log_ok("teste")
    captured = capsys.readouterr()
    assert "teste" in captured.out

def test_log_warn(capsys):
    log_warn("teste")
    captured = capsys.readouterr()
    assert "teste" in captured.out

def test_log_error(capsys):
    log_error("teste")
    captured = capsys.readouterr()
    assert "teste" in captured.out
