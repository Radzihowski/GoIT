# Пул потоків
#
# В Python існує ще один механізм написання асинхронного коду. Ви можете скористатися пакетом concurrent.futures.
# Він дозволяє піднятися на вищий рівень абстракції, коли вам просто потрібно паралельно виконати ряд однотипних
# завдань і немає необхідності вдаватися до низькорівневих деталей реалізації.
#
# Основна ідея полягає у використанні реалізації абстрактного класу Executor. У concurrent.futures є дві реалізації
# цього абстрактного базового класу: ProcessPoolExecutor — для виконання коду окремих процесів (з ним ми познайомимося
# пізніше) та ThreadPoolExecutor — для виконання в окремих потоках.
#
# Кожен такий Executor приховує набір потоків або процесів, яким ви можете дати роботу та отримати результат її
# виконання. Вам не потрібно вручну управляти створенням потоків та їх коректним завершенням.
#
# Звичайно, все ще потрібно пам'ятати про доступ до загальних ресурсів та примітиви синхронізації.