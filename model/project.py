from sys import maxsize

status = ["в разработке", "выпущен", "стабильный", "устарел"]
view_state = ["публичный", "приватный"]

class Project:
    def __init__(self, id=None, name=None, state=None, is_active=None, use_global_setting=None, visible=None, description=None):
        self.id = id
        self.name = name
        self.state = state
        self.is_active = is_active  # не участвует при создании проекта
        self.use_global_setting = use_global_setting  # отсутствует на с странице проектов
        self.visible = visible
        self.description = description

    def __repr__(self):
        return f"id:{self.id}, name:{self.name}, state:{self.state}, is_active:{self.is_active}, " \
               f"use_global_setting:{self.use_global_setting}, visible:{self.visible}, description:{self.description}"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        equal_id = self.id == None or other.id == None or self.id == other.id
        equal_name = self.name == other.name
        equal_state = self.state == other.state
        equal_is_active = self.is_active == other.is_active
        equal_visible = self.visible == other.visible
        equal_description = self.description == other.description

        return equal_id and equal_name and equal_state and equal_is_active and equal_visible and equal_description

    def id_or_max(self):
        return self.id if self.id else maxsize

    def set_default_value(self):
        if self.state is None:
            self.state="выпущен"
        if self.is_active is None:
            self.is_active = True
        if self.visible is None:
            self.visible = "приватный"
        if self.description is None:
            self.description = ''
        return self