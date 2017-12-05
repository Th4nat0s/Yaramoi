rule Dracula
{
meta:
author = "Thanatos@trollprod.org"
maltype = "pws"
        
    strings:
        $a1 = "DraculaTextBox"
        $a2 = "DraculaButton"
        $a3 = "get_RECOVERY_ALL"
        
    condition:
        all of them
}
