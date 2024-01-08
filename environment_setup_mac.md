# Setting Up Your Development Environment on macOS

In this guide, we'll walk you through the process of setting up a development environment on your Mac. We'll cover the installation of Homebrew, Python, Visual Studio Code, and Git.

## Step 1: Install Homebrew

Homebrew is a package manager that makes it easy to install and manage software on macOS.

1. Open the Terminal app. You can find it in the "Utilities" folder within the "Applications" folder, or you can use Spotlight Search (Cmd + Space, then type "Terminal").

2. Install Homebrew by running the following command:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   *Note: You may be prompted to enter your password. If so, enter your password and press Enter.*

3. Follow the on-screen instructions to complete the installation.

4. After installation is complete, run the following command to ensure Homebrew is set up correctly:

      ```bash
      brew doctor
      ```

   *Note: If the brew command above does not work try pasting the following to link brew to you path variables:

   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

## Step 2: Install Python

Python is a popular programming language, and it's likely you'll need it for your college courses.

1. Install Python 3 using Homebrew by running the following command:

   ```bash
   brew install python
   ```

1. Verify the installation by checking the Python version:

    ```bash
    python3 --version
    ```

You should see the installed Python version displayed.

## Step 3: Install Git

Git is a version control system used by developers to manage code repositories.

1. Open the Terminal app.

2. Install Git using Homebrew:

   ```bash
   brew install git
   ```

3. Verify the installation by checking the Git version:

   ```bash
   git --version
   ```

## Step 4: Install Visual Studio Code

Visual Studio Code (VS Code) is a powerful code editor developed by Microsoft.

1. Open a web browser and visit the VS Code download page: [Visual Studio Code](https://code.visualstudio.com/Download).

2. Click the "Download for Mac" button to download the macOS version.

3. After the download is complete, open the downloaded file and drag the "Visual Studio Code" icon into the "Applications" folder.

4. Launch Visual Studio Code from the "Applications" folder.


## Step 5: Install the Python Extension for VS Code

1. Open Visual Studio Code.
2. Click the "Extensions" icon in the left sidebar. It looks like a square with four squares inside.
3. Search for "Python" in the search bar.
4. Click the "Install" button for the "Python" extension.

## Step 6: Create a Python File

1. Click the "Explorer" icon in the left sidebar.
2. Click the "Open Folder" button and select the folder where you want to store your code.
3. Click the "New File" button in the Explorer sidebar and name the file "hello.py".
4. Add the following code to the file:

    ```python
    print("Hello, world!")
    ```

5. Save the file by pressing Cmd + S.
6. Run the file by clicking the "Run" button in the top right corner of the window.

   You should see the following output in the Terminal:

    ```bash
    Hello, world!
    ```

## Step 7: Sign into Github within VS Code

1. Open Visual Studio Code.
2. Open the Command Palette by pressing Cmd + Shift + P.
3. Type "git: clone" and press Enter.
4. Select "Clone from GitHub".
5. Select "Allow" to give VS Code access to your GitHub account.
6. A browser window will open. Sign into your GitHub account.
