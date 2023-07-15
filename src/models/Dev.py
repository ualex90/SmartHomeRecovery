class Dev:
    """
    Класс для хранения информации о модуле
    """
    def __init__(self, client, module=None):
        self.client = client.get("client") if client is not None else 'localhost'
        self.ip = client.get("ip") if client is not None else '127.0.0.1'
        self.port = client.get("port") if client is not None else 502
        self.name = module.get('name') if module is not None else 'Default'
        self.model = module.get('model') if module is not None else 'Razumdom'
        self.description = module.get('description') if module is not None else 'Default device'
        self.unit_id = module.get('unit_id') if module is not None else 1
        self.baud_rate = module.get('baud_rate') if module is not None else 9600
        self.data_bits = module.get('data_bits') if module is not None else 8
        self.parity = module.get('parity') if module is not None else 'N'
        self.stop_bits = module.get('stop_bits') if module is not None else 2
        self.scenarios = module.get('scenarios') if module is not None else []
        self.reboot = 5678

    def __str__(self):
        return f'''Клиент: {self.client} 
addr: {self.ip}:{self.port}
----------------------------------------------------------------
Имя модуля: {self.name}
Модель: {self.model}
Описание: {self.description}
modbus: {self.baud_rate}/{self.data_bits}-{self.parity}-{self.stop_bits}
Количество сценариев: {len(self.scenarios)}
----------------------------------------------------------------'''
