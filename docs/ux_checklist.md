

\# Knowledge Assistant - UX Review Checklist



\## 1. Clear Status

\- \[x] Loading message displayed while searching.

\- \[x] Answer displayed after successful retrieval.

\- \[x] Source filename displayed with the answer.

\- \[x] Not-found message displayed when no document matches.



\## 2. Actionable Errors

\- \[x] Invalid CSRF token explains the problem.

\- \[x] Error tells the user to refresh the page.

\- \[x] Empty question explains what the user should enter.

\- \[x] Error messages use simple language.



\## 3. Plain Language

\- \[x] Page heading is clear.

\- \[x] Input label explains what to enter.

\- \[x] Button uses a clear action word: Ask.

\- \[x] Loading message uses understandable wording.



\## 4. Keyboard Accessibility

\- \[x] Input can be reached using Tab.

\- \[x] Ask button can be reached using Tab.

\- \[x] Form can be submitted using Enter.

\- \[x] Focus outline is visible.



\## 5. Contrast

\- \[x] Body text and background contrast checked.

\- \[x] Button text and background contrast checked.

\- \[x] Answer text and background contrast checked.

\- \[x] Focus outline visibility checked.



\## 6. Security and Safe Output

\- \[x] Jinja2 autoescaping enabled.

\- \[x] Script tag is rendered as text.

\- \[x] CSRF token validated.

\- \[x] Content-Security-Policy header configured.
