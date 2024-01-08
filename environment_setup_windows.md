# Setting Up Your Development Environment on Windows

In this guide, we'll walk you through the process of setting up a development environment on your Windows computer. We'll cover the installation of Python, Git, and Visual Studio Code.

## Step 1: Install Python

Python is a popular programming language, and it's likely you'll need it for your college courses.

1. Open a web browser and visit the official Python download page: [Python Downloads](https://www.python.org/downloads/).

2. Scroll down to the "Stable Releases" section and click on the "Windows" installer link for the latest Python 3.11.5 version.

3. Run the downloaded installer.

4. In the installer window, check the box that says "Add Python 3.11.5 to PATH" (replace 3.11.5 with the Python version number).

5. Click "Install Now" to begin the installation.

6. Once the installation is complete, open the Command Prompt by searching for "cmd" in the Start menu.

7. Verify the installation by running the following command:

   ```bash
   python --version
   ```

You should see the installed Python version displayed.

## Step 2: Install Git

Git is a version control system used by developers to manage code repositories.

1. Open a web browser and visit the Git download page: [Git Downloads](https://git-scm.com/downloads).

2. Download the Windows installer and run it.

3. Follow the installation wizard's instructions, leaving the default options selected.

   Note: If you see anything regarding installing git into PATH select that option.

4. Once the installation is complete, open the Command Prompt again.

5. Verify the installation by running the following command:

   ```bash
   git --version
   ```

You should see the installed Git version displayed.

## Step 3: Install Visual Studio Code

Visual Studio Code (VS Code) is a powerful code editor developed by Microsoft.

1. Open a web browser and visit the VS Code download page: [Visual Studio Code](https://code.visualstudio.com/Download).

2. Click the "Download for Windows" button to download the Windows version.

3. Run the downloaded installer.

4. Follow the installation wizard's instructions, leaving the default options selected.

## Step 4: Install the Python Extension for VS Code

1. Launch Visual Studio Code.
2. Click the "Extensions" icon in the left sidebar.
3. Search for "Python" and click the "Install" button for the "Python" extension.

## Step 5: Create a Python File

1. Click the "Explorer" icon in the left sidebar.
2. Click the "Open Folder" button and select the folder where you want to store your code.
3. Click the "New File" button in the Explorer sidebar and name the file "hello.py".
4. Add the following code to the file:

    ```python
    print("Hello, world!")
    ```

5. Save the file by clicking ctrl + s.
6. Run the file by clicking the "Run" button in the top right corner of the window.

   You should see the following output in the Terminal:

   ```bash
   Hello, world!
   ```

## Step 6: Sign into Github within VS Code

1. Open Visual Studio Code.
2. Open the Command Palette by pressing ctrl + Shift + P.
3. Type "git: clone" and press Enter.
4. Select "Clone from GitHub".
5. Select "Allow" to give VS Code access to your GitHub account.
6. A browser window will open. Sign into your GitHub account.
