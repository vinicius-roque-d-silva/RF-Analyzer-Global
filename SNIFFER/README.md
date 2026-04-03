# 🛰️ RF Analyzer Pro: Global Enterprise Edition
> (Ou: "O Pesadelo do SysAdmin")

Bem-vindo ao **RF Analyzer Pro**. Sabe aquele momento em que a rede está lenta e ninguém sabe o porquê? Pois é, este script foi feito para você parar de dar palpites e começar a dar respostas.

Ele não só captura pacotes; ele os interroga, guarda no banco de dados e ainda te entrega um relatório mastigado diretamente no seu navegador.

---

## 🛠️ O que tem sob o capô? (Tech Stack)

Não economizamos no motor. Este projeto combina o que há de melhor para análise de dados e redes:

* **🐍 Python 3**: A alma do negócio.
* **📡 Scapy**: Para sniffar pacotes como um profissional (ou um hacker ético, você escolhe).
* **🗄️ SQLite3**: Porque arquivos TXT são para amadores. Aqui temos persistência e integridade de verdade.
* **📊 Dashboard HTML Interno**: Um servidor HTTP sob demanda para você ver os dados com estilo e clareza.
* **📈 Psutil**: Monitoramento de hardware, porque não queremos que o analyzer consuma mais recursos que a própria rede.

---

## 🚀 Funcionalidades Principais

* **`scan`**: Ativa o radar. Captura tudo o que passa pela placa de rede e joga instantaneamente no banco de dados.
* **`observe`**: Dá aquela olhada panorâmica. Quem está consumindo mais banda? Onde está o gargalo? Estatísticas em tempo real.
* **`web`**: O pulo do gato. Gera um report HTML dinâmico e abre o browser sozinho. É o momento "Uau" da apresentação.
* **`export`**: Precisa mandar os dados para o compliance ou para o chefe? Gera um arquivo `.csv` limpinho.
* **`health`**: Autodiagnóstico. Porque até quem vigia precisa ser vigiado (monitoramento de RAM e DB).

---

## 🚦 Pré-requisitos (Não pule isso!)

Para rodar essa fera, você vai precisar de:

1.  **Privilégios de Admin/Root**: Capturar pacotes de rede é coisa séria. O Sistema Operacional não vai te deixar fazer isso sem as devidas permissões.
2.  **Bibliotecas Necessárias**:
    ```bash
    pip install scapy psutil
    ```

---

## 📦 Como subir o nível da sua rede

1.  **Clone este repo**: 
    ```bash
    git clone [https://github.com/vinicius-roque-d-silva/Network-Audit-Pro.git](https://github.com/vinicius-roque-d-silva/Network-Audit-Pro.git)
    ```
2.  **Entre na pasta**: 
    ```bash
    cd Network-Audit-Pro
    ```
3.  **Execute como admin**: 
    ```bash
    python main.py
    ```
4.  **Divirta-se** (com responsabilidade, hein!).

---

## 🧠 Por que este projeto é especial?

Ele demonstra o domínio de conceitos avançados como **concorrência**, **fluxo de dados em tempo real (Streaming)** e **visualização de dados integrada**. É o tipo de ferramenta que separa quem apenas "copia código" de quem realmente **constrói soluções de infraestrutura**.

---
_Desenvolvido com ☕ e Python por Vinícius Roque._

## ⚠️ Aviso Legal
o nome do programa e meramente uma brincadeira com os programas da atualidade, dito isso este e um projeto livre use para se divertir e textar conceitos.