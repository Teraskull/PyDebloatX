<p align="center">
  <img width="10%" align="center" src="icon.ico">
</p>
<h1 align="center">
  PyDebloatX
</h1>

<p align="center">
    A Python GUI for uninstalling the default Windows 10 apps.
</p>

<p align="center">
  <a style="text-decoration:none" href="https://github.com/Teraskull/PyDebloatX/releases">
    <img src="https://img.shields.io/github/v/release/Teraskull/PyDebloatX?label=Version&style=flat-square&color=00B16A" alt="Releases" />
  </a>
  <a style="text-decoration:none" href="https://www.codefactor.io/repository/github/teraskull/pydebloatx">
    <img src="https://www.codefactor.io/repository/github/teraskull/pydebloatx/badge?style=flat-square" alt="CodeFactor" />
  </a>
  <a style="text-decoration:none" href="https://github.com/Teraskull/PyDebloatX/releases">
    <img src="https://img.shields.io/github/downloads/teraskull/pydebloatx/total?color=00B16A&style=flat-square" alt="Downloads" />
  </a>
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/OS-Windows%2010-blue?style=flat-square&color=00B16A" alt="OS" />
  </a>
</p>

<div align="center">

![Main window screenshot](images/app_main.png)

![Loading screenshot](images/app_loading.png)

![Confirmation screenshot](images/app_confirm.png)

</div>


## Shortcuts:

* **Ctrl+R** to refresh the list of installed apps.
* **Ctrl+G** to visit the Github page.
* **Ctrl+A** to view the "About" window.
* **Ctrl+Q** to quit the app.

## App limitations:

* [FIXED] ~~It takes a few seconds to list all currently installed apps.~~
* [FIXED] ~~When uninstalling apps, PowerShell windows will open.~~
* You can only **uninstall** apps with this GUI, hence the name.
* You cannot uninstall other apps, for example Cortana, with this GUI, because PowerShell does not support it.
* App disk space is approximate and taken from Microsoft Store, there is no other way to get real-time app size.

## Dependencies:

* PyQt5
    ```pip install pyqt5```

## Usage:

* ```git clone https://github.com/Teraskull/PyDebloatX```
* ```cd PyDebloatX```
* ```pip install -r requirements.txt```
* ```python app.py``` or ```py app.py```

## License:

This software is available under the following licenses:

  * **MIT**