class PrinterQueue:

    def __init__(self, printer_queue: list = None):
        if printer_queue is None:
            self.__printer_queue = []
        else:
            self.__printer_queue = printer_queue

    def add_document(self, document_name):
        self.__printer_queue.append(document_name)
        return f'{document_name} помещен в очередь печати'

    # def print_document(self):
    #     document = self.__printer_queue.pop(0)
    #     return f'Печать {document}....'

    def print_documents(self):
        while self.__printer_queue:
            document = self.__printer_queue.pop(0)
            print(f'Печать {document}....')
        return "Очередь печати пуста"


hp_printer = PrinterQueue()
kyocera_printer = PrinterQueue(['Документ kyocera 1', 'Документ kyocera 2'])

hp_printer.add_document('Отчет hp 1')
hp_printer.add_document('Отчет hp 2')
print(hp_printer.print_documents())
print()

kyocera_printer.add_document('Документ kyocera 3')
kyocera_printer.add_document('Документ kyocera 4')
print(kyocera_printer.print_documents())
