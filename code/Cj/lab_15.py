import requests

class search_engine():
    def __init__(self):
        self.page = 1
        self.header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        self.error = 'Error! Please make a valid entry: '
        self.prev_flag = False
        self.error_flag = False
        self.new_flag = False
        self.menu = '''
            Enter "next" to display next page.
            Enter "prev" to display previous page.
            Enter "quit" to exit.
            Enter "new" to start a new search.
            
            Enter: '''
    def search(self):
        return_list = ''
        counter = 1
        if self.page == 1 and self.prev_flag == False or self.new_flag == True:
            self.key = input('Enter a keyword to search for: ')
        self.url = f'https://favqs.com/api/quotes?page={self.page}&filter={self.key}'
        self.response = requests.get(self.url, headers = self.header).json()
        self.result_count = len(self.response['quotes'])
        return_list += f'Results for keyword: {self.key}  Page: {self.page} '
        return_list += '\n'
        for i in self.response['quotes']:
            return_list += str(counter) + '. ' +  i['body']
            return_list += '\n'
            return_list += '- ' + i["author"]
            return_list += '\n'
            counter += 1
        print(return_list.strip())

    def error_clear(self):
        self.menu = '''
        Enter "next" to display next page.
        Enter "prev" to display previous page.
        Enter "quit" to exit.
        Enter "new" to start a new search.
        
        Enter: '''

    def navigation(self):
        while True:
            if self.new_flag != True:
                menu_nav = input(f'{self.menu}')
            if self.error_flag == True:
                self.error_clear()
                self.error_flag == False
            if menu_nav == 'prev':
                if self.page == 1:
                    self.menu = self.menu.replace('Enter', 'No previous page: ')
                    self.error_flag = True
                else:
                    self.page -= 1
                    self.prev_flag = True
                    self.search()
            elif menu_nav == 'next':
                if self.response['last_page'] == True:
                    self.menu = self.menu.replace('Enter', 'Last page: ')
                    self.error_flag = True
                else:
                    self.page += 1
                    self.search()
            elif menu_nav == 'quit':
                exit()
            elif menu_nav == 'new':
                self.new_flag = True
                result = self.search()
                print(result)
            else:
                self.menu = self.menu.replace('Enter', self.error)
            #self.search()
engine = search_engine()
engine.search()
engine.navigation()

        # return_list = ''
        # counter = 1
        # self.key = input('Enter a keyword to search for: ')
        # self.url = f'https://favqs.com/api/quotes?page={self.page}&filter={self.key}'
        # self.response = requests.get(self.url, headers = self.header).json()
        # self.result_count = len(self.response['quotes'])
        # return_list += f'Results for keyword: {self.key}  Page: {self.page} '
        # return_list += '\n'
        # for i in self.response['quotes']:
        #     return_list += str(counter) + '. ' +  i['body']
        #     return_list += '\n'
        #     return_list += '- ' + i["author"]
        #     return_list += '\n'
        #     counter += 1
        # return return_list


# turn = input('Enter "next" to display the next page: ')

# print(search_engine.search())



    

