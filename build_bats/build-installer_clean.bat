cd ..
pip install -r requirements.txt
rmdir /s /q build
pyinstaller --noconfirm --icon "img/icon.ico" --console --onefile "horsy_installer.py"
rmdir /s /q __pycache__
del horsy_installer.spec
rmdir /s /q build
cd build_bats