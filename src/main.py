from hash_tabla import HashTable
tabla = HashTable()

tabla.add_route("192.168.0.1", "eth0")
tabla.add_route("192.168.0.2", "eth1")
tabla.add_route("192.168.0.3", "eth2")
tabla.add_route("192.168.0.4", "eth3")

tabla.add_route("192.168.0.5", "eth4")  # Esta debería causar "tabla llena"

# Busqueda de todas las IPs para ver si se encuentran correctamente
for ip in ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5"]:
    tabla.find_router(ip)

tabla.add_route("192.168.0.2", "ethX")  # Se actualiza la interfaz de esta IP
tabla.find_router("192.168.0.2")
