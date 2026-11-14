\# Day 14 - XSS Security Test Evidence



\## 1. Objective



Verify that user-submitted HTML and JavaScript are safely escaped and are not executed by the application.



\## 2. Test Input



The following script-tag payload was submitted as a question:



```html

<script>alert("XSS")</script>

```



\## 3. Test Method



The manual test was performed using:



```cmd

python tests\\check\_xss.py

```



The test script:

1\. Opens the application homepage.

2\. Retrieves the CSRF token.

3\. Submits the script-tag payload.

4\. Checks whether the response contains escaped HTML.

5\. Checks whether an executable script tag is present.



\## 4. Actual Test Result



```text

Status: 200

Script escaped: True

Executable script tag present: False

```



The response displayed the submitted payload as escaped text:



```html

\&lt;script\&gt;alert(\&#34;XSS\&#34;)\&lt;/script\&gt;

```



\## 5. Conclusion



The XSS test passed.



Jinja2 automatic HTML escaping converted the script-tag characters into harmless text. The response did not contain an executable script element.



This demonstrates that the tested user input is safely displayed rather than executed.
