from my_subnet_librairy import *

mask="255.255.252.0"
ip_address="1.1.1.1"
     
print("number of host: "+str(get_nb_host(mask)))
print("size of the mask: "+str(get_no_of_ones(mask)))
print("wildcard mask: "+get_wildcard_mask(mask))
print("broad ast address: "+get_broadcast_address(ip_address,mask))
print("randonm address in subnet: "+generate_random_ip_address_from_subnet(ip_address,mask))
