# Por sua vez aqui está meu primeiro teste de integração nesse projeto, unindo a função collector as fontes de dados.

from monitoring.collector import collect_hardware

def test_collect_hardware():
    result = collect_hardware()

    assert isinstance(result, dict)

    assert "cpu" in result
    assert "ram" in result
    assert "disk" in result