
import os
import secrets
import hmac
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from src.retrieval import search_policies


# Load environment variables from the .env file.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SESSION_SECRET = os.getenv("SESSION_SECRET")

if not SESSION_SECRET:
    raise RuntimeError("SESSION_SECRET is missing from the .env file")


# Configure Jinja2 templates.
templates = Jinja2Templates(
    directory=str(BASE_DIR / "src" / "templates")
)

# Create the FastAPI application.
app = FastAPI()

# Serve CSS and other static files.
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


# Add Content-Security-Policy security header.
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://unpkg.com; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "form-action 'self'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'; "
        "object-src 'none'"
    )

    return response


# Enable signed sessions using a secret key.
app.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET,
    same_site="lax",
    https_only=False,
)


# Display the Knowledge Assistant homepage.
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    # Generate a CSRF token if the session does not have one.
    if "csrf_token" not in request.session:
        request.session["csrf_token"] = secrets.token_urlsafe(32)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


# Receive a question and validate the CSRF token.
@app.post("/ask", response_class=HTMLResponse)
async def ask(
    request: Request,
    question: str = Form(...),
    csrf_token: str = Form(...),
):

    # Get the token stored in the user's session.
    session_token = request.session.get("csrf_token")

    # Reject the request if the tokens do not match.
    if not session_token or not hmac.compare_digest(
        csrf_token,
        session_token,
    ):
        return templates.TemplateResponse(
            request=request,
            name="partials/error.html",
            context={
                "request": request,
                "message": "Your security token is invalid or expired.",
                "action": "Refresh the page and submit your question again.",
            },
            status_code=403,
        )

    # Reject questions that contain only spaces.
    if not question.strip():
        return templates.TemplateResponse(
            request=request,
            name="partials/error.html",
            context={
                "request": request,
                "message": "Your question is empty.",
                "action": "Enter a question before clicking Ask.",
            },
            status_code=422,
        )

    # Search the policy documents for the user's question.
    matches = search_policies(question)

    # Prepare the answer and its source citation.
    if matches:
        answer = matches[0]["content"]

        sources = [
            {"source": matches[0]["source"]}
        ]
    else:
        answer = (
            "I couldn't find information about this question "
            "in the available policy documents. "
            "Try asking about leave, attendance, travel, "
            "or other company policies."
        )

        sources = []

    return templates.TemplateResponse(
        request=request,
        name="partials/answer.html",
        context={
            "request": request,
            "question": question,
            "answer": answer,
            "sources": sources,
        },
    )
