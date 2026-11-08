# Essa é minha primeira experiência prática criando testes unitários, pretendo expandir essa boa prática para mais setores do projeto.

from modules.system import get_system_info

def test_system():
    result = get_system_info()

    assert isinstance(result, dict)

# Primeiro validar se os campos retornam o dicionário como esperado.
    assert "hostname" in result
    assert "operating_system" in result
    assert "os_version" in result
    assert "architecture" in result
    assert "username" in result
    assert "uptime" in result

# Depois validar indivualmente se cada chave do dicionário retorna o tipo esperado e se nenhuma está com retorno vazio.
    assert isinstance(result["hostname"], str)
    assert result["hostname"] != ""

    assert isinstance(result["username"], str)
    assert result["username"] != ""

    assert isinstance(result["os_version"], str)
    assert result["os_version"] != ""

    assert isinstance(result["architecture"], str)
    assert result["architecture"] != ""

    assert isinstance(result["uptime"], str)
    assert result["uptime"] != ""