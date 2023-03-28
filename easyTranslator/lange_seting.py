
class lange_select:
    def __init__(self):
        self.lange_dic()
        self.lange_lis()
        self.matinent_select()
    def lange_dic(self):
        self.dic = {
            0: 'Chinese',
            1: 'English',
            2: 'French',
            3: 'German',
            4: 'Japanese',
            5: 'Korean',
            6: 'Spanish',
            7: 'Portuguese',
            8: 'Italian'
        }
        return self.dic
    def lange_lis(self):
        self.lis=[value for value in self.dic.values()]
        return self.lis

    def matinent_select(self):
        self.com1_select=''
        self.com2_select=''


# l=lange_select()








