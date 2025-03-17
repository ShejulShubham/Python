## Getting Started with Python

Here’s how you can install Python and verify that it’s installed correctly:

---

### **Step 1: Install Python**

#### **For Windows:**
1. **Download Python Installer:**
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Click on the "Download Python" button for your operating system.

2. **Run the Installer:**
   - Double-click the downloaded `.exe` file.
   - During installation, **ensure you check the box that says "Add Python to PATH"** (important for using Python from the command line).

3. **Customize Installation (Optional):**
   - If you want to change the installation directory, select "Customize installation" and choose your preferred options.

4. **Complete Installation:**
   - Click "Install Now" and follow the prompts to complete the installation.

#### **For macOS:**
1. macOS usually comes with Python pre-installed. To install the latest version:
   - Install **Homebrew** if you don't already have it. Open Terminal and run:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install Python using Homebrew:
     ```bash
     brew install python
     ```

2. Verify the installation:
   ```bash
   python3 --version
   ```

#### **For Linux:**
1. Open a terminal and use your package manager to install Python:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3
     ```
   - On Fedora:
     ```bash
     sudo dnf install python3
     ```

2. Verify the installation:
   ```bash
   python3 --version
   ```

---

### **Step 2: Verify Python Installation**

1. **Check Python Version:**
   - Open a terminal (or Command Prompt on Windows).
   - Type the following command:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```

   - You should see the installed version of Python (e.g., `Python 3.11.4`).

2. **Launch Python Interpreter:**
   - Type:
     ```bash
     python
     ```
     or
     ```bash
     python3
     ```
   - You should see the Python interactive prompt (`>>>`), indicating that Python is working correctly.
   - Type `exit()` or press `Ctrl+D` to exit the interpreter.

3. **Test a Simple Script:**
   - Create a Python file named `test.py` with the following content:
     ```python
     print("Hello, Python!")
     ```
   - Run the script in the terminal:
     ```bash
     python test.py
     ```
     or
     ```bash
     python3 test.py
     ```

   - You should see the output:
     ```
     Hello, Python!
     ```

---
