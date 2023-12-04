# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file
import copy
import csv
import os


def read_csv_to_table(table_name, filename):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    data = []
    with open(os.path.join(__location__, filename)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            data.append(dict(r))
    return Table(table_name, data)

# add in code for a Database class


class DataBase:
    def __init__(self):
        self.database = []
    # table is class table

    def insert(self, table):
        self.database.append(table)
    # name str table_name
    # self.database is array for store list of table

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    def delete(self, username):
        if username == "Cristiano.R":
            del self.database
        # check table login if user is admin role


# add in code for a Table class


class DataBaseBackup:
    def __init__(self):
        self.database_back_up = []

    def getdata(self):
        dict1 = copy.deepcopy(DataBase)
        self.database_back_up.append(dict1)
        return self.database_back_up

    def save_data(self):
        # self.database_back_up.append()
        pass


class Table:
    # table_name is str
    # table is array for data field is name of column ex. [{id = 1, name = A}, {id = 2, name = B}]
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def insert_entry(self, entry):
        self.table.append(entry)

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' +
                             other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def __is_float(self, element):
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
                elif len(attributes_list) == 0:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
