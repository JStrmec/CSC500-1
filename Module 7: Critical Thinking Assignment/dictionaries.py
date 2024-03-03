class Dictionaries:
    def __init__(self):
        self.course_number = ['CSC101','CSC102','CSC103','NET110','COM241']

    def create_room_dict(self):
        course_room = ['3004','4501','6755','1244','1411']
        course_number = self.course_number
        return dict(zip(course_number, course_room))

    def create_instructor_dict(self):
        course_instructor = ['Haynes','Alvarado','Rich','Burke','Wright']
        course_number = self.course_number
        instructors = {}
        for index in range(0,len(course_instructor)):
            instructors[course_number[index]] = course_instructor[index]
        return instructors

    def create_meeting_time_dict(self):
        course_meeting = ['8:00 a.m.','9:00 a.m.','10:00 a.m.','11:00 a.m.','1:00 p.m.']
        course_number = self.course_number
        meeting_times = {k: v for k, v in zip(course_number, course_meeting)}
        
        return meeting_times

def main():
    d = Dictionaries()
    rooms = d.create_room_dict()
    instructors = d.create_instructor_dict()
    times = d.create_meeting_time_dict()
    user_input = input('Enter a course number: ')
    while user_input != 'quit':
        if user_input in rooms:
            print(f'The room for {user_input} is {rooms[user_input]}')
            print(f'The instructor for {user_input} is {instructors[user_input]}')
            print(f'The meeting time for {user_input} is {times[user_input]}')
        else:
            print('Course not found')
        user_input = input('Enter a course number: ')
main()