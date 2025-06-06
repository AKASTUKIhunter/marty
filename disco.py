from connect import MartyConnection

marty = MartyConnection()
marty.connect("192.168.1.6")

marty.marty.disco_named_pattern(marty.marty.Disco.EYES, pattern="show-off")
marty.marty.dance()
