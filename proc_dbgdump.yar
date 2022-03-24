
rule proc_dbgdump: dbgprocdump

{
    meta:
        author = "Thanat0s"
        description = "Find a process memory dump (good for carving a lsass)"
        reference = "http://thanat0s.trollprod.org/2014/09/dumper-les-creds-en-memoire-discretement/"
    strings:
        $a = { 4D 44 4D 50 93 A7 61 }
        $b = "dbgcore" wide
    condition:
        $b in (@a+512..@a+1536)
}
