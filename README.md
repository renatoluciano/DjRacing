# 🏎️ DjRacing - Simulador de Corrida

Um simulador de corrida simples construído com **Django** e **JavaScript** puro. O projeto simula o movimento de um carro e registra o tempo de volta no banco de dados ao cruzar a linha de chegada.

## 🚀 Funcionalidades

- 🚗 Movimentação aleatória do carro simulando aceleração.
- ⏱️ Cronômetro preciso em milissegundos usando `performance.now()`.
- 🏷️ Possibilidade de inserir um nome personalizado para o veículo.
- 🏆 Painel de Recordes (Leaderboard) atualizado dinamicamente.
- 🗑️ Opção para resetar a tabela de recordes.

## 🛠️ Tecnologias Utilizadas

- **Python** e **Django** (Backend e API)
- **SQLite** (Banco de dados padrão do Django)
- **HTML5**, **CSS3** e **JavaScript** (Frontend e animações)
- **Git** e **GitHub** (Controle de versão)

## 🏁 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto em sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd NOME_DO_REPOSITORIO
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

Acesse `http://127.0.0` no seu navegador para jogar!
