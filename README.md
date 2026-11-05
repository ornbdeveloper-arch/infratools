# InfraTools Local Observability

**Uma ferramenta de monitoramento e diagnóstico de infraestrutura desenvolvida em Python.**

O InfraTools é um projeto de observabilidade local que coleta e apresenta informações sobre hardware, sistema operacional, armazenamento e interfaces de rede.

Inspirado em ferramentas de monitoramento de infraestrutura, como Zabbix, o projeto busca explorar conceitos de coleta de métricas, análise de recursos computacionais e diagnóstico de sistemas.

> Status: Em desenvolvimento.

## Funcionalidades

### Sistema

* Identificação do hostname.
* Sistema operacional e versão.
* Arquitetura do sistema.
* Usuário conectado.
* Tempo de atividade (uptime).

### Hardware

* Utilização da CPU.
* Frequência do processador.
* Núcleos físicos e lógicos.
* Utilização da memória RAM.
* Informações sobre partições e armazenamento.

### Rede

* Identificação de interfaces de rede.
* Status das interfaces.
* Velocidade e MTU.
* Endereços IPv4 e IPv6.
* Endereços MAC.

### Interface

* Apresentação das informações no terminal.
* Tabelas formatadas utilizando Rich.

## Tecnologias

| Tecnologia | Finalidade                    |
| ---------- | ----------------------------- |
| Python     | Linguagem principal           |
| psutil     | Coleta de métricas do sistema |
| Rich       | Interface no terminal         |

## Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd infratools
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Roadmap

* [ ] Monitoramento de tráfego de rede.
* [ ] Monitoramento de processos.
* [ ] Monitoramento de serviços.
* [ ] Monitoramento contínuo.
* [ ] Sistema de classificação de saúde dos componentes.
* [ ] Configuração de limites e alertas.
* [ ] Histórico de métricas.
* [ ] Geração de relatórios.
* [ ] Interface gráfica.
* [ ] Suporte ao Linux.

## Objetivo

Este projeto também possui finalidade educacional, sendo desenvolvido para aprofundar conhecimentos em Python, administração de sistemas, redes de computadores, monitoramento e observabilidade de infraestrutura.

---

Desenvolvido como projeto pessoal de estudo em infraestrutura e automação.
