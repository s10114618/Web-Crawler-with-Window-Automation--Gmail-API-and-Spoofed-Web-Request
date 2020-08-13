# Web Crawler with Window Automation, Gmail API and Spoofed Web Request


<!-- ABOUT THE PROJECT -->
## About The Project
This project automatically crawls for new chapter on One Piece Site and alerts the users if found. 
The User-Agent is spoofed from the default "Python 3.6" to "mozilla/5.0 (windows nt 10.0; win64; x64)", this is to avoid any bot or crawler checks.


### How to setup Gmail API
Before we can start using Gmail API, we need to login to our Gmail account to 
```sh
1. Disable "2-Step Verification"
2. Turn on "Less Secure App Access". 
Without the 2 functions above running, our Python Gmail API will fail. Both functions can be managed at "Manage your Google Account" -> "Security", after which enter the sender credentials and recipients' email addresses in the python code.
```

### How to create a DOS batch file
We need to create a BAT file to run our python script. This is because Windows automation server runs better with bat file than python script.
Most of my python packages are stored in anaconda site-package environment. Hence, I am using Anaconda Prompt as my default command prompt.
```sh
Spawn Anaconda Prompt using Bat file
1. Create a file with .bat extension
2. Paste "call C:\ProgramData\Anaconda3\Scripts\activate.bat"
3. Paste "C:\ProgramData\Anaconda3\python.exe "C:\Users\ZHENHUI\Desktop\onepiece_crawler\manga_crawler.py"
4. Save and close
```

### How to setup Automation Task Scheduler on Windows 10
![](images/Task Scheduler Mainpage.JPG)
