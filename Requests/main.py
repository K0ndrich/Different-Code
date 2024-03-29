import requests

# q - первый атрибут во всех запросах в google
my_attributes = {"q": "hello"}

# даем запрос к сайту
# params указывате параметры для нашего get запроса
response = requests.get(
    "https://soundcloud.com/you/likes",
)

# response.status_code возвращает статус ответа от сайта в виде Код Ответа 200 , Код Ответа 404
# response.headers возвращает заголовки ответов от сайта

# response.content возвращает содержимое страници html , css , js в вдие байтовой строки
# response.text возвращает содержимое страници html , css , js в виде текста (можна сохранить в своем проекте)
