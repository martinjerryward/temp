# 💻 Markdown Code Blocks

Markdown provides powerful ways to display and format **code snippets**, making it an essential tool for documentation and technical writing.

---

## **✅ Inline Code**
To include small code snippets inside a sentence, use **single backticks (` ` )**.

### **Example:**
```markdown
Use the `print()` function in Python.
```

### **Renders as:**
Use the `print()` function in Python.

---

## **✅ Fenced Code Blocks**
For multi-line code blocks, use **triple backticks (` ``` `)** or **triple tildes (` ~~~ `)**.

### **Example: Python**

````text
```python
print("Hello, World!")
```
````


### **Renders as:**
```python
print("Hello, World!")
```

---

## **✅ Syntax Highlighting**
To add syntax highlighting, specify the programming language after the opening triple backticks.

### **Example (Python Code Block):**
````text
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Martin"))
```
````

### **Renders as:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Martin"))
```

🚀 **MkDocs Material** automatically applies syntax highlighting based on the language specified.

---

## **✅ Code Blocks with Line Numbers**
You can **enable line numbers** by using the `linenums` option.

### **Example:**
````text
```python linenums="1"
def add(a, b):
    return a + b

print(add(2, 3))
```
````

### **Renders as:**
```python linenums="1"
def add(a, b):
    return a + b

print(add(2, 3))
```

---

## **✅ Highlight Specific Lines**
To emphasize important lines in a code block, use `hl_lines="X Y"` where **X, Y** are the lines to highlight.

### **Example:**
````text
```python hl_lines="2 4" linenums="1"
def add(a, b):
    return a + b  # Highlighted line

print(add(2, 3))  # Highlighted line
```
````

### **Renders as:**
```python hl_lines="2 4" linenums="1"
def add(a, b):
    return a + b  # Highlighted line

print(add(2, 3))  # Highlighted line
```

---

## **🚀 Summary**

| Feature | Syntax |
|---------|--------|
| **Inline Code** | `` `code` `` |
| **Basic Code Block** | `` ``` `` or `~~~` |
| **Syntax Highlighting** | `` ```python `` |
| **Line Numbers Only** | `` ```python linenums="1" `` |
| **Highlighting Lines** | `` ```python hl_lines="X Y" `` |
| **Both Features** | `` ```python linenums="1" hl_lines="X Y" `` |

---

## 🎯 Key Takeaway
"In Markdown, you use triple backticks \```  create code blocks, and you can specify a language (e.g., python) for syntax highlighting."