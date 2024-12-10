---
lesson_name: Program Overview
code_editor: False
code_execution: True
adding_file_allowed: False
---

## Explain the rules of the game.

For this program, we will create a simple guessing game. The rules of the game are that the computer will randomly select a number between 0 and 100, and the player's goal is to guess the number with the fewest number of tries.

![Guess the number game example](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/guess_the_number_en.gif)

<p class="caption">Example of the game we will create</p>

### Creating a folder for the program

First, open the VSCode program that we installed earlier. Click on **File**, and **Open Folder**. Then, create a new folder and name it **guess-the-number** or any other name you want, and click **Open.**

After creating the folder, the Explorer bar with the name of the newly created folder will appear on the left-hand side of the screen, as shown in the example below.

![](https://asset.pythonexpert.dev/media/markdownx/2024/05/03/bb776444-f978-43c0-b8f8-03757f436bf3.png)

After that, right-click in the Explorer area and select New File... to create a new file. Name the file **game.py** and make sure to use the file extension **.py** to let the program understand that the created file is a Python file.

![Create a new file](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/create-new-file.gif)

### How to run Python code through VSCode

Once the file is created, enter the code below in the newly created file. Save the file and click on the arrow pointing downwards on the right-hand side of the triangle in the top right corner of the screen. Then select **Run Python File** to run the code.

```python
print("Hello World!")
```

![Test run the file](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/run-python-file.gif)

<div class="alert-info text-sm">
If there is no triangle button on the top right of the screen like in the example, install the Python extension from this <a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" class="text-blue-500" target="_blank">website</a> and click install.
</div>

### How to Run Code through Terminal

In addition to running code through VSCode, **the general way to run a file is through the terminal**, which can also be done through the VSCode program. To do this, select Terminal from the top bar of the screen and choose New Terminal. The program will open a Terminal window at the bottom of the screen. Then type the command `python game.py` or `python3 game.py` to run the file we created.

```shell
$ python game.py
Hello World
```

![Run the file with command line](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/run-with-cli.gif)

<p class="caption">Example of running code through Terminal</p>

If "Hello World!" appears at the bottom of the screen, as per the code we wrote, it indicates that we have installed everything correctly and are ready to create games in this topic. If you see cannot run the program and see an error message <span class="text-red-500"> No such file or directory</span>, try running the command `pwd` and check if you are in the right folder.
