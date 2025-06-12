from connect import MartyConnection

marty_connec = MartyConnection()
marty_connec.connect("192.168.1.6")

marty_connec.marty.disco_named_pattern(marty_connec.marty.Disco.EYES, pattern="show-off")
marty_connec.marty.dance()
