"""Это модуль из моего проекта магазина... Это я делаю по книге...
    В книге описывается, как должен работать backend и все подробно объясняется..."""


import typing
from datetime import datetime
from dataclasses import dataclass

class OutOfStock:
    pass


@dataclass(frozen=True)
# ===============================   товарная позиция   ==========================================================
class OrderLine:
    orderid: str                                    # артикул товара
    product_name: str                               # наименование товара
    # sku: str                                        # sku - единица складского учета (stock-keeping unit)
    qty: int                                        # qty- количество товара (quantity)



# ============================== Изменение остатков в партии товара при его покупке или продаже =================
class Batch:
    def __init__(self, ref: str, product_name: str, qty: int, eta: typing.Optional[datetime.date]):
        self.reference = ref                        # ссылка на ордер (order reference)
        self.product_name= product_name             # наименование товара
        # self.sku = sku                              # sku - единица складского учета (stock-keeping unit)
        self.eta = eta                              # eta (estimated arrival time) - предполагаемый срок прибытия товара на склад
        self._purchased_quantity = qty              # qty- партия товара на складе, приобретенное количество (quantity) товара
        self._allocations = set()                   # уменьшает количество товара в партии (заказ покупателя или списание товара)


    def __eq__(self, other):
        # Это не экземпляр класса ?
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        # Сортировка по дате eta (чем раньше, тем лучше)
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


    # Добавление товара в _allocation (уменьшает количество товара в партии)
    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)
            print('allocate add ->  {}'.format(self._allocations))


    # Удаление товара из _allocation (увеличивает количество товара в партии)
    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)
            print('allocate remove ->  {}'.format(self._allocations))


    # Выделенное (купленное или проданное) количество. Используется в функции available_quantity()
    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)
    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity


    # Сравниваем товар (что есть на складе и что заказали покупатели, self.product_name == line.product_name)
    # Сравниваем количество остатков на складе и тем, что заказал покупатель. Товара на складе должно быть >= тому, что заказал покупатель
    def can_allocate(self, line: OrderLine) -> bool:
        # print('can_allocate -> {}={} and {} >= {}'.format(self.product_name, line.product_name, self.available_quantity, line.qty))
        return self.product_name == line.product_name and self.available_quantity >= line.qty


# Вспомогательная функция для сортировки заказа по времени (чем раньше заказ будет на складе, тем быстрее поступит в продажу)
# Функция использует оператор перегрузки __gt__ и возвращает ссылку на ордер с более ранним поступлением на склад
def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(
        b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock


if __name__ == '__main__':
    # Создаем продукт
    product1, product2 = 'table', 'lamp'

    # Создаем ордера на покупку
    order_on_table = OrderLine(orderid='00001', product_name=product1, qty=2)
    order_on_lamp = OrderLine(orderid='00002', product_name=product2, qty=7)

    # Задаем остатки на складе
    batch_1 = Batch(ref='001', product_name=product1, qty=10, eta=None)
    batch_2 = Batch(ref='002', product_name=product2, qty=20, eta=None)

    print(batch_1.allocate(order_on_table))    # Функция allocate возвращает еще и None потому, что ничего не возвращает, а просто добавляет товар в продажу
    print(batch_2.allocate(order_on_lamp))     # Функция allocate возвращает еще и None потому, что ничего не возвращает, а просто добавляет товар в продажу

    print(f'Остатки товара {product1} = ', batch_1.available_quantity)
    print(f'Остатки товара {product2} = ', batch_2.available_quantity)