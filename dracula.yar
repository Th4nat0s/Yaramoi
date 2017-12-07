rule Dracula
{
meta:
author = "Th4nat0s"
maltype = "pws"
        
    strings:
        $a1 = "DraculaTextBox"
        $a2 = "DraculaButton"
        $a3 = "get_RECOVERY_ALL"
        
    condition:
        all of them
}
