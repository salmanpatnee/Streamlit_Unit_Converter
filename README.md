# 🔄 Google-Style Unit Converter (Built with Streamlit & UV)

A clean and modern unit converter web app built with [Streamlit](https://streamlit.io/) and managed using [uv](https://github.com/astral-sh/uv). Inspired by Laravel's clean coding style and layout simplicity.

---

## ✨ Features

- Convert units for **Length**, **Weight**, and **Temperature**
- Sleek, responsive UI using Streamlit's column layout
- Inspired by Google's simple and intuitive conversion interface
- Fast setup using `uv` (a fast Python package manager)

---

## 🚀 Quick Start

### 🔧 Requirements

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (for dependency and virtual environment management)

### 📦 Setup

```bash
# Clone the repo
git clone https://github.com/your-username/unit-converter-app.git
cd unit-converter-app

# Create and activate virtual environment using uv
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv pip install streamlit
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

- Conversion factors are predefined for each category
- Temperature conversion uses custom logic (e.g., C ↔ F ↔ K)
- Streamlit form groups inputs inline using `st.columns` for better UX

---

## 📁 Project Structure

```
unit-converter-app/
├── .venv/               # Virtual environment (auto-created by uv)
├── app.py               # Main Streamlit application
├── requirements.txt     # Optional: freeze your environment
└── README.md            # This file
```

---

## 🙌 Credits

- Built with ❤️ by a Laravel-turned-Python dev
- Powered by [Streamlit](https://streamlit.io/)
- Managed with [uv](https://github.com/astral-sh/uv)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
