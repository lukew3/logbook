# Python Logbook
This program enables it's users to instantly make a logbook entry from the terminal. The program instantly creates folders that correspond to the date that each entry was published. Each file is named as date_time. If you want to see all logs at once, you can do such with combineLogs.py, which will concatenate all logs into one long logbook.

## Getting Started
This app can be installed with pip3
```
pip3 install pythonlogbook
```
or pip
```
pip install pythonlogbook
```
You can also install this on debian-based operating systems using these commands. However, these repositories are not regularly updated and this method is not recommended.
```
sudo add-apt-repository ppa:lukew3/logbook
sudo apt update
sudo apt install logbook
```

## Alternate install method
The python logbook was designed to be as convenient as possible. If you do it right, you should be able to simply run `logbook` into the terminal and create a log entry.

### Setting up directory
As of right now, the only way to change the folder where the logs are stored is by editing the variable originalPath so that line 11 of logbook.py says `originalPath = r"folderLocation"`.

Once you set this up, you should be able to run the program through the terminal by running `python logbook.py` while in the folder that the file is in.

### Using the Command Line Interface
To create a new log, run: `newlog` in your terminal. To combine logs, run: `combinelogs`. It's as easy as that!

## Built with
* Python

## Author

* **Luke Weiler** - [lukew3](https://github.com/lukew3)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
