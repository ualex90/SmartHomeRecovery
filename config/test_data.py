# Настройка устройств
TEST_MODULES = [{"name": "Test_1", "model": "Razumdom", "result": int("0x0000", 16),
                 "unit_id": 1, "baud_rate": 9600, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_2", "model": "Razumdom", "result": int("0x0100", 16),
                 "unit_id": 2, "baud_rate": 9600, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_3", "model": "Razumdom", "result": int("0x0200", 16),
                 "unit_id": 3, "baud_rate": 9600, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_4", "model": "Razumdom", "result": int("0x0300", 16),
                 "unit_id": 4, "baud_rate": 9600, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_5", "model": "Razumdom", "result": int("0x0400", 16),
                 "unit_id": 5, "baud_rate": 9600, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_6", "model": "Razumdom", "result": int("0x0500", 16),
                 "unit_id": 6, "baud_rate": 9600, "data_bits": 8, "parity": "O", "stop_bits": 1},

                {"name": "Test_7", "model": "Razumdom", "result": int("0x0001", 16),
                 "unit_id": 7, "baud_rate": 19200, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_8", "model": "Razumdom", "result": int("0x0101", 16),
                 "unit_id": 8, "baud_rate": 19200, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_9", "model": "Razumdom", "result": int("0x0201", 16),
                 "unit_id": 9, "baud_rate": 19200, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_10", "model": "Razumdom", "result": int("0x0301", 16),
                 "unit_id": 10, "baud_rate": 19200, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_11", "model": "Razumdom", "result": int("0x0401", 16),
                 "unit_id": 11, "baud_rate": 19200, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_12", "model": "Razumdom", "result": int("0x0501", 16),
                 "unit_id": 12, "baud_rate": 19200, "data_bits": 8, "parity": "O", "stop_bits": 1},

                {"name": "Test_13", "model": "Razumdom", "result": int("0x0002", 16),
                 "unit_id": 13, "baud_rate": 38400, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_14", "model": "Razumdom", "result": int("0x0102", 16),
                 "unit_id": 14, "baud_rate": 38400, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_15", "model": "Razumdom", "result": int("0x0202", 16),
                 "unit_id": 15, "baud_rate": 38400, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_16", "model": "Razumdom", "result": int("0x0302", 16),
                 "unit_id": 16, "baud_rate": 38400, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_17", "model": "Razumdom", "result": int("0x0402", 16),
                 "unit_id": 17, "baud_rate": 38400, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_18", "model": "Razumdom", "result": int("0x0502", 16),
                 "unit_id": 18, "baud_rate": 38400, "data_bits": 8, "parity": "O", "stop_bits": 1},

                {"name": "Test_19", "model": "Razumdom", "result": int("0x0003", 16),
                 "unit_id": 19, "baud_rate": 57600, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_20", "model": "Razumdom", "result": int("0x0103", 16),
                 "unit_id": 20, "baud_rate": 57600, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_21", "model": "Razumdom", "result": int("0x0203", 16),
                 "unit_id": 21, "baud_rate": 57600, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_22", "model": "Razumdom", "result": int("0x0303", 16),
                 "unit_id": 22, "baud_rate": 57600, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_23", "model": "Razumdom", "result": int("0x0403", 16),
                 "unit_id": 23, "baud_rate": 57600, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_24", "model": "Razumdom", "result": int("0x0503", 16),
                 "unit_id": 24, "baud_rate": 57600, "data_bits": 8, "parity": "O", "stop_bits": 1},

                {"name": "Test_25", "model": "Razumdom", "result": int("0x0004", 16),
                 "unit_id": 25, "baud_rate": 115200, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_26", "model": "Razumdom", "result": int("0x0104", 16),
                 "unit_id": 26, "baud_rate": 115200, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_27", "model": "Razumdom", "result": int("0x0204", 16),
                 "unit_id": 27, "baud_rate": 115200, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_28", "model": "Razumdom", "result": int("0x0304", 16),
                 "unit_id": 28, "baud_rate": 115200, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_29", "model": "Razumdom", "result": int("0x0404", 16),
                 "unit_id": 29, "baud_rate": 115200, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_30", "model": "Razumdom", "result": int("0x0504", 16),
                 "unit_id": 30, "baud_rate": 115200, "data_bits": 8, "parity": "O", "stop_bits": 1},

                {"name": "Test_31", "model": "Razumdom", "result": int("0x0005", 16),
                 "unit_id": 31, "baud_rate": 230400, "data_bits": 8, "parity": "N", "stop_bits": 2},
                {"name": "Test_32", "model": "Razumdom", "result": int("0x0105", 16),
                 "unit_id": 32, "baud_rate": 230400, "data_bits": 8, "parity": "N", "stop_bits": 1},
                {"name": "Test_33", "model": "Razumdom", "result": int("0x0205", 16),
                 "unit_id": 33, "baud_rate": 230400, "data_bits": 8, "parity": "E", "stop_bits": 2},
                {"name": "Test_34", "model": "Razumdom", "result": int("0x0305", 16),
                 "unit_id": 34, "baud_rate": 230400, "data_bits": 8, "parity": "E", "stop_bits": 1},
                {"name": "Test_35", "model": "Razumdom", "result": int("0x0405", 16),
                 "unit_id": 35, "baud_rate": 230400, "data_bits": 8, "parity": "O", "stop_bits": 2},
                {"name": "Test_36", "model": "Razumdom", "result": int("0x0505", 16),
                 "unit_id": 36, "baud_rate": 230400, "data_bits": 8, "parity": "O", "stop_bits": 1},
                ]
