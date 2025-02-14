# 📷 Images

## **Understanding Markdown Image Syntax**

If you're new to **Markdown**, this guide will help you understand how to insert images using Markdown syntax.

---

## **📌 What Does This Do?**
```markdown
![sample1](assets/sample1.jpeg)
```

This **displays an image** called `sample1.jpeg` inside a Markdown file.

### **🖼 Output:**
![sample1](assets/sample1.jpeg)

---

## **🔍 Breaking It Down:**

### **1️⃣ `!` (Exclamation Mark)** 
- The `!` at the beginning **tells Markdown that this is an image** (not just a regular link).
- **If you remove it, the text becomes a clickable link instead of an image.**

```markdown
[sample1](assets/sample1.jpeg)
```

### **🖼 Output:**
[sample1](assets/sample1.jpeg)

---

### **2️⃣ `[sample1]` (Alternative Text)**
- The text inside **square brackets** (`[sample1]`) is called **alt text** (alternative text).  
- **What is alt text?**
  - 📌 **Used if the image doesn’t load** (it will display this text instead).
  - 👀 **Helps visually impaired users** (screen readers will read it aloud).
  - 🔍 **Improves SEO** (search engines understand the image better).

✅ **If the image loads, this text is not shown.**  
❌ **If the image is missing, "sample1" will be displayed instead.**

---

### **3️⃣ `(assets/sample1.jpeg)` (Image File Path)**
- The **path inside parentheses** `(assets/sample1.jpeg)` tells Markdown **where to find the image**.
- It means:
  - `assets/` → The image is stored inside a folder named **"assets"**.
  - `sample1.jpeg` → The actual **image file name**.

✅ The browser will look for `sample1.jpeg` inside `assets/`.

---

## **🛠 Example Scenarios**

### **✅ When the Image is Found:**
The image will be displayed **with no text visible**.

### **❌ When the Image is Missing:**
Instead of an image, the text **"sample1"** will appear.

---

## **🎨 Variations & Examples**

### **🖼 Example 1: Using a Full URL Instead**
```markdown
![example1](https://example.com/images/example1.png)
```
- **Uses an online image** instead of a local file.
- The image is loaded from **https://example.com/images/example1.png**.

### **🖼 Output:**
![example1](https://example.com/images/example1.png)

---

### **🖼 Example 2: Image Without Alt Text**
```markdown
![](assets/sample1.jpeg)
```
- The image will **still load**, but **if it’s missing, nothing will be displayed**.

### **🖼 Output:**
![](assets/sample1.jpeg)

---

### **🖼 Example 3: Clickable Image (Image as a Link)**
```markdown
[![sample1](assets/sample1.jpeg)](https://sample1.com)
```
- The image is **clickable** and will take the user to `https://sample1.com` when clicked.

### **🖼 Output:**
[![sample1](assets/sample1.jpeg)](https://sample1.com)

---

## **📁 Different Image Formats**

### **🖼 PNG Example:**
```markdown
![PNG Example](assets/images/example.png)
```
![PNG Example](assets/images/example.png)

### **🖼 JPG Example:**
```markdown
![JPG Example](assets/images/example.jpg)
```
![JPG Example](assets/images/example.jpg)

### **🖼 GIF Example:**
```markdown
![GIF Example](assets/images/example.gif)
```
![GIF Example](assets/images/example.gif)

### **🖼 SVG Example (Not Always Supported):**
```markdown
![SVG Example](assets/images/example.svg)
```
![SVG Example](assets/images/example.svg)

---

As you can see markdown supports many image types 

## **🚀 Summary**

| Markdown Part | Purpose |
|--------------|---------|
| `!` | Marks this as an **image** |
| `[Alt Text]` | Shows **alternative text** if the image is missing |
| `(image path)` | **File location** of the image |

---

### **🎯 Key Takeaway**
_"In Markdown, you use `![Alt Text](image path)` to insert an image—where `Alt Text` is a description (for accessibility) and `image path` is the location of the image file."_

---