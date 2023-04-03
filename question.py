


############################################### QUESTION CLASS ##############################################
class Question:
    def __init__(self,a_question="",a_points=0):
        # checking if points given are positive
        try:
            if (a_points < 0):
                raise ValueError("Points of question cannot be negative!")
            else:
                self.question = a_question
                self.points = a_points
        except ValueError as ve:
            print(ve)

    def set_question(self,a_question=""):
        if(a_question!=""):
            self.question = a_question

    def set_points(self,a_points):
        try:
            if (a_points < 0):
                raise ValueError("Points of question cannot be negative!")
            else:
                self.points = a_points
        except ValueError as ve:
            print(ve)


    def get_question(self):
        return self.question

    def get_points(self):
        return self.points

    def print(self):
        final = " ({} points)".format(self.points)
        final = self.question + final
        print(final)

    def score(self,a_score=""):
        pass


################################## FillInTheBlank Class ################################
class FillInTheBlank(Question):
    def __init__(self,a_question,a_points,a_answer):
        super().__init__(a_question,a_points)
        if a_answer!="":
            self.answer = a_answer

    def score(self,stud_answer=""):
        if stud_answer==self.answer:
            return self.points
        else:
            return 0

    def set_answer(self,stud_answer=""):
        if stud_answer!="":
            self.answer = stud_answer

    def get_answer(self):
        return self.answer


########################################## MultipleChoiceQuestion class ##############################
class MultipleChoice(Question):
    def __init__(self, a_question, a_points, a_choices=[], a_answer=""):
        super().__init__(a_question,a_points)
        self.list_of_choices = a_choices
        self.answer = a_answer

    def score(self,stud_answer=""):
        if(stud_answer==self.answer):
            return self.points
        else:
            return 0

    def print(self):
        super().print()
        print()
        for index,choice in enumerate(self.list_of_choices):
            print(f'{chr(97+index)}) ' + choice)

