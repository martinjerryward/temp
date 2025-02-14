# 📖 Guide to Setting Up Webpack for Three.js Projects

## 🔹 Introduction
In the previous lesson, we loaded **Three.js** using a script tag and directly downloaded the library. This method has limitations:
- Some classes are missing due to file size constraints.
- Running a local server is required for security reasons when working with textures.

To solve these issues, we will use **Webpack**, a popular bundler.

---

## 🔹 What is a Bundler?
A **bundler** is a tool that processes various asset types (JavaScript, CSS, HTML, images, TypeScript, etc.), applies modifications, and outputs web-friendly bundles. It also provides features such as:
- Running a **local server**.
- Managing **dependencies**.
- Handling **modules**.
- Improving **compatibility** by transpiling JavaScript.
- Optimizing files and assisting in deployment.

We will use **Webpack** due to its popularity, extensive documentation, and active community support.

---

## 🔹 Installing Webpack

### **Step 1: Install Node.js**
1. Download and install the latest **Node.js** version from [Node.js official website](https://nodejs.org/).
2. Verify the installation by running:
   ```sh
   node -v
   npm -v
   ```
   in your terminal.

### **Step 2: Download the Starter Project**
1. Download the **starter project** (provided with this lesson).
2. Extract it to a properly organized folder.

### **Step 3: Open the Project in VS Code**
- Open **Visual Studio Code**.
- Use `View > Terminal` to open an integrated terminal.

### **Step 4: Navigate to the Project Directory**
Run the following command in the terminal:
```sh
cd path/to/your/project
```
Alternatively, **drag and drop** the folder into the terminal after typing `cd `.

### **Step 5: Install Dependencies**
Run:
```sh
npm install
```
This command installs all dependencies listed in `package.json`.

---

## 🔹 Running Webpack Dev Server
To start the local development server, run:
```sh
npm run dev
```
This will:
- Launch a local server.
- Open the project in your **default browser**.
- Enable **live reloading**.

### **Stopping the Server**
To stop the server, press:
```sh
Ctrl + C
```
(Windows users may need to confirm by pressing `O` + `Enter`.)

### **Restarting the Server**
Each time you resume work, simply run:
```sh
npm run dev
```
without reinstalling dependencies.

---

## 🔹 Understanding the Project Structure

### **Important Folders & Files:**
- 📂 `src/` → Contains **working files** (JS, HTML, CSS).
- 📂 `static/` → Stores **assets** (images, models, etc.).
- 📂 `dist/` → The final **output folder** (generated after `npm run build`).
- 📄 `index.html` → The main HTML file.
- 📄 `script.js` → The JavaScript entry point.
- 📄 `style.css` → The main CSS file.

### **Importing Three.js in JavaScript**
Instead of manually adding a `<script>` tag, use:
```js
import * as THREE from 'three';
```
This ensures Three.js is correctly loaded as a module.

---

## 🔹 Building the Project for Deployment
To generate an optimized bundle, run:
```sh
npm run build
```
This creates a **`dist/`** folder containing the final version of the website, ready for hosting.

---

## 🔹 Troubleshooting
### **Common Errors & Fixes**
| Error | Solution |
|--------|----------|
| `Xcode error (Mac users only)` | Run `xcode-select --install` in the terminal. |
| `Template doesn’t work / White page` | Ensure you're in the correct folder (`PWD` command). |
| `Older Node.js version causing issues` | Update Node.js and reinstall dependencies. |
| `Website not opening` | Try `localhost:8080` or `127.0.0.1:8080`. |

---

## 🔹 Accessing the Website on Other Devices
1. Connect all devices to the same **Wi-Fi or Ethernet network**.
2. Use your **local IP address** (e.g., `192.168.1.X:8080`) on your phone or tablet.

---

## 🔹 Conclusion
- Webpack **bundles assets**, manages dependencies, and runs a **local server**.
- Use `npm install` **once** per project.
- Run `npm run dev` to **start the development server**.
- Run `npm run build` to **prepare the project for deployment**.

With Webpack set up, we can now proceed with **Three.js development** in a more structured and efficient way! 🚀
