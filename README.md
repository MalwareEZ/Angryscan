# AngryEnum
AngryEnum is a Python script designed for automating the enumeration process on a target machine. It performs checks for common services such as FTP, SMB, and HTTP, providing insights into potential vulnerabilities and aiding in the enumeration of accessible resources. This script simplifies the process of information gathering and enumeration, making it an efficient tool for penetration testers and cybersecurity enthusiasts.

# Features
* Automated enumeration of FTP, SMB, and HTTP services.
* Anonymous login attempts on FTP servers for quick access assessment.
* List available shares as an anonymous user on SMB servers to understand accessible resources.
* Directory brute-forcing on HTTP servers using a customizable wordlist.

# Usage
* Ensure that all necessary Python modules are installed.
* Run the script with the desired target IP address using the following command
```sh
$ git clone https://github.com/MalwareEZ/Angryscan
$ cd Angryscan
$ pip install -r requirements.txt
$ python3 angryenum.py -i <target>
```

# Disclaimer
AngryEnum is intended for educational purposes and authorized assessments only. Users are advised to adhere to ethical hacking practices and obtain proper authorization before performing any enumeration on target systems.

The goal of this project is to evolve continuously (endlessly). If you have any suggestions for adding additional features regarding network enumeration, please feel free to share them with me. I have many more improvements in store that I plan to implement. Your ideas and contributions are welcome !
