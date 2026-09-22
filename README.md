# Diet Calc

[![Tests](https://github.com/ViniOcCode/diet-calc/actions/workflows/tests.yml/badge.svg)](https://github.com/ViniOcCode/diet-calc/actions/workflows/tests.yml)

A Flask web application that turns a small set of personal measurements into educational estimates for daily energy expenditure, BMI, water intake, and macronutrient distribution.

**Live demo:** [diet-calc.onrender.com](https://diet-calc.onrender.com)

![Diet Calc interface](https://imgur.com/gJj1EvK.png)

## Why it exists

Diet Calc was developed as a university extension project connected to **UN Sustainable Development Goal 3 — Good Health and Well-Being**. The project applies backend development, form validation, server-side rendering, and automated calculation tests to an accessible health-education use case.

> [!IMPORTANT]
> Diet Calc provides general educational estimates. It does not diagnose conditions, prescribe a diet, or replace advice from a physician, registered dietitian, or other qualified health professional.

## Features

- Calculates an activity-adjusted Basal Metabolic Rate estimate using the Mifflin-St Jeor equation.
- Calculates BMI and displays its corresponding category.
- Estimates daily water intake using age-based factors.
- Distributes estimated calories across protein, fat, and carbohydrates.
- Adjusts the calorie estimate for maintenance, cutting, or bulking goals.
- Validates accepted age, height, weight, activity, goal, and sex values.
- Requires no account and stores no submitted health data.
- Includes automated tests for calculation and validation behavior.

## Request flow

```text
Browser form
    -> Flask-WTF validation
    -> Person calculation model
    -> Structured summary
    -> Jinja-rendered results
```

## Technology stack

- Python 3.12+
- Flask 3
- Flask-WTF and WTForms
- Jinja2
- Bootstrap and custom CSS
- Waitress for the production entry point
- Pytest and GitHub Actions

## Running locally

```bash
git clone https://github.com/ViniOcCode/diet-calc.git
cd diet-calc
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install and run:

```bash
pip install -r requirements.txt
python main.py
```

Open [http://localhost:8080](http://localhost:8080).

For deployed environments, set a strong random `SECRET_KEY`. Local development receives an ephemeral fallback key, so no reusable secret is stored in the repository.

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

The test suite covers worked calculation examples, the public result structure, boundary validation, and rejected activity factors.

## Project structure

```text
app/
  calculator.py        Calculation and domain validation
  main/forms.py        Input fields and form validation
  main/routes.py       Flask routes and result orchestration
  templates/           Jinja pages
  static/              CSS assets
  tests/               Calculation tests
main.py                 Application entry point
config.py               Runtime configuration
```

<details>
<summary><strong>Português</strong></summary>

## Sobre o projeto

O Diet Calc é uma aplicação Flask que gera estimativas educacionais de gasto energético diário, IMC, consumo de água e distribuição de macronutrientes. O projeto foi desenvolvido como atividade de extensão universitária relacionada à **ODS 3 — Saúde e Bem-Estar**.

> [!IMPORTANT]
> Os resultados são estimativas gerais. A aplicação não realiza diagnósticos, não prescreve dietas e não substitui a orientação de nutricionista, médico ou outro profissional de saúde qualificado.

### Funcionalidades

- Estimativa da Taxa Metabólica Basal ajustada ao nível de atividade.
- Cálculo do IMC e exibição da categoria correspondente.
- Estimativa de consumo diário de água por faixa etária.
- Distribuição de proteínas, gorduras e carboidratos.
- Ajuste para manutenção, cutting ou bulking.
- Validação dos dados aceitos e testes automatizados.
- Uso sem cadastro e sem armazenamento dos dados informados.

### Executando

Crie um ambiente virtual, instale `requirements.txt`, execute `python main.py` e acesse [http://localhost:8080](http://localhost:8080).

Para executar os testes, instale `requirements-dev.txt` e rode `pytest -q`.

</details>
