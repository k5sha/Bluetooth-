echo "Installing"
echo "\nCreate by k5sha."
pkg upgrade
pkg install python
pkg install bluetooth libbluetooth-dev
git clone https://github.com/pybluez/pybluez
cd pybluez
python setup.py install
cd ..
echo "\nInstaled"
echo "\nStarted KB-DD"
python ddos.py