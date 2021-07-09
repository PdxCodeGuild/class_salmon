import math
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import datetime
import csv

def isfloat(x):
    try:
        x = float(x)
        return True
    except:
        return False

#-------------------------------------------------------------------#
# difference = desired_parameter_level - current_parameter_level
# doseage = difference / conversion_dict['alk']['DKH']                  ## Krabby patty secret formula.
# doseage *= total_water_volume
# ------------------------------------------------------------------#

class calculator():
    def __init__(self):
        self.ideal_parameters = {'alk': 9.0,
    'cal': 380,
    'mag': 1250}
        self.conversion_dict = {
    'cal': {'ml': 1, 'gal': 1, 'ppm': 16},
    'alk': {'ml': 1, 'gal': 1, 'DKH': 2.07},
    'mag': {'ml': 1, 'gal': 1, 'ppm': 6}}

        self.error = 'Error! Please make a valid selection: '

    def calculate(self, menu_select):
            if menu_select == 1:
                x = 'alk'
                y = 'DKH'
            elif menu_select == 2:
                x= 'cal'
                y = 'ppm'
            elif menu_select == 3:
                x = 'mag'
                y = 'ppm'
            current_parameter_level = float(input(f'Enter the current {y}: '))
            desired_parameter_level = float(input(f'Enter desired {y}: '))
            total_water_volume = float(input('Enter the total water volume: '))
            difference = desired_parameter_level - current_parameter_level
            doseage = difference / self.conversion_dict[x][y]                  ## Krabby patty secret formula.
            doseage *= total_water_volume
            print(f'In order to raise your current {x} by {difference} you would need to dose {round(doseage)} ml of {x} addative formula.')

class Menu():
    def __init__(self):
        self.main = '''
        Please make a selection from the following menu:

        1. Use Calculator 
        
        2. Create Parameter log

        3. Retrieve Parameter log

        4. Update Parameter log

        5. Delete Parameter log

        6. Help
        
        7. Quit

        Enter: '''

        self.plot_ = '''
        User data found!

        1. Display alkalinity graph.
        
        2. Display calcium graph.
        
        3. Display magnesium graph.
        
        4. Return to main menu.
         
        5. Exit.


        Enter: '''
        
        self.parameter_select = '''
        Which parameter would you like to calculate?

        1. Alkalinity

        2. Calcium

        3. Magneseium

        4. Back to main menu

        5. Quit

        Enter: '''

        self.help = '''
        To use the reef calculator start by entering the parameter you want to calculate.
        You will then be promted to enter the current DKH or ppm value of the parameter.
        The next piece of information you will be asked for is the desired DKH or ppm of the parameter.
        Finally you will be aske to enter the total water volume of your aquarium system in gallons.
        The calculator will then do the rest of the work for you and calculate how many ML of a given addative to dose to your aquarium.
        '''

        self.welcome_msg = '''
        Hello, and welcome to my saltwater reef aquarium water parameter calculator and consumption log.

        This calculator uses a ml to gallons ratio to determine how many ml of a given addative to dose into your reef tank.
        
        This calculator is only intended to calculate INCREASES in the water parameters of your marine aquarium system ONLY!

        To reduce parameters that are too high, dilute the concentration in your system using water changes. 
        '''

        self.err = 'Error! Please make a valid selection: '
        
        self.nav = '0'

        self.retrieved_data = []
        self.alk = []
        self.cal =[]
        self.mag = []
        self.dates = []

    def valid(self, menu):
        self.nav = str(self.nav)
        if self.nav.isnumeric():
            self.nav = int(self.nav)
        else:
            return False
        if menu == self.plot_:
            if self.nav < 1 or self.nav > 5:
                return False
            else:
                return self.nav
        elif menu == self.main:
            if self.nav < 1 or self.nav > 7:
                return False
            else:
                return self.nav
        elif menu == self.parameter_select:
            if self.nav < 1 or self.nav > 5:
                return False
            else:
                return self.nav

    def error(self):
        self.main = self.main.replace('Enter: ', self.err)
        self.plot_ = self.plot_.replace('Enter: ', self.err)
        self.parameter_select = self.parameter_select.replace('Enter: ', self.err)

    def main_(self):
        self.nav = '0'
        while not self.valid(self.main):
            self.nav = input(f'{self.main}')
            if not self.valid(self.main):
                self.error()
        return self.nav
    
    def plot_menu(self):
        self.nav = '0'
        while not self.valid(self.plot_):
            self.nav = input(f'{self.plot_}')
            if not self.valid(self.plot_):
                self.error()
        return self.nav
    
    def parameter_select_(self):
        self.nav ='0'
        while not self.valid(self.parameter_select):
            self.nav = input(f'{self.parameter_select}')
            if not self.valid(self.parameter_select):
                self.error()
        return self.nav
    
    def create(self):
        date = datetime.date.today()
        alk = input('Enter current alkalinity levels in DKH: ')
        cal = input('Enter current calcium levels in ppm: ')
        mag = input('Enter current magnesium levels in ppm: ')

        val = {'Date': date, 'alk': alk, 'cal': cal, 'mag': mag}
        UI = input('Enter your name: ')
        output = ''
        for v in val.values():
            output += str(v) + ','
        output = output[:-1]
        with open(f'c:\\Users\\Cj\\Documents\\PDX_CODE_GUILD_BOOT_CAMP\\class_salmon\\code\\Cj\\{UI}\'s_reef_log.csv', 'w' ) as file:
            file.write(output)
        print('Profile created!')

    def retrieve(self):
        UI = input('Enter your name: ')
        with open(f'{UI}\'s_reef_log.csv', 'r') as file:
            file = file.readlines()
            self.retrieved_data = []
            for line in file:
                data = line.split(',')
                data[-1] = data[-1].strip() 
                date = data[0]
                alk = data[1]
                cal = data[2]
                mag = data[3]
                value = {'Test date': date, 'alk': alk, 'cal': cal, 'mag': mag}
                self.retrieved_data.append(value)
            for dict in self.retrieved_data:
                self.alk.append(float(dict['alk']))
                self.dates.append(dict['Test date'])
                self.cal.append(dict['cal'])
                self.mag.append(dict['mag'])
      
    def update(self):
        UI = input('Enter your name: ')
        date = datetime.date.today()
        alk = input('Enter current alkalinity levels in DKH: ')
        cal = input('Enter current calcium levels in ppm: ')
        mag = input('Enter current magnesium levels in ppm: ')
        val = {'Date': date, 'alk': alk, 'cal': cal, 'mag': mag}
        output = ''
        for v in val.values():
            output += str(v) + ','
        output = output[:-1]
        with open(f'{UI}\'s_reef_log.csv', 'a') as file:
            file.write('\n' + output)
    
    # def delete(self):
    #     UI = input('Enter name of profile to delete: ')

    def plot_alk(self):
        plt.style.use('seaborn')
        plt.plot_date(self.dates, self.alk, linestyle = 'solid')
        plt.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.show()

    def plot_cal(self):
        plt.style.use('seaborn')
        plt.plot_date(self.dates, self.cal, linestyle = 'solid')
        plt.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.show()

    def plot_mag(self):
        plt.style.use('seaborn')
        plt.plot_date(self.dates, self.mag, linestyle = 'solid')
        plt.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.show()

def run_program():
    menu = Menu()
    while True:
        print(menu.welcome_msg)
        menu_select = menu.main_()
        if menu_select == 1:
            calc = calculator()
            menu_select = menu.parameter_select_()
            if menu_select >= 1 and menu_select <= 3:
                calc.calculate(menu_select)
                continue
            elif menu_select == 4:
                continue
            elif menu_select == 5:
                exit()
        elif menu_select == 2:
            menu.create()
            continue
        elif menu_select == 3:
            menu.retrieve()
            menu_select = menu.plot_menu()
            if menu_select == 1:
                menu.plot_alk()
            elif menu_select == 2:
                menu.plot_cal()
            elif menu_select == 3:
                menu.plot_mag()
            elif menu_select == 4:
                continue
            elif menu_select == 5:
                exit()
        elif menu_select == 4:
            menu.update()
        elif menu_select == 5:
            pass
            # menu.delete()
        elif menu_select == 6:
            print(menu.help)
        elif menu_select == 7:
            exit()

run_program()