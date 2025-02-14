# 📊 Markdown Tables

Markdown allows you to create **tables** quickly and easily, making it useful for organizing structured data in your documentation.

---

## **✅ Basic Table Syntax**
To create a table, use **vertical bars (`|`)** to separate columns and **hyphens (`-`)** to define the header row.

### **Example:**
```markdown
| Name    | Age | Country |
|---------|-----|---------|
| John    | 25  | Canada  |
| Alice   | 30  | USA     |
| Bob     | 28  | UK      |
```

### **Renders as:**
| Name    | Age | Country |
|---------|-----|---------|
| John    | 25  | Canada  |
| Alice   | 30  | USA     |
| Bob     | 28  | UK      |

---

## **✅ Aligning Columns**
You can **align text** in table columns using colons (`:`).

| Alignment | Syntax Example |
|-----------|----------------|
| **Left**  | `:---`         |
| **Center** | `:---:`       |
| **Right**  | `---:`        |

### **Example:**
```markdown
| Left Aligned | Center Aligned | Right Aligned |
|:------------|:--------------:|-------------:|
| Text        | Text           | Text         |
| More Text   | More Text      | More Text    |
```

### **Renders as:**
| Left Aligned | Center Aligned | Right Aligned |
|:------------|:--------------:|-------------:|
| Text        | Text           | Text         |
| More Text   | More Text      | More Text    |

---

## **✅ Adding Row & Column Spacing**
- The number of hyphens (`-`) in the header **doesn’t matter**.
- Extra spaces around columns **don’t affect rendering**.

### **Example: 1**
```markdown
| Column 1 | Column 2 |
|---|---|
| Short | This is a longer text to show how tables adjust automatically. |
```

### **Example: 2**
You can also type it as follows but it will not impact the final output:

```markdown
| Column 1  | Column 2                                              |
|-----------|-------------------------------------------------------|
| Short     | This is a longer text to show how tables adjust.      |
| Longer    | Even longer text to illustrate column width behavior. |
```


### **Renders as:**
| Column 1 | Column 2 |
|----------|-----------------------------------------|
| Short    | This is a longer text to show how tables adjust automatically. |

---

## **✅ Using Tables in MkDocs Admonitions**
You can place tables inside **MkDocs callout boxes** for better organization.

### **Example:**
````text
??? info "Example Table Inside an Admonition"
    | Item  | Price  |
    |-------|--------|
    | Apple | $1.00  |
    | Orange| $0.80  |
````

### **Renders as:**
??? info "Example Table Inside an Admonition"
    | Item  | Price  |
    |-------|--------|
    | Apple | $1.00  |
    | Orange| $0.80  |

---

## **🚀 Summary**
| Feature                 | Syntax |
|-------------------------|--------|
| **Basic Table**         | `| Col1 | Col2 |` |
| **Column Alignment**    | `:---:`, `:---`, `---:` |
| **Admonition Table**    | `??? info` with table inside |

---

## **🎯 Key Takeaway**
- Markdown tables are simple yet **powerful** for formatting structured data.
- MkDocs supports **tables inside callout boxes (admonitions)**.