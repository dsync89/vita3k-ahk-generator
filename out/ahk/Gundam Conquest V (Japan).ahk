; Author: dsync89
; Get the path of the script (including the script's directory)
scriptPath := A_ScriptFullPath
scriptDirectory := StrReplace(scriptPath, A_ScriptName, "")

; Combine the script's directory with the filename
emupathFile := scriptDirectory . ".emupath.txt"
gamedbFile := scriptDirectory . ".gamedb.txt"

FileRead, Vita3kPath, %emupathFile%
if Vita3kPath =
{
    MsgBox, Could not read Vita3k path from .emupath.txt
    ExitApp
}

ScriptFileName := SubStr(A_ScriptName, 1, StrLen(A_ScriptName) - 4) ; Remove ".ahk" extension

Loop, read, %gamedbFile%
{
    LineText := A_LoopReadLine
    if LineText = ; Exit the loop when no more lines are left
        break

    ; Split the line into Title and GameID
    StringSplit, GameInfo, LineText, `|
    GameTitle := Trim(GameInfo1)
    GameID := Trim(GameInfo2)

    ; Check if the AHK script's filename matches the GameTitle
    if (GameTitle = ScriptFileName)
    {
        Run, %Vita3kPath% -r %GameID%
        return
    }
}

#IfWinActive ahk_exe Vita3K.exe
Escape::
    Process, Close, Vita3K.exe
    Run, taskkill /im Vita3K.exe /F,, Hide
    ExitApp
return