

# Textify Lite

Textify Lite is a Linux utility that lets you **select an area** of the screen, **extract text** using OCR, and **open the extracted text in an editor window** for quick editing and copying.The extraction happens within the fraction of a second.
<details>
<summary>Note</summary>
<div style="padding-left: 3em;padding-right: 3em;">
This is a side project previewing the main app in development. The original will be a cross-platform tool for efficient text extraction, leveraging a more advanced OCR engine than the current one to deliver improved accuracy. Users will be able to select OCR languages and customize the popup via config files, along with other new features.

```
Textify : https://github.com/sayel765/textify
```


</div>
</details>

## 📺 Preview

https://github.com/user-attachments/assets/9c69039b-c5d8-4db7-900e-5503d45f3a6f

## 📌 Features

- 🌐 **Supports Wayland & X11** (auto-detects environment)
- 📷 **Screenshot selection** via grim/slurp (Wayland) or maim/slop (X11)
- ⌨️ **OCR for English & Bengali** (Tesseract backend)
- ✍️ **Editable popup window** (PyQt5)
- 📋 **Copy to system clipboard** via wl-clipboard (Wayland) or xclip (X11)
<!-- =================== FEATURE END ===================== -->
## 📦 Installation

Install according to your distribution.
For installation, Follow Instruction given for your distribution.

<!-- ----------------------- Debian ----------------------- -->
<details>
<summary><strong>Debian/Ubuntu-based </strong>(Debian, Ubuntu, Kali, Pop!_OS, Linux Mint et al.)</summary>
<div style="padding-left: 2em;">

##### [✓] Dependency installation
```bash
sudo apt update
sudo apt install python3-pipx grim slurp wl-clipboard maim slop xclip tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben xdg-utils
```
##### [✓] Add pipx binary path to your shell PATH
```bash
pipx ensurepath # Similar to adding (export PATH="$PATH:/home/your-username/.local/bin") in config file

# Either close or reopen the terminal
# OR run the command:
source ~/.bashrc # or your shell config file ~/.zshrc
```
##### [✓] Install Textify Lite 
```bash
git clone https://github.com/sayel765/textify-lite.git
cd textify-lite
pipx install .
```
🏆 **Your Installation is completed**  
Now you can run via ***textify*** command or set a key binding.  
I prefer using **mod+shift+a** [for A → Area selection.]

</div>
</details>
<!-- ----------------------- Arch ------------------------- -->
<details>
<summary><strong>Arch-based </strong>(Arch, Manjaro, EndeavourOS, ArcoLinux, Artix Linux et al.)</summary>
<div style="padding-left: 2em;">

##### [✓] Install dependencies
```bash
sudo pacman -S python-pipx grim slurp wl-clipboard maim slop xclip tesseract tesseract-data-eng tesseract-data-ben xdg-utils
```
##### [✓] Add pipx binary path to your shell PATH
```bash
pipx ensurepath # Similar to adding (export PATH="$PATH:/home/your-username/.local/bin") in config file

# Either close or reopen the terminal
# OR run the command:
source ~/.bashrc # or your shell config file ~/.zshrc
```
##### [✓] Install Textify Lite 
```bash
git clone https://github.com/sayel765/textify-lite.git
cd textify-lite
pipx install .
```
🏆 **Your Installation is completed**  
Now you can run via ***textify*** command or set a key binding.  
I prefer using **mod+shift+a** [for A → Area selection.]

</div>
</details>

<!-- --------------------- Red Hat ------------------------ -->
<details>
<summary><strong>Fedora / RHEL / CentOS</strong> et al.</summary>
<div style="padding-left: 2em;">

##### [✓] Dependency installation
```bash
sudo dnf install pipx grim slurp wl-clipboard maim slop xclip tesseract tesseract-langpack-eng tesseract-langpack-ben xdg-utils
```
##### [✓] Add pipx binary path to your shell PATH
```bash
pipx ensurepath # Similar to adding (export PATH="$PATH:/home/your-username/.local/bin") in config file

# Either close or reopen the terminal
# OR run the command:
source ~/.bashrc # or your shell config file ~/.zshrc
```
##### [✓] Install Textify Lite 
```bash
git clone https://github.com/sayel765/textify-lite.git
cd textify-lite
pipx install .
```
🏆 **Your Installation is completed**  
Now you can run via ***textify*** command or set a key binding.  
I prefer using **mod+shift+a** [for A → Area selection.]

</div>
</details>
<!-- ---------------------- openSUSE ----------------------- -->
<details>
<summary><strong>openSUSE</strong> et al.</summary>
<div style="padding-left: 2em;">

##### [✓] Dependency installation
```bash
sudo zypper install python3-pipx grim slurp wl-clipboard maim slop xclip tesseract tesseract-ocr-traineddata-english tesseract-ocr-traineddata-bengali xdg-utils
```
##### [✓] Add pipx binary path to your shell PATH
```bash
pipx ensurepath # Similar to adding (export PATH="$PATH:/home/your-username/.local/bin") in config file

# Either close or reopen the terminal
# OR run the command:
source ~/.bashrc # or your shell config file ~/.zshrc
```
##### [✓] Install Textify Lite 
```bash
git clone https://github.com/sayel765/textify-lite.git
cd textify-lite
pipx install .
```
🏆 **Your Installation is completed**  
Now you can run via ***textify*** command or set a key binding.  
I prefer using **mod+shift+a** [for A → Area selection.]

</div>
</details>
<!-- =================== INSTALLATION END ======================== -->

## 🛠 Development Setup

**ONLY If you want to contribute or run from source:**

```bash
# 1. Install system dependencies.
#    Run one of the followings according to your package manager.

# sudo pacman -S python-pip grim slurp wl-clipboard maim slop xclip tesseract tesseract-data-eng tesseract-data-ben xdg-utils python python-pip python-virtualenv git
# sudo apt install python3-pip grim slurp wl-clipboard maim slop xclip tesseract-ocr tesseract-ocr-eng tesseract-ocr-ben xdg-utils
# sudo dnf install python3-pip grim slurp wl-clipboard maim slop xclip tesseract tesseract-langpack-eng tesseract-langpack-ben xdg-utils
# sudo zypper install python3-pip grim slurp wl-clipboard maim slop xclip tesseract tesseract-ocr-traineddata-english tesseract-ocr-traineddata-bengali xdg-utils

# 2. Clone the repository
git clone https://github.com/sayel765/textify-lite.git
cd textify-lite

# 3. Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate

# 4. Install Python dependencies inside the virtual environment
pip install -e .

# 5. Run the app in development mode
textify
```

## 🗂 Folder Structure

```
textify-lite/
├── src/
│   └── textify/
│       ├── __init__.py
│       ├── utils.py
│       ├── screenshot.py
│       ├── ocr.py
│       ├── editor.py
│       └── main.py
├── tests/
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## 📜 License

MIT License

## 💻 Author

Md. Sayel – [mdsayel666@gmail.com](mailto:mdsayel666@gmail.com)  
GitHub – [Md. Sayel](https://github.com/sayel765)  
LinkedIn – [Md. Sayel](https://linkedin.com/in/sayel765)
