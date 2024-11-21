class Employee:
    _team = []
    def __init__(self,name,id):
        self.__name = name
        self.__id = id
    def get_info(self):
        return f'Имя: {self.__name}\nID: {self.__id}'
    def get_team_info(self=None):
        for i in Employee._team:
            print(i)

class Technician(Employee):
    def __init__(self,spec,name,id):
        self._spec = spec
        Employee.__init__(self,name, id)
    def get_info(self):
        return f'{Employee.get_info(self)}\nСпециализация: {self._spec}\n'
    def perform_maintenance(self):
        return f'{self.__name} выполняет тех. обслуживание'

class Manager(Employee):
    def __init__(self,dep,name,id):
        self._dep = dep
        Employee.__init__(self,name,id)
    def get_info(self):
        return f'{Employee.get_info(self)}\nОтдел: {self._dep}\n'
    def manage_project(self):
        return f'{self.__name} руководит проектом'

class TechManager(Manager, Technician):
    def __init__(self,dep,spec,name,id):
        Technician.__init__(self,spec,name,id)
        Manager.__init__(self,dep,name,id)
    def get_info(self):
        return f'{Employee.get_info(self)}\nСпециализация: {self._spec}\nОтдел: {self._dep}\n'
    def manage_project(self):
        return super().manage_project()
    def perform_maintenance(self):
        return super().perform_maintenance()
    def add_employee(self):
        if self not in Employee._team:
            Employee._team.append(self.get_info())
        return Employee._team
    def remove_employee(self):
        Employee._team.remove(self.get_info())
        return Employee._team

tm1 = TechManager('Отдел','ТехМенеджер','Денис','2401')
tech1 = Technician('ТехСпециалист','Миша','2402')
tech2 = Technician('ТехСпециалист','Игорь','2403')
tech3 = Technician('ТехСпециалист','Артём','2404')
man1 = Manager('Менеджмент','Никита','2405')

TechManager.add_employee(tm1)
TechManager.add_employee(tech1)
TechManager.add_employee(tech2)
TechManager.add_employee(tech3)
TechManager.add_employee(man1)

Employee.get_team_info()