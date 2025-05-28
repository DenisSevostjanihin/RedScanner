# RedScanner

RedScanner is an advanced port and service scanner written in Python, an alternative to nmap with support for multithreading, banner grabbing, and logging.

## Features

- Multithreaded port scanning
- Banner grabbing (service version detection)
- Logging scan results
- Final summary of open ports

## Installation

Clone the repository and create a virtual environment:

```bash```
git clone https://github.com/YOUR_GITHUB_USERNAME/RedScanner.git
cd RedScanner
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt


```markdown```
## Usage

Run the scanner with:

```bash
python scanner.py 127.0.0.1 -s 20 -e 80 -t 50


## License

This project is licensed under the MIT License. See the LICENSE file for details.
