class Garden:
    students_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students = students_list):
        self.diagram = diagram
        self.students = students

    def garden(self):
        myDict = {'V': 'Violets', 'R': 'Radishes', 'C':'Clover', 'G':'Grass'}

        kindergarten_garden = {'Alice': [], 'Bob': [], 'Charlie':[], 'David':[], 'Eve':[], 'Fred':[], 'Ginny': [], 'Harriet':[], 'Ileana':[], 'Joseph': [], 'Kincaid': [], 'Larry': []}

        diagram_splitted = self.diagram.split()
        for plants in diagram_splitted:
            k = 0
            j = 1
            for i, plant in enumerate(plants):
                kindergarten_garden.setdefault(self.students[k], []).append(myDict[plant])
                if(j%2 == 0):
                    k+=1
                j+=1
        return kindergarten_garden
