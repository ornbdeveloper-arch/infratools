# InfraTools Local Observability

Uma aplicação de monitoramento e diagnóstico de infraestrutura desenvolvida em Python, com foco na coleta, organização e apresentação de informações sobre o estado de computadores e sistemas.

## Sobre o projeto

O InfraTools Local Observability é um projeto de monitoramento local inspirado em ferramentas de observabilidade e infraestrutura, como Zabbix.

A proposta é desenvolver uma aplicação capaz de coletar informações de hardware, sistema operacional, armazenamento e rede, permitindo acompanhar o estado da máquina e identificar possíveis problemas.

O projeto tem como foco o aprendizado prático de Python, administração de sistemas, redes e monitoramento de infraestrutura.

## Objetivos

* Coletar informações de hardware e sistema operacional.
* Monitorar recursos computacionais.
* Identificar interfaces e configurações de rede.
* Avaliar condições de funcionamento da máquina.
* Organizar informações para facilitar diagnósticos.
* Desenvolver mecanismos de alertas e histórico de monitoramento.

## Funcionalidades implementadas

* [x] Identificação do sistema operacional e hostname.
* [x] Identificação do usuário e arquitetura.
* [x] Cálculo do tempo de atividade do sistema.
* [x] Monitoramento de utilização da CPU.
* [x] Identificação de núcleos físicos e lógicos.
* [x] Monitoramento de memória RAM.
* [x] Identificação de partições e utilização de armazenamento.
* [x] Identificação de interfaces de rede.
* [x] Coleta de endereços IPv4, IPv6 e MAC.
* [x] Identificação do status, velocidade e MTU das interfaces.
* [x] Apresentação das informações em tabelas no terminal.

## Tecnologias utilizadas

* **Python:** linguagem principal.
* **psutil:** coleta de informações do sistema, hardware e rede.
* **Rich:** apresentação formatada das informações no terminal.

## Estrutura do projeto

```text
infratools/
├── config/
├── logs/
├── modules/
│   ├── hardware.py
│   ├── network.py
│   └── system.py
├── monitoring/
├── reports/
├── utils/
├── main.py
├── requirements.txt
├── PROJECT.md
└── .gitignore
```

## Instalação

Clone o repositório:

```bash
git clone REPOSITORIO_DO_PROJETO
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

Com o ambiente virtual ativado, execute:

```bash
python main.py
```

## Roadmap

* [ ] Monitoramento de tráfego de rede.
* [ ] Monitoramento de processos.
* [ ] Monitoramento de serviços do sistema operacional.
* [ ] Coleta de informações adicionais de hardware.
* [ ] Sistema de classificação de saúde dos componentes.
* [ ] Configuração de limites e alertas.
* [ ] Histórico de métricas.
* [ ] Geração de relatórios.
* [ ] Interface gráfica.
* [ ] Suporte ao Linux.
* [ ] Modo de monitoramento contínuo.

## Status do projeto

Em desenvolvimento.

Esta é a primeira versão do InfraTools Local Observability, com foco na implementação dos coletores básicos e na apresentação das informações coletadas.

```

---

**Uma observação importante:** estamos documentando o que realmente existe, não o que pretendemos implementar. Por isso, as funcionalidades futuras ficam no roadmap.

E uma dica: mantenha o `PROJECT.md` como documentação técnica do projeto. Mais adiante, podemos criar um `README.md` mais visual e atraente para a página inicial do GitHub, com imagens, demonstrações e exemplos de execução.
```
