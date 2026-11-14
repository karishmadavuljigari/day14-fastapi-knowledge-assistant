\# FastAPI Knowledge Assistant



A web-based Knowledge Assistant built using FastAPI, Jinja2, and HTMX. Users can ask questions about company policies and view matching policy information with source references.



\## Features



\- Ask questions through a simple web interface.

\- Retrieve relevant information from 20 company policy documents.

\- Display matching policy information and source filenames.

\- Handle empty and unsupported questions with clear error messages.

\- Use HTMX to update answers without reloading the page.

\- Protect form submissions using CSRF tokens.

\- Escape user input using Jinja2 autoescaping to prevent XSS.

\- Apply Content Security Policy (CSP) security headers.

\- Support keyboard navigation and visible focus indicators.



\## Technology Stack



\- Python

\- FastAPI

\- Uvicorn

\- Jinja2

\- HTMX

\- HTML, CSS, JavaScript

\- Pytest and HTTPX



\## Project Structure



```text

day14\_fastapi\_ui\_project/

├── data/

│   └── policy\_docs/

├── docs/

│   ├── screenshots/

│   ├── consulting\_practice.md

│   ├── implementation\_plan.md

│   ├── ux\_checklist.md

│   └── xss\_test\_evidence.md

├── src/

│   ├── templates/

│   │   └── partials/

│   ├── main.py

│   └── retrieval.py

├── static/

│   ├── css/

│   └── js/

├── tests/

├── .env

├── .gitignore

└── requirements.txt

```



\## Setup Instructions



\### 1. Clone the repository



```bash

git clone https://github.com/karishmadavuljigari/day14-fastapi-knowledge-assistant.git

cd day14-fastapi-knowledge-assistant

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the virtual environment



Windows CMD:



```cmd

.venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Configure environment variables



Create a `.env` file in the project root:



```text

SESSION\_SECRET=replace\_with\_a\_secure\_random\_secret

```



Use a unique secret value. Do not commit the `.env` file.



\### 6. Start the application



```bash

python -m uvicorn src.main:app --reload

```



Open the application at:



http://127.0.0.1:8000



\## Running Tests



Run the automated test suite:



```bash

python -m pytest -v

```



Run the manual XSS check:



```bash

python tests/check\_xss.py

```



\## Security Measures



\- CSRF token validation for form submissions.

\- Jinja2 automatic HTML escaping.

\- Content Security Policy response header.

\- Environment-based session secret.

\- Input validation for empty questions.



\## Retrieval Behaviour



The current implementation uses keyword-based matching against local policy text files.



It is a lightweight policy lookup application. It does not currently use semantic/vector search or an LLM to generate answers.



\## Documentation



Additional project documentation is available in the `docs/` directory:



\- Implementation plan

\- Consulting practice and acceptance tests

\- UX checklist

\- XSS test evidence

\- Application screenshots



\## License



This project was created as part of a learning assignment.

