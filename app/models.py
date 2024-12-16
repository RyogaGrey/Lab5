from neomodel import StructuredNode, StringProperty, IntegerProperty, Relationship, UniqueIdProperty

# Модель узла пользователя (User)
class UserNode(StructuredNode):
    uid = UniqueIdProperty()  # Уникальный идентификатор узла
    vk_id = IntegerProperty(required=True, unique_index=True)  # ID пользователя VK
    name = StringProperty(required=True)  # Полное имя пользователя
    screen_name = StringProperty()  # Короткое имя пользователя (может быть пустым)
    sex = IntegerProperty()  # Пол (1 - женщина, 2 - мужчина, 0 - неизвестно)
    city = StringProperty()  # Город проживания (например, "Tyumen")

    # Связи
    followers = Relationship("UserNode", "FOLLOWS")  # Подписчики
    subscriptions = Relationship("GroupNode", "SUBSCRIBES")  # Подписки на группы

# Модель узла группы (Group)
class GroupNode(StructuredNode):
    uid = UniqueIdProperty()  # Уникальный идентификатор узла
    vk_id = IntegerProperty(required=True, unique_index=True)  # ID группы VK
    name = StringProperty(required=True)  # Название группы
    screen_name = StringProperty()  # Короткое имя группы

    # Связи
    subscribers = Relationship("UserNode", "SUBSCRIBES")  # Подписчики на группу
