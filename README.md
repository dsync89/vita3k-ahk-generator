# About

A set of scripts that generate AutoHotKey (AHK) file to launch game via Vita3K. These AHK scripts is ready to integrate with Launchbox, without you having to create the Argument per game title! Unlike most emulator such as RetroArch, Vita3k CLI uses GameID to run game, not the filename. 

Of course you could rename each game as the GameID itself, but then scraping it to your Frontend such as Launchbox would yield no result because most (if not all) scrapers scrape games based on the filename or foldername, not the GameID which differ per platform.

Note: These AHK script is V1 version, not V2!

# Why These?

Things become tedious to add to your favorite FrontEnd if you imported the whole games like I did, which is a whopping 1824 titles! These are Games Only titles, excluding DLC, Themes, Avatar, etc.

# Pre-requisite

You must already imported all games to Vita3K. I suggest you to batch the job using the scripts from my other repo [vita3k-batch-pkg-installer](https://github.com/dsync89/vita3k-batch-pkg-installer), especially if you have more than 100 titles! Even using batch job, it took 3 full days to fully import all 1824 titles to a USB3 connected HDD @7200RPM. Imagine doing it manually via the GUI for each of these titles individually!

# Quick Start

Have all your PS Vita game folder renamed according to the DAT file.

This uses the ROMs downloaded from the amazing Erista website: https://myrient.erista.me/files/No-Intro/Sony%20-%20PlayStation%20Vita%20(PSN)%20(Content)/

Generate a list of AHK for each game in your game folder.
```
python3 gen_ahk.py
```

Generate a `.gamedb.txt` file containing `GameTitle|GameID` that the AHK file will lookup to start Vita3K. Vita3K uses GameID to launch game, not game title.
```
python3 gen_gamedb.py
```

Create a `.emupath` file in your ROm folder


Example of the final dir
```
|- .emupath.txt
|- .gamedb.txt
|- Game1.ahk
|- Game2.ahk
|- [Game1]
|- [Game2]
...
```

# Integrating with Launchbox

Create a new Emulator and name it as `AutoHotKey`. Then use `C:\Program Files\AutoHotkey\v1.1.37.01\AutoHotkeyU64.exe` as the **Application Path**. Uncheck all the checkboxes.

The Sample Command at the bottom **MUST** show the following
```
AutoHotKeyU64.exe "FULL\PATH\TO\ROM\FILE"
```

Note: Make sure to use the v1.x version instead of v2!