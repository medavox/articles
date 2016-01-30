#SingleInstance Force
#NoTrayIcon
SetBatchLines, -1
; Process, Priority,, High
Title := "Totally Rad Time Tracker"
Gui()
DllCall( "RegisterShellHookWindow", UInt,Hwnd )
MsgNum := DllCall( "RegisterWindowMessage", Str,"SHELLHOOK" )
OnMessage( MsgNum, "ShellMessage" )
TimeActiv8d := A_Now
MsActiv8d := A_MSec
oldActiveWindow := WinExist()
Return

;wParam is the message number
;lParam is the ahk id

Gui()
{
    Global
    Gui, +LastFound +AlwaysOnTop +Resize ; +ToolWindow
    Gui, Margin, 0, 0
    Gui, Font, s8, Microsoft Sans Serif
    Gui, Color,, DEDEDE
    Gui, Add, ListView, w400 r10 vData +Grid, Process|Title|Time(ms) ;+Sort, 
    LV_ModifyCol( 1, 100 ), LV_ModifyCol( 2, 200 ), LV_ModifyCol( 3, 60 )
    ;LV_ModifyCol(3, Integer Logical)
    Gui, Show,, %Title%

}

DateCompare(date_then, ms_then)
{
    date_now := A_Now
    ms_now := A_MSec
    
    date_now -= date_then, Seconds
    ms_now -= ms_then
    precisionDiff := date_now * 1000
    precisionDiff += ms_now
    ;return % date_now . ".seconds," . ms_now . "ms" ;%
    ;return % precisionDiff . "ms" ;%
    return precisionDiff
    ;return % A_now . "-" . date_then . "=" . date_now ;%
}

ShellMessage( wParam, lParam ) 
{
    ;HSHELL_WINDOWACTIVATED
    if (wParam = 4)
    {
        Global TimeActiv8d, MsActiv8d, rowNum, OldActiveWindow
        WinGetTitle, title, ahk_id %OldActiveWindow%
        WinGet, pname, ProcessName, ahk_id %OldActiveWindow%
        WinGet, pid, PID, ahk_id %OldActiveWindow%
    
        msg := DateCompare(TimeActiv8d, MsActiv8d)
        LV_Add( "", pname, title, msg )
        oldActiveWindow := lParam
        TimeActiv8d := A_Now
        MsActiv8d := A_MSec
    }
}

GuiSize:
GuiControl, Move, Data, w%A_GuiWidth% h%A_GuiHeight%
GuiControl, Move, Data, w%A_GuiWidth% h%A_GuiHeight%
Return

GuiClose:
GuiEscape:
ExitApp
Return

NumpadAdd::Reload
NumpadSub::ExitApp
