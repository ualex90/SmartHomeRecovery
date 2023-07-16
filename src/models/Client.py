class Client:
    """
    Класс для хранения информации о клиенте tcp
    """
    def __init__(self, client):
        self.client = client.get("name") if client is not None else 'localhost'
        self.ip = client.get("ip") if client is not None else '127.0.0.1'
        self.port = client.get("port") if client is not None else 502

    def __str__(self):
        return f'''Клиент: {self.client} 
addr: {self.ip}:{self.port}'''
