"""Practical 7: Simple rule-based Student Support Chatbot."""

class StudentSupportChatbot:
    def __init__(self):
        self.intro_message = 'Hello! I am your Student Support Chatbot. How can I help you today?'
        self.commands = {
            'courses': self.get_courses,
            'schedule': self.get_schedule,
            'location': self.get_location,
            'exit': self.exit_chat,
        }

    def get_courses(self):
        courses = ['Mathematics', 'Physics', 'Computer Science', 'Biology']
        return 'We offer the following courses: ' + ', '.join(courses)

    def get_schedule(self):
        schedule = {
            'Mathematics': 'Mon-Wed 10:00 AM - 12:00 PM',
            'Physics': 'Tue-Thu 1:00 PM - 3:00 PM',
            'Computer Science': 'Mon-Wed 2:00 PM - 4:00 PM',
            'Biology': 'Tue-Thu 3:00 PM - 5:00 PM',
        }
        return '\n'.join(f'{course}: {time}' for course, time in schedule.items())

    def get_location(self):
        return 'The university is located at 123 University Ave, Springfield.'

    def exit_chat(self):
        return 'Thank you for chatting with me! Have a great day!'

    def handle_input(self, user_input):
        user_input = user_input.lower()
        if 'course' in user_input:
            return self.get_courses()
        elif 'schedule' in user_input:
            return self.get_schedule()
        elif 'location' in user_input:
            return self.get_location()
        elif 'exit' in user_input:
            return self.exit_chat()
        else:
            return "Sorry, I didn't understand that. Can you ask something else?"

    def start_chat(self):
        print(self.intro_message)
        while True:
            user_input = input('You: ')
            response = self.handle_input(user_input)
            print('Chatbot: ' + response)
            if 'exit' in user_input.lower():
                break

if __name__ == '__main__':
    chatbot = StudentSupportChatbot()
    chatbot.start_chat()
