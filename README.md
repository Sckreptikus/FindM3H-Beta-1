# FindM3H
Username recognition on various websites.

---

## Installation

#### With `pip3`
```bash
# Linux
sudo -H pip3 install git+https://github.com/anonhack990/FindM3H-Beta-1.git --upgrade
FindM3H --help
```

#### Build from source
```bash
# Linux
git clone https://github.com/Anonhack990/FindM3H-Beta-1.git ; cd FindM3H-Beta-1
sudo -H pip3 install -r requirements.txt
python3 setup.py build
sudo python3 setup.py install
```
---

## Usage
Start by printing the available actions by running `FindM3H --help`. Then you can perform the following tests:
```bash
# print all results.
FindM3H target Anonhack990 --all -o test


# print positive results.
FindM3H target Anonhack990 --positive -o test


# print negative results.
FindM3H target Anonhack990 --negative  -o test
```