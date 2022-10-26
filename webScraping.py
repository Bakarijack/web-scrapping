from bs4 import BeautifulSoup

with open("world.html", "r") as myfile:
    content = myfile.read()
    #print(content)
     
    #creating the instance of the BeautifulSoup 
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #grabbing specific content
    tags = soup.find_all("title")
    #print(tags)

    #for element in tags:
       # print(element.text)
    
    books = soup.find_all("div",class_="col-sm-6")

    for book in books:
        #print(book.h2)
        book_topics = book.a
        book_subtopic = book.small.text
        print("Under ",book_topics.text," they offer the following books : ")
        print(book_subtopic[2:-1])
        print()