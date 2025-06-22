# 🚪 DirCop – Advanced Directory & File Discovery Tool

**DirCop** is a fast and flexible directory scanning tool written in Python.  
Designed to help security researchers, bug bounty hunters, and CTF players find hidden or restricted resources on web servers.

---

## ✨ Features

- 🔍 Scan for hidden directories/files using wordlists
- ⚙️ Multi-threaded for fast discovery
- 🚦 Categorizes results by status code:
  - ✅ `200 OK`
  - 🔐 `403 / 401 Restricted`
  - 🔁 `302 Redirect`
- 🧠 CLI or interactive mode
- 🐍 Minimal dependency: `requests`
---
## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/ABXAR/dircop.git
cd dircop
pip install requests
```
---

## 🚀 Usage

### CLI Mode (recommended)

```dircop
python dircop.py -u http://example.com -w wordlist.txt -t 20
```

**Options:**

| Flag               | Description                             |
|--------------------|-----------------------------------------|
| `-u`, `--url`      | Target URL (e.g., http://example.com)   |
| `-w`, `--wordlist` | Path to your wordlist file              |
| `-t`, `--threads`  | Number of threads (default: 10)         |

---

### Interactive Mode

If flags are not provided, the tool will prompt for:

```
Enter the target URL (e.g., http://example.com): 
Enter the path to the payload file: 
```

---

## 📂 Example Output

```output
[FOUND] http://example.com/admin [200 OK]
[RESTRICTED] http://example.com/hidden [403]
[REDIRECT] http://example.com/old-login [302]

[+] Summary of Found Paths:
http://example.com/admin
```

---

## 🧪 Wordlist Example

Example contents for `wordlist.txt`:

```wordlist
admin
login
robots.txt
config.php
dashboard/
```

Use larger or curated lists from [SecLists](https://github.com/danielmiessler/SecLists) for better discovery.

---

## 👤 Author

Made with ❤️ by **AB-X-AR**

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

