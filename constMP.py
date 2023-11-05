#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
#PEERS_SAME_REGION = ['18.211.6.152','44.216.125.255','54.210.115.4','44.207.136.9','34.205.13.18','3.234.217.135']
PEERS_SAME_REGION = ['44.216.125.255','54.210.115.4']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['18.211.6.152','44.216.125.255','54.210.115.4','44.207.136.9','44.242.104.128','44.224.229.0']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 2   # Number of peers
SERVER_ADDR ='18.211.6.152'
SERVER_PORT = 5678

