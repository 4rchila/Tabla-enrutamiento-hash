class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def ip_to_int(self, ip: str) -> int:
        octetos = ip.split(".")
        a, b, c, d = [int(x) for x in octetos]
        return (a << 24) + (b << 16) + (c << 8) + d

    def hash_ip(self, ip: str) -> int:
        return self.ip_to_int(ip) % self.size

    def add_route(self, ip: str, interfaz: str):
        index = self.hash_ip(ip)
        self.table[index] = (ip, interfaz)
        print(f"Agregado {ip} -> {interfaz} en índice {index}")

    def find_router(self, ip: str):
        for d in self.table:
            if d is not None:
                if ip == d[0]:
                    print(f"La Ip: {ip}, fue encontrada exitosamente")
                    return
                else:
                    print(f"La Ip: {ip}, no se encuentra registrada")

