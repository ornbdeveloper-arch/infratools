import pytest
from modules.system import get_system_info

def test_system():

    result = get_system_info()

   
    assert isinstance(result, dict)
    assert "hostname" in result
    assert "operating_system" in result
    assert "os_version" in result
    assert "architecture" in result
    assert "username" in result
    assert "uptime" in result

    
    assert isinstance(result['hostname'], str)
    assert result['hostname'] != ""

    assert isinstance(result['username'], str)
    assert result['username'] != ""