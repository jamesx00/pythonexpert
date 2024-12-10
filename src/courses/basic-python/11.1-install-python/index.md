---
lesson_name: Install Python
code_editor: False
code_execution: False
adding_file_allowed: False
section: Write Your First Program
---

## How to Install Python

Currently, the Python language is divided into two main versions, which are Python 2 and Python 3. In this course, we will use Python 3, which is the version that is mostly used today.

In this section, we will check the version of Python that is installed on your machine, or install it if it has not been installed yet. Additionally, we will install a text editor called Visual Studio Code, which was developed by Microsoft.

Let's see the details of how to check the version according to the operating system of your device:

- [Windows](#windows)
- [MacOS](#macos)
- [Linux](#linux)

### Windows

#### Checking the version on Windows

To start, check whether Python is already installed on your computer by opening the program called Command Prompt. Type "cmd" in the search bar located at the bottom of the taskbar, and then select the program called Command Prompt.

![](https://asset.pythonexpert.dev/media/markdownx/2024/05/03/1adf6ecd-1b76-4b57-a564-2fe951cbb93e.png)

Once the program is running, type the command `python` and press Enter. If Python is already installed on your computer, you will see that the command prompt changes to a python prompt preceded by the symbol ">>>".

If Python is already installed on your computer, you can skip this step and move on to the next step to install VSCode. However, if the message displayed is something like <span class="text-red-500">'python' is not recognized as an internal or external command, operable program, or batch file.</span> it means that Python has not been installed on your computer yet. Follow the instructions below to install Python.

#### Installing Python on Windows

To install Python on Windows, go to the website <a class="text-blue-500" href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>. You will see a button labeled "Download Python" followed by the version number. Click the button to download the installer and run it when the download is complete.

Before starting the installation, check the box labeled "Add Python 3.x to PATH" and click the install button.

After the installation is complete, open the Command Prompt program again and run the command "python". You will see that the description has changed and the version of Python that we installed will be displayed.

```bash
Python 3.11.2 [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### MacOS

#### Checking the version on MacOS

Normally, devices running MacOS come with both Python 2 and 3 installed. To check the version, open the "Terminal" application that comes with the device and run the command `python` to run a program using Python 2, or the command `python3` to run a program using Python 3.

<div class="alert-info text-sm">
Throughout this course, use the command that runs Python version 3 on your machine.
</div>

```bash
$ python
Python 2.7.5 (default, Mar 9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>
```

<p class="caption">Python 2</p>

```bash
$ python3
Python 3.10.9 (main, Feb 17 2023, 07:18:58) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<p class="caption">Python 3</p>

### Linux

#### Checking the version on Linux

In Linux systems, Python is already installed by default. We can run the command python to see the default version of Python installed on the machine. In some machines, the default version may be Python 2, so in some cases, it may be necessary to differentiate between versions 2 and 3 using the commands python and python3.

<div class="alert-info text-sm">
Throughout this course, use the command that runs Python version 3 on your machine.
</div>

```bash
$ python
Python 2.7.16 (default, Oct 10 2019, 22:02:15)
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<p class="caption">Python 2</p>

```bash
$ python3
Python 3.7.3 (default, Jan 22 2021, 20:04:44)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<p class="caption">Python 3</p>

### Installing VSCode

After successfully installed Python, install a text editor called VSCode, which can be downloaded and installed from <a href="https://code.visualstudio.com/download" class="text-blue-500" target="_blank">code.visualstudio.com</a>

After installing VSCode, install the Python extension by going to <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" class="text-blue-500" target="_blank">this website</a> and clicking install.
