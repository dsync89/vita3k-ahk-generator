# About

A set of scripts that generate AutoHotKey (AHK) file to launch game via Vita3K. These AHK scripts is ready to integrate with Launchbox, without you having to create the Argument per game title! Unlike most emulator such as RetroArch, Vita3k CLI uses GameID to run game, not the filename. 

Of course you could rename each game as the GameID itself, but then scraping it to your Frontend such as Launchbox would yield no result because most (if not all) scrapers scrape games based on the filename or foldername, not the GameID which differ per platform.

Note: These AHK script is V1 version, not V2!

# Why These?

Things become tedious to add to your favorite FrontEnd if you imported the whole games like I did, which is a whopping 1824 titles! These are Games Only titles, excluding DLC, Themes, Avatar, etc.

# Pre-requisite

1) The games used here are from **NoPayStation (PSN Content)**, not Commercial Cartridge. You can download these ROMs from the amazing [Erista](https://myrient.erista.me/files/No-Intro/Sony%20-%20PlayStation%20Vita%20(PSN)%20(Content)/) website.

2) You must already imported all games to Vita3K. I suggest you to batch the job using the scripts from my other repo [vita3k-batch-pkg-installer](https://github.com/dsync89/vita3k-batch-pkg-installer), especially if you have more than 100 titles! Even using batch job, it took 3 full days to fully import all 1824 titles to a USB3 connected HDD @7200RPM. Imagine doing it manually via the GUI for each of these titles individually!

# Quick Start

Copy `.emupath.txt` and `.gamedb.txt` from `out` folder into your ROMs folder. Modify the path in `.emupath.txt` to where you put your `Vita3k.exe` emulator.

Copy all `.ahk` scripts from `out/ahk` into the same level as your ROMs folder.

Double click on any `.ahk` file and the game should load.

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

# Generating Output

The `.gamedb.txt` which contains the game title and game ID is generated from `scripts/gen_ahk.py`. Each row in that file consist of the format of `GameTitle|GameID` that the AHK file will lookup to start Vita3K. Vita3K uses GameID to launch game, not game title.

To replicate the work,

Generate a list of AHK for each game in your game folder. If you downloaded from Erista, use that here.
```
python3 gen_ahk.py
```

Generate a `.gamedb.txt` file containing `GameTitle|GameID` that the AHK file will lookup to start Vita3K. Vita3K uses GameID to launch game, not game title.
```
python3 gen_gamedb.py
```

Note that if you run it on ROM for Erista, some games might have `?` instead of it's GameID. The script extract the GameID from the `.pkg` filename and it must have the format of `UP0891-PCSE01356_00-RATAACCESSDENIED_bg_1_608369de8958e541869c6e4e714f395904f7f836.pkg`. So if the `.pkg` filename has the format of `fgcTnrIklUaUeefOmUFQRYSqfpeYTPYGwiMvbYcdRZCwgiYCWHhjthMjiSJnWpXZ.pkg`, the script will simply put a `?` for it. This require manual lookup from the `.tsv` downloadable from NoPayStation: https://nopaystation.com/tsv/PSV_GAMES.tsv. Don't worry as I already try my best to fill in all the `?` in the `out/.gamedb.txt` file so you don't have to do the manual labor work.

# Integrating with Launchbox

Create a new Emulator and name it as `AutoHotKey`. Then use `C:\Program Files\AutoHotkey\v1.1.37.01\AutoHotkeyU64.exe` as the **Application Path**. Uncheck all the checkboxes.

The Sample Command at the bottom **MUST** show the following
```
AutoHotKeyU64.exe "FULL\PATH\TO\ROM\FILE"
```

Note: Make sure to use the v1.x version instead of v2!
