import sqlite3 
class Film:
    def __init__(self):
        self.search = " "
        self.result = " "
    def get_search(self):
        return self.search
    def set_search(self, search):
        self.search = search
    
    def searchByTitle(self):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE Title LIKE '%{0}%' UNION SELECT * FROM Series WHERE Title LIKE '%{0}%'".format(self.search))
        results = cur.fetchall()
        if results:
            return True
        else:
            return False
    def searchByGenre(self):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE Genre LIKE '%{0}%' UNION SELECT * FROM Series WHERE Genre LIKE '%{0}%'".format(self.search))
        results = cur.fetchall()
        if results:
            return True
        else:
            return False
    def searchByYear(self):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE ReleaseYear = '{0}' UNION SELECT * FROM Series WHERE ReleaseYear = '{0}'".format(self.search))
        results = cur.fetchall()
        if results:
            return True
        else:
            return False
    def searchInDatabase(self):
        if self.searchByYear():
            return True
        elif self.searchByTitle():
            return True
        
        elif self.searchByGenre():
            return True
            
        else:
            return False
    def searchTitle(self,title):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE Title LIKE '%{0}%' UNION SELECT * FROM Series WHERE Title LIKE '%{0}%'".format(title))
        return cur.fetchall()
    def searchGenre(self):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE Genre LIKE '%{0}%' UNION SELECT * FROM Series WHERE Genre LIKE '%{0}%'".format(self.search))
        return cur.fetchall()
    def searchYear(self):
        with sqlite3.connect("movies.db") as db:
            cur = db.cursor()
        cur.execute("SELECT * FROM Movies WHERE ReleaseYear = '{0}' UNION SELECT * FROM Series WHERE ReleaseYear = '{0}'".format(self.search))
        return cur.fetchall()
#pang test ng functions lang
    def Print(self):
        if self.searchByYear():
            message = self.formatResultYear(self.search)
        elif self.searchByTitle():
            message = self.formatResultTitle(self.search)
        
        elif self.searchByGenre():
            message = self.formatResultGenre(self.search)
            
        else:
            message = "Not Found"
        #print(message)
        return message
            
    def autoNextLine(self, string, wordsPerLine):
        string = string.split(" ")
        #string = string.split(" ")
        stringSliced = ""
        i = 0
        while i < len(string):
            if (i % wordsPerLine == 0 and i != 0):
                stringSliced += "\n"
            stringSliced += string[i] + " "
            i += 1
        return stringSliced
    def formatResultGenre(self, genre):
        results = self.searchGenre()
        resultCount = len(results)
        formattedOutput = ""
        if(resultCount > 0):
            for result in results:
                formattedOutput += "Title: {}".format(result[1]) + " | " 
                formattedOutput += "Duration: {}".format(result[8]) + " | "
                formattedOutput += "Genre: {}".format(result[9]) + "\n"
        elif(resultCount == 0):
            formattedOutput += "NA"
        return formattedOutput 
    def formatResultYear(self, year):
        results = self.searchYear()
        resultCount = len(results)
        formattedOutput = ""
        if(resultCount > 0):
            for result in results:
                formattedOutput += "Title: {}".format(result[1]) + " | " 
                formattedOutput += "Duration: {}".format(result[8]) + " | "
                formattedOutput += "Release Year: {}".format(result[4]) + "\n"
        elif(resultCount == 0):
            formattedOutput += "NA"
        return formattedOutput 
    def formatResultTitle(self, title):
        results = self.searchTitle(title)
        resultCount = len(results)
        formattedOutput = ""
        if(resultCount > 0):
            for result in results:
                formattedOutput += "Title: {}".format(result[1]) + "\n"
                formattedOutput += "Description: {}".format(self.autoNextLine(result[2], 15)) + "\n"
                formattedOutput += "Rating: {}".format(result[3]) + "\n"
                formattedOutput += "Release Year: {}".format(result[4]) + "\n"
                formattedOutput += "Directors: {}".format(result[5]) + "\n"
                formattedOutput += "Cast: {}".format(result[6]) + "\n"
                formattedOutput += "Country: {}".format(result[7]) + "\n"
                formattedOutput += "Duration: {}".format(result[8]) + "\n"
                formattedOutput += "Genre: {}".format(result[9]) + "\n\n"
        elif(resultCount == 0):
            formattedOutput += "NA"
        return formattedOutput 
def main():
    trial = Film()
    
    trial.set_search("Drama")
    trial.Print()
    
#if __name__ == '__main__':
#    main() 