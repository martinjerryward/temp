# 📊 Markdown Diagrams

Markdown supports diagrams using **Mermaid.js**, a powerful tool for creating flowcharts, sequence diagrams, class diagrams, and more.

---

## **✅ Flowcharts**
Use `graph TD;` for a **top-down** flowchart.

### **Example:**
````markdown
```mermaid
graph TD;
    A[Start] --> B{Decision?};
    B -- Yes --> C[Proceed];
    B -- No --> D[Stop];
    C --> E[End];
```
````

### **Renders as:**
```mermaid
graph TD;
    A[Start] --> B{Decision?};
    B -- Yes --> C[Proceed];
    B -- No --> D[Stop];
    C --> E[End];
```

---

## **✅ Class Diagrams**
Use `classDiagram` to define object-oriented structures.

### **Example:**
````markdown
```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +String breed
        +bark()
    }
    Animal <|-- Dog
```
````

### **Renders as:**
```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +String breed
        +bark()
    }
    Animal <|-- Dog
```

---

## **✅ Sequence Diagrams**
Use `sequenceDiagram` to visualize interactions between entities.

### **Example:**
````markdown
```mermaid
sequenceDiagram
    participant A as User
    participant B as Server
    A->>B: Request Data
    B-->>A: Response Data
```
````

### **Renders as:**
```mermaid
sequenceDiagram
    participant A as User
    participant B as Server
    A->>B: Request Data
    B-->>A: Response Data
```

---

## **✅ Gantt Charts**
Use `gantt` to create **project timelines**.

### **Example:**
````markdown
```mermaid
gantt
    title Project Timeline
    section Development
    Task A :a1, 2024-02-01, 10d
    Task B :a2, after a1, 15d
```
````

### **Renders as:**
```mermaid
gantt
    title Project Timeline
    section Development
    Task A :a1, 2024-02-01, 10d
    Task B :a2, after a1, 15d
```

---

## **🚀 Summary**
| Diagram Type | Syntax |
|-------------|--------|
| **Flowchart** | `graph TD;` |
| **Class Diagram** | `classDiagram` |
| **Sequence Diagram** | `sequenceDiagram` |
| **Gantt Chart** | `gantt` |

---

## 🎯 Key Takeaway
_"Mermaid.js allows you to create diagrams directly in Markdown, enhancing documentation with visual clarity."_
