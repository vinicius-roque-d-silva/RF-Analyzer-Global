# 🛰️ RF Analyzer Pro: Global Enterprise Edition
> (Or: "The SysAdmin's Nightmare")

Welcome to **RF Analyzer Pro**. You know that moment when the network crawls to a halt and everyone is just guessing why? Well, this script was built so you can stop guessing and start giving answers.

It doesn’t just capture packets; it interrogates them, stores them in a database, and delivers a pre-digested report directly to your browser.

---

## 🛠️ What's Under the Hood? (Tech Stack)

We didn't hold back on the engine. This project combines the best tools for data and network analysis:

* **🐍 Python 3**: The heart of the operation.
* **📡 Scapy**: For sniffing packets like a pro (or an ethical hacker, your choice).
* **🗄️ SQLite3**: Because TXT files are for amateurs. We use real persistence and data integrity here.
* **📊 Internal HTML Dashboard**: An on-demand HTTP server to visualize data with style and clarity.
* **📈 Psutil**: Hardware monitoring, because we don't want the analyzer to consume more resources than the network itself.

---

## 🚀 Key Features

* **`scan`**: Activates the radar. Captures everything passing through the network interface and throws it instantly into the database.
* **`observe`**: The panoramic view. Who is hogging the bandwidth? Where is the bottleneck? Real-time statistics at your fingertips.
* **`web`**: The "Ace in the hole." Generates a dynamic HTML report and opens your browser automatically. This is the "Wow" moment of the demo.
* **`export`**: Need to send data to compliance or the boss? Generates a clean `.csv` file.
* **`health`**: Self-diagnosis. Because even the watcher needs watching (RAM and DB monitoring).

---

## 🚦 Prerequisites (Don't skip this!)

To run this beast, you will need:

1.  **Admin/Root Privileges**: Capturing network packets is serious business. The OS won't let you do this without proper permissions.
2.  **Required Libraries**:
    ```bash
    pip install scapy psutil
    ```

---

## 📦 Level Up Your Network

1.  **Clone this repo**: 
    ```bash
    git clone [https://github.com/vinicius-roque-d-silva/Network-Audit-Pro.git](https://github.com/vinicius-roque-d-silva/Network-Audit-Pro.git)
    ```
2.  **Enter the folder**: 
    ```bash
    cd Network-Audit-Pro
    ```
3.  **Run as admin**: 
    ```bash
    python main.py
    ```
4.  **Have fun** (with great power comes great responsibility!).

---

## 🧠 Why is this project special?

It demonstrates mastery of advanced concepts such as **concurrency**, **real-time data streaming**, and **integrated data visualization**. It’s the kind of tool that separates those who just "copy-paste code" from those who actually **build infrastructure solutions**.

---

## ⚠️ Disclaimer
The name of this program is merely a joke playing on the naming conventions of modern enterprise software. That being said, **this is an open-source project**—feel free to use it to have fun, experiment, and test new concepts.

---
_Developed with ☕ and Python by Vinícius Roque._