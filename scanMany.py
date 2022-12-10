from socket import gethostbyaddr, gethostbyname
from scan import scanTarget

def scanTargets(host, ports): 
  try: 
    targetIp = gethostbyname(host)
  except:
    print("unrecoverable host")
  try: 
    targetName = gethostbyaddr(targetIp)
    print(f"Results of {targetName}:")
  except: 
    print(f"Results of {targetIp}:")
  
  for port in ports:
    scanTarget(host, int(port))