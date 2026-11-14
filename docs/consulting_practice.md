\# Day 14 - Consulting Practice



\## 1. Confirmed Requirements



Based on the agreed requirements, the Knowledge Assistant should:



\- Provide a web page where employees can ask questions about company policies.

\- Retrieve relevant information from the available policy documents.

\- Display the answer along with its source filename.

\- Display a clear message when information cannot be found.

\- Validate empty questions.

\- Protect requests using CSRF tokens.

\- Escape user input to prevent cross-site scripting (XSS).

\- Provide an accessible interface with keyboard navigation and visible focus indicators.



\## 2. Suggestions



The following improvements can be considered as future enhancements:



\- Replace basic keyword matching with semantic search using embeddings.

\- Generate concise answers using an LLM while retaining source citations.

\- Add document upload and document-management functionality.

\- Add authentication and role-based access to restricted policy documents.

\- Add search filters and feedback options.

\- Improve the answer display by showing relevant passages instead of entire documents.



These are suggestions and are not part of the current implementation.



\## 3. Risks and Caveats



\- Current retrieval uses keyword matching, so it may miss questions expressed using different words.

\- The application displays the content of the best-matching document; it does not generate an AI-summarized answer.

\- The current implementation uses local text files as its knowledge source.

\- The application does not yet implement user authentication or role-based document permissions.

\- A Content-Security-Policy is configured, but deployment should use HTTPS and secure session-cookie settings.

\- Retrieval quality should be tested with a larger set of representative questions.



\## 4. Acceptance Tests



| ID | Test scenario | Expected result |

|---|---|---|

| AT-01 | Open the homepage | Knowledge Assistant page loads |

| AT-02 | Ask about leave policy | Matching policy content and source appear |

| AT-03 | Ask about attendance policy | Matching policy content and source appear |

| AT-04 | Submit only spaces | Empty-question error appears |

| AT-05 | Ask about an unavailable policy | Not-found message appears without a source |

| AT-06 | Submit an invalid CSRF token | Request is rejected |

| AT-07 | Submit a script-tag payload | Script is escaped and not executed |

| AT-08 | Navigate using the keyboard | Input and button can be reached and used |

| AT-09 | Inspect the response headers | Content-Security-Policy header is present |

| AT-10 | Load the stylesheet | CSS loads successfully |



\## 5. Scope Clarification



The current delivery covers the basic Knowledge Assistant interface, keyword-based document retrieval, security controls, and usability checks.



Semantic retrieval, LLM-generated answers, authentication, and role-based permissions are potential future enhancements rather than completed features.
