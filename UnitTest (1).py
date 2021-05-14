import Login
import search
import NetflixTitles
import unittest
import sys
class TestLogin(unittest.TestCase):
    #test the function set_username
    def test_set_username_Empty(self):
        test = Login.User()   
        self.username = " "
        test.set_username(self.username)
        self.assertEqual(test.get_username(), self.username)
    def test_set_username_String(self):
        test = Login.User()
        self.username = "Russell"
        test.set_username(self.username)
        self.assertEqual(test.get_username(), self.username)
    '''def test_set_username_Integer(self):
        test = Login.User()
        self.username = 123
        test.set_username(self.username)
        self.assertIsInstance(test.get_username(), int)'''
    #test the function set_password
    def test_set_password_Empty(self):
        test = Login.User()   
        self.password = " "
        test.set_password(self.password)
        self.assertEqual(test.get_password(), self.password)
    def test_set_password_String(self):
        test = Login.User()
        self.password = "Russell"
        test.set_password(self.password)
        self.assertEqual(test.get_password(), self.password)

class TestSearch(unittest.TestCase):

    def test_set_search_Empty(self):   
        test = search.Film()   
        self.search = " "
        test.set_search(self.search)
        self.assertEqual(test.get_search(), self.search)
    def test_set_search_String(self):   
        test = search.Film()   
        self.search = "365 Days"
        test.set_search(self.search)
        self.assertEqual(test.get_search(), self.search)
    # def test_searchByTitle(self):

    #     with sqlite3.connect("movies.db") as db:
    #         cur = db.cursor()
    #     cur.execute("SELECT * FROM Movies WHERE Title LIKE '%{0}%' UNION SELECT * FROM Series WHERE Title LIKE '%{0}%'".format(self.search))
    #     results = cur.fetchall()



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule( sys.modules[__name__] ) 
    unittest.TextTestRunner(verbosity=3).run( suite )
