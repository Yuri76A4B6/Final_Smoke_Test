В данном репозитории представлен собственный проект по автоматизации действующего сайта с использованием паттерна PageObjectModel и пайтест с подключением логгирования (локально, logger.py) и Allure. Успешным завершением теста является заполнение полей на странице с выполнением заказа. Конечно же полным завершением теста являлось бы оформление заказа 
(клик на красную кнопку "Оформить заказ"), но такими действиями я бы "заспамил" менеджеров сайта)). Ещё раз повторюсь, что проект действующий и каждый раз при выполнении теста оформление заказа помешало бы работе проекта (сайт Минимакс.ру)
Аннотация к коду.
В классе Base написаны методы для общего использования.
current_url - для проверки действующего URL (Uniform resource locator);
assert_word - используется для проверки названия товара;
assert_price - используется для валидации цены на товар на последней странице (сравнивается цена на товар и итоговый прайс)
get_screenshot - для выполнения скриншота по завершению теста
scroll_down - для скролинга экрана. На данном сайте я использовал цепочки активных действий и наведение по локатору так как window.scrollTo({x}, {y}) отрабатывал неадекватно. Связано с работой сайта, скорее всего.
Класс Main_page - в данном классе выполняется получение URL сайта "Минимакс", написаны несколько локаторов без взаимодействия с ними (на будущее), взаимодействие и переход осуществляется во вкладку "Светотехника". 
Класс Light_page - описана страница с различными источниками света. Переход выполняется в Светодиодные лампы.
Led_lamps_page(led_lamps_page.py) - страница боли и кучи переделок кода...Самая большая страница по объему кода. На данной странице выбирается товар по наличию и много-много фильтров для подбора конкретного товара. Местами используется time.sleep(). 
Я знаю, что во многих или вообще ни в каких проектах это не используется, но при выборе товара (при клике на фильтр "В наличии") происходит перезагрузка страницы, поэтому пауза необходима.
На данной странице я убрал два метода и не выбрал все фильтры потому, что сайт работает "криво". При выборе всех фильтров идет долгое раздумье сайт и после этого он перебрасывает на страницу, котороая показывает нам, что ведутся технические работы. Также было замечено, что при выборе некоторых фильтров часть доступных пропадают, перестают быть кликабельными, куда-то скрываются...
Класс - Cart_page(cart_page.py) - на данной странице выполняется проверка названия товара, в отдельную переменную я брал название товара с главной страницы, а на странице корзины название извлечено из локатора в виде текста. После этого выполняется клик на чекбокс для выбора товара и клик для оформления заказа. Далее выполняется переход к следующей странице - к авторизации.
Класс Authorization_page (authorization_page.py)  - это страница авторизации, на ней происходит переход на быструю регистрацию. Можно было бы зарегистрироваться, но многие современные сайты требуют имя, фамилию, номер телефона и почту, но мы же не будем распространять свой номер и почту на весь интернет (этим занимаются мобильные операторы за нас xDDD)
Класс Make_order_page (make_order_page_.py) - на данной странице происходит заполнение полей для оформления заказа -информация о покупателе, выбирается способ заказа, сверяется цена товара с итоговой суммой и далее заполняется поле "Комментарий к заказу".
