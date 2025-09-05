class HashTable:
    def __init__(self, size=5):
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
        start_index = index  # Se guarda el idnice inicial para detener bucles infinitos

        while self.table[index] is not None:
            # Si la IP ya está registrada, se actualiza
            if self.table[index][0] == ip:
                self.table[index] = (ip, interfaz)
                print(f"Actualizada {ip} -> {interfaz} en índice {index}")
                return
            # Si no es la misma IP, se prueba la siguiente casilla
            index = (index + 1) % self.size
            if index == start_index:
                print("La tabla está llena, no se puede insertar.")
                return

        # Encontramos un espacio vacío
        self.table[index] = (ip, interfaz)
        print(f"Agregado {ip} -> {interfaz} en índice {index}")

    def find_router(self, ip: str):
        index = self.hash_ip(ip)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == ip:
                print(f"La IP {ip} fue encontrada en índice {index} -> Interfaz: {self.table[index][1]}")
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:  # se dio toda la vuelta
                break

        print(f"La IP {ip} no se encuentra registrada")
        return None
