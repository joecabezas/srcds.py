#!/usr/bin/env python

from SRCDS import SRCDS

#Login to our server
#serverAddress = socket.gethostbyname(socket.gethostname())
serverAddress = "192.168.0.11"

server = SRCDS(serverAddress, 27015, "macondo")
print server.nplayers()

#try:
	#server = SRCDS(serverAddress, 27015, "macondo")
	#print "[SRCDS] Reloading sourcemod"
	#server.say("[SRCDS] Reloading sourcemod")
	#server.rcon_command("sm plugins unload_all")
	#server.rcon_command("sm plugins refresh")
	#print "[SRCDS] Reload completed"
	#server.say("probando")
	#server.players
#except:
	#print "[SRCDS] Could not connect to server ", serverAddress
#print "end of script"