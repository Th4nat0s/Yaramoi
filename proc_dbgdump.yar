
rule proc_dbgdump: dbgprocdum
{
    meta:
        author = "Thanat0s"
        description = "Find a process memory dump (good for carving a lsass)"
    strings:
        $a = { 4D 44 4D 50 93 A7 61 }
        $b = "dbgcore" wide
    condition:
        $b in (@a+512..@a+1536)
}
