class ListTasksBuilder:
    def __init__(self, user_list:list[str]):
        self.user_list = user_list

    def access(self, index: int) -> None:
        print(self.user_list[index])

    def modify(self, index:int, new_value:str):
        self.user_list[index] = new_value

    def slice(self, start_index:int, end_index:int):
        print(self.user_list[start_index:end_index])

student_names: list[str] = ['Minahil', 'Zahida', 'Saghir', 'Amir', 'Tariq']
task_list : ListTasksBuilder = ListTasksBuilder(student_names)

task_list.access(1)

task_list.modify(0, 'Fatima')
task_list.access(0)

task_list.slice(1,3)