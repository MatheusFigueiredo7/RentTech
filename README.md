# 🛠️ RentTech - Sistema de Gerenciamento de Locação de Equipamentos

## 📋 Respostas ao Desafio

### 1. Qual é o tema do seu sistema?
O **RentTech** é uma plataforma para o gerenciamento de inventário e locação de equipamentos audiovisuais, como câmeras, drones e kits de iluminação. O sistema foi criado para substituir o exemplo de "Tarefas Acadêmicas" utilizado em aula, focando em um novo domínio.

### 2. Quais são as funcionalidades esperadas?
* **Gestão de Inventário:** Cadastro e edição de equipamentos via painel administrativo (Django Admin).
* **Controle de Disponibilidade:** Monitoramento do estado de conservação e disponibilidade de cada item.
* **API de Consulta Geral:** Endpoint que retorna a lista completa de equipamentos cadastrados em formato JSON.
* **API de Consulta Filtrada:** Endpoint específico que aplica um filtro para exibir apenas equipamentos com status "Disponível".

### 3. Quais serão os dados armazenados?
Para cada entidade "Equipamento" no núcleo do sistema, armazenamos:
* **Nome:** Identificação textual do produto.
* **Especificações:** Descrição detalhada técnica (TextField).
* **Status:** Campo de controle utilizando o parâmetro `choices` (Disponível, Alugado, Manutenção, Indisponível).
* **Valor da Diária:** Campo numérico para o preço de locação.
* **Data de Aquisição:** Registro cronológico da entrada do item no estoque.

---

## 📡 Endpoints da API

O Back-end atua como o cérebro do sistema, devolvendo as seguintes respostas em JSON:

* **Listagem Geral:** `GET /api/equipamentos/`
* **Filtro de Disponíveis:** `GET /api/equipamentos/disponiveis/`

---
