import pandas

class username_and_passwords():
    def __init__(self):
        self.users = pandas.read_csv('users.csv')
        print(self.users)


    def check_login(self, user,password):
        user_confirm = self.check_username(user)
        # the username does not exist, return back with False
        if user_confirm == None:
            return False
        pass_confirm =self.check_password(password, user_confirm)
        # the username was ok but the password is wrong
        if pass_confirm == None:
            return False

        return True
    def check_username(self, name):
        try:
            # get the index from the dataframe
            username_index = self.users['user'][self.users['user'] == name].index[0]
            return username_index
        except IndexError:
            # the index does not exist
            return None
    def check_password(self, password,index):
        pass_should_be = self.users['password'][index]
        # the password is ok
        if password == pass_should_be:
            return True
        # the password is not ok
        else:
            return None
    def create_new_user(self, user,password):
        # mel_count = a['Names'].str.contains('Mel').sum()
        count = self.users['user'].str.contains(user).sum()
        if count > 0:
            print('user already exists')
            return False

        max_index = self.users.index.max()

        # create new user dataframe to concat
        new_user = pandas.DataFrame({'user':user, 'password':password}, index=[max_index+1])
        frames = [self.users, new_user]
        # concat dataframes and write to file
        result = pandas.concat(frames)
        result.to_csv('users.csv', encoding='utf-8', index=False)
        print(result)
if __name__ == '__main__':
    usr = username_and_passwords()
    usr.create_new_user('allen', 'hash999')
    # ret = usr.check_login('john', 'hash2')
    # print('ret value is %s' % ret)

