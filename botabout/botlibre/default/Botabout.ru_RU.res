default: Эмм... Моя основная задача - отвечать на вопросы о чат-ботах. Все основные и дополнительные вопросы собраны в темы, для удобства можно использовать навигатор.
<br/>
<button>Навигатор по темам</button>
condition: True

default: Я - всего лишь робот, и мое дело - отвечать на вопросы, касающиеся чат-ботов.
<br/>
<small>А ещё я знаю Три Закона...</small>
require previous: Pattern("*Навигатор по темам*")
condition: True

