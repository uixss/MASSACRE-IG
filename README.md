# MASSACRE-IG
## ⚠️ Disclaimer

This project is for **educational purposes only**. Misuse of this script to violate the terms and policies of any platform, including Instagram, is prohibited. The author is not responsible for any misuse or consequences.

 <img src="./url.png" alt="ig">

---

# 🚨 Instagram Report v1 

A Python script designed for automating the submission of reports to Instagram's support form. This tool is built for educational purposes and highlights the importance of understanding APIs and headers.

## 🖥️ Example Output 

```
[+] Victim UserName : target_username
[+] Victim Name : John Doe
=======================================
[√] Done Report : 1 | target_username
[×] Error Code : 403
```

---

# 🚀 Instagram Report v2

A Python script designed to automate the submission of reports to Instagram's support page. This script uses configurable email lists, user-agents, and relationships to randomize and streamline the process.

## Features ✨

- **Dynamic User-Agent Generator**: Simulates different devices and browsers.
- **Configurable Email List**: Loads emails from a text file to randomize submissions.
- **Relationship Randomization**: Selects from predefined relationships.
- **Error Logging**: Captures and logs network errors or unexpected issues.
- **Customizable Configurations**: Modify headers, URLs, sleep ranges, and more.

---

## Configuration ⚙️

The script uses a configuration dictionary (`CONFIG`) to control the following:

- **`email_file`**: Path to the file containing email addresses (default: `emails.txt`).
- **`url`**: URL for submitting reports (default: Instagram support form).
- **`headers_base`**: Base headers for requests.
- **`sleep_range`**: Time range (in seconds) for pauses between requests.
- **`log_file`**: File to save logs (default: `report_log.txt`).

---

## Important Notes 📝

- The script uses hardcoded headers and data fields required by Instagram's support form.
- Ensure to use this responsibly and within the bounds of ethical usage.
