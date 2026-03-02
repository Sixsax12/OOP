class Resource:
    def __init__(self,name,author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    def display_info(self):
        pass
class EBook(Resource):
    def __init__(self,name, author,page_count):
        super().__init__(name, author)
        self.__page_count = page_count
    
    def display_info(self):
        return f"Reading {self.name} ({self.__page_count} pages)"

class Audiobook(Resource):
    def __init__(self,name, author,duration_mins):
        super().__init__(name, author)
        self.__duration_mins = duration_mins
    
    def display_info(self):
        return f"Listening to {self.name} ({self.__duration_mins} mins)"

class LibraryList:
    def __init__(self):
        self.__resources = []
    
    def add_resource(self,item):
        self.__resources.append(item)

    def show_all(self):
        for resource in self.__resources:
            print(resource.display_info())

class Author:
    def __init__(self,author_name):
        self.__author_name = author_name
        self.__resource_list = []

    @property
    def author_name(self):
        return self.__author_name
    
    @property
    def resource_list(self):
        return self.__resource_list
    
    def add_resource(self,ebook):
        self.__resource_list.append(ebook)
    

class LibraryManager:
    def __init__(self):
        self.__author_list = []
        self.__resource_list = []

    def search_by_author(self,author_name):
        for author in self.__author_list:
            if author.author_name == author_name:
                print(f"--- Resources by {author_name} ---")
                for res in author.resource_list:
                    print(res.display_info())

    def play_resource(self,title, author_name):
        for author in self.__author_list:
            if author.author_name == author_name:
                for resource in author.resource_list:
                    if resource.name == title:
                        print(resource.display_info())
                        return

    def add_author(self, author):
        self.__author_list.append(author)



# --- เริ่มส่วนการทดสอบ ---

# 1. สร้างตัวจัดการระบบ (Library Manager)
my_library = LibraryManager()

# 2. สร้างข้อมูลผู้แต่ง (Author)
author_jk = Author("J.K. Rowling")
author_king = Author("Stephen King")

# 3. สร้างหนังสือ (EBook) และ หนังสือเสียง (Audiobook)
# สังเกตว่าเราส่งชื่อ และชื่อผู้แต่ง (จาก property ของ Author) เข้าไป
book1 = EBook("Harry Potter 1", author_jk.author_name, 309)
book2 = Audiobook("Harry Potter 2 (Audio)", author_jk.author_name, 540)
book3 = EBook("The Shining", author_king.author_name, 447)

# 4. เพิ่มทรัพยากรลงในรายชื่อผลงานของผู้แต่ง
author_jk.add_resource(book1)
author_jk.add_resource(book2)
author_king.add_resource(book3)

# 5. เพิ่มผู้แต่งลงในระบบ Library Manager
my_library.add_author(author_jk)
my_library.add_author(author_king)

# --- ทดสอบการใช้งานฟังก์ชันต่างๆ ---

print("=== Test Case 1: Search by Author ===")
my_library.search_by_author("J.K. Rowling")
print("\n")

print("=== Test Case 2: Play Specific Resource (EBook) ===")
my_library.play_resource("The Shining", "Stephen King")
print("\n")

print("=== Test Case 3: Play Specific Resource (Audiobook) ===")
my_library.play_resource("Harry Potter 2 (Audio)", "J.K. Rowling")
print("\n")

print("=== Test Case 4: Search for non-existing resource (Should do nothing) ===")
my_library.play_resource("Minecraft Guide", "J.K. Rowling")

# --- ทดสอบ LibraryList (Optional) ---
print("\n=== Test Case 5: LibraryList (Personal Playlist) ===")
my_fav = LibraryList()
my_fav.add_resource(book1)
my_fav.add_resource(book3)
my_fav.show_all()