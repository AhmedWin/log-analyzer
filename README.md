# log-analyzer

readme_content = """# Smart Log File Analyzer (Python)

A lightweight, CLI-based log analysis tool written in Python that scans logs files for `ERROR`, `CRITICAL`, and `WARNING` entries. This tool is ideal for quick diagnostics in NOC/SOC or DevOps environments.

---

##  Features

-  Parses large log files efficiently
-  Highlights ERROR, CRITICAL, and WARNING entries
-  Shows exact line number and log message
-  Optional output to a clean summary text file
-  Modular and extensible (great for automation or alerting tools)

---

##  How to Use

### 1. Run the Script from CLI

```bash
python log_parser.py logfile.log -o output.txt
'''' bash
