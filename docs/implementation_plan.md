

\# Day 14 - Knowledge Assistant Implementation Plan



\## 1. Objective



Build a simple Knowledge Assistant web application that allows users to ask questions about company policy documents and view relevant answers with source filenames.



\## 2. Requirements



\- Build the user interface using HTML and Jinja2 templates.

\- Use FastAPI to handle HTTP requests.

\- Use HTMX to submit questions without a full-page reload.

\- Retrieve information from the available policy text files.

\- Display the answer and its source filename.

\- Display a clear message when no matching information is found.

\- Validate empty questions.

\- Implement CSRF protection.

\- Enable Jinja2 automatic HTML escaping.

\- Configure Content-Security-Policy security headers.

\- Provide accessible labels, keyboard navigation, and visible focus indicators.



\## 3. Implementation Approach



\### Phase 1: Project Setup

\- Create a separate Day 14 project.

\- Create and activate a Python virtual environment.

\- Install the required Python packages.

\- Organize source code, templates, static files, tests, and documentation.



\### Phase 2: Backend Development

\- Create the FastAPI application.

\- Configure Jinja2 templates and static file serving.

\- Load the policy documents.

\- Implement keyword-based policy retrieval.

\- Add question validation and response handling.



\### Phase 3: Frontend Development

\- Create the Knowledge Assistant homepage.

\- Build the question submission form.

\- Integrate HTMX for partial-page updates.

\- Display answers, source filenames, and error messages.

\- Add CSS for layout, readability, and visible focus indicators.



\### Phase 4: Security

\- Configure signed sessions.

\- Generate and validate CSRF tokens.

\- Use Jinja2 automatic HTML escaping.

\- Configure Content-Security-Policy headers.

\- Test script-tag input to verify safe output.



\### Phase 5: Testing and UX Review

\- Write automated tests for the application.

\- Test valid and invalid CSRF tokens.

\- Test XSS protection.

\- Verify static file loading and security headers.

\- Test empty and unknown questions.

\- Review keyboard accessibility and visual contrast.

\- Document the UX review.



\## 4. Acceptance Criteria



\- The homepage loads successfully.

\- Users can submit questions.

\- Matching policy information is displayed with its source filename.

\- Unknown questions return a clear not-found response.

\- Empty questions display an actionable error.

\- Invalid CSRF tokens are rejected.

\- Script tags are escaped and not executed.

\- Security headers are present.

\- Keyboard navigation and visible focus work.

\- Automated tests pass.



\## 5. Current Implementation Notes



Policy retrieval currently uses basic keyword matching against local text documents. It is not semantic search and does not use an LLM to generate answers.



The application displays the content of the best-matching policy document rather than generating a summarized response.
