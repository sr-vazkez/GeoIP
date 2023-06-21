import requests
from decouple import config


class ConsultorCiudadOrigen:
    def __init__(self, ip):
        self.ip = ip
        self.servicios = [
            self.consultar_geolocation,
            self.consultar_ipinfo,
            self.consultar_hostip,
            self.consultar_geoiplookup_io,
            self.consultar_ipapi_com,
            self.consultar_freegeoip,
        ]

    def obtener_ciudad_origen(self):
        ciudades = [servicio() for servicio in self.servicios]
        ciudad_mas_comun = max(set(ciudades), key=ciudades.count)

        if ciudades.count(ciudad_mas_comun) == len(ciudades):
            return {
                "status": True,
                "msg":f"Ciudad origen: {ciudad_mas_comun}",
                "ip_address": f"{self.ip}"
                }
        else:
            return {
                "status": True,
                "msg":f"Probable Ciudad Origen: {ciudad_mas_comun}",
                "ip_address": f"{self.ip}"
                }

    def consultar_geolocation(self):
        return self.consultar_servicio(f"https://geolocation-db.com/json/{self.ip}&position=true")

    def consultar_ipinfo(self):
        # token = "f0bf2a5d16e6ec"
        return self.consultar_servicio(f"https://ipinfo.io/{self.ip}/json?token={config('IP_INFO_TOKEN')}")

    def consultar_hostip(self):
        return self.consultar_servicio(f"http://api.hostip.info/get_json.php?{self.ip}")

    def consultar_geoiplookup_io(self):
        return self.consultar_servicio(f"https://json.geoiplookup.io/{self.ip}")

    def consultar_ipapi_com(self):
        return self.consultar_servicio(f"http://ip-api.com/json/{self.ip}")

    def consultar_freegeoip(self):
        return self.consultar_servicio(f"https://api.ipbase.com/v1/json/{self.ip}")

    def consultar_servicio(self, url):
        response = requests.get(url)
        data = response.json()
        ciudad = data.get("city", "")
        return ciudad
