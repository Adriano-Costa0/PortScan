import pyfiglet

banner = pyfiglet.figlet_format("ADR_SCAN")

def showManual():
  print(banner)
  print("\n - Parameters \n\n#   host - target host to be scanned")
  print("#   1-100 - range of ports that will be scanned, if not passed, the default will be from 1 to 1024")
  print("#   -man - show tool help manual")

showManual()