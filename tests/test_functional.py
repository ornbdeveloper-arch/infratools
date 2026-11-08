# Teste de uso prático, mas de forma automatizada usando sobprocess e sys

import subprocess
import sys

def test_menu_system_option():
    result = subprocess.run(
        [sys.executable, "main.py"],
        input="4\n0\n",
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=30
    )

    assert result.returncode == 0

    assert "Informações do Sistema" in result.stdout
    assert "Hostname" in result.stdout
    assert "Sistema operacional" in result.stdout
    assert "Arquitetura" in result.stdout
    assert "Encerrando InfraTools" in result.stdout