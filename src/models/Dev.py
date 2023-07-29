class Dev:
    """
    Класс для хранения информации о модуле
    """
    def __init__(self, module=None):
        self.name = module.get('name') if module is not None else 'Default'
        self.model = module.get('model') if module is not None else 'Razumdom'
        self.description = module.get('description') if module is not None else 'Default device'
        self.unit_id = module.get('unit_id') if module is not None else 1
        self.baud_rate = module.get('baud_rate') if module is not None else 9600
        self.data_bits = module.get('data_bits') if module is not None else 8
        self.parity = module.get('parity') if module is not None else 'N'
        self.stop_bits = module.get('stop_bits') if module is not None else 2
        if module is not None:
            if module.get('scenarios'):
                self.scenarios = module.get('scenarios')
            else:
                self.scenarios = [{f'Сценарий {i}': ['0x0' for j in range(13)] for d in range(64)} for i in range(64)]
        else:
            self.scenarios = [{f'Сценарий {i}': ['0x0' for j in range(13)] for d in range(64)} for i in range(64)]
        self.reboot = 5678

    def __str__(self):
        return f'''Имя модуля: {self.name}
Модель: {self.model}
Описание: {self.description}
MODBUS: Unit ID {self.unit_id}, {self.baud_rate}/{self.data_bits}-{self.parity}-{self.stop_bits}
----------------------------------------------------------------'''
