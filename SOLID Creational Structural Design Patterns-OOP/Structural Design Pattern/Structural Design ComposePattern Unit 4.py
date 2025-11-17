""" please write a code to do the following task:
The Composite Pattern allows you to compose objects into hierarchical structures (tree of objects).
 Both File and Folder implement the same interface (FileSystemComponent).
 Think of a scenario where you might use the Composite Pattern, such as managing a file system with files and folders.
Scenario: Managing a file system where files and folders can be treated uniformly.
Explain how the Composite Pattern would solve the problem."""
from abc import ABC, abstractmethod
#Step 1: Define an interface for file system components.
class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_size(self):
        pass
    @abstractmethod
    def get_child_count(self):
        pass
#Step 2: Create classes for files and folders that implement the interface.
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    #File has no children, so always should return 0
    def get_child_count(self):
        return 0
#Step 3: Create a Folder class that can contain other FileSystemComponents (both Files and Folders).
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []
    def get_name(self):
        return self.name
    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    def get_child_count(self):
        return len(self.children)
    def add_child(self, child):
        self.children.append(child)
#Demonstrate how to use the composite structure with an example.
if __name__ == "__main__":
    #create instances of files and folders
    doc_file = File("doc.txt", 100)
    image_file= File("image.png", 500)
    doc_folder = Folder("Documents")
    music_folder = Folder("Music")
    #Add files and folders
    music_folder.add_child(doc_file)
    doc_folder.add_child(image_file)
    doc_folder.add_child(music_folder)
    #Demo composite structure
    print(doc_folder.get_name())  # Output: Documents
    print(doc_folder.get_size())  # Output: 600
    print(doc_folder.get_child_count())  # Output: 2
    print(doc_file.get_child_count()) #output: 0

    for child in doc_folder.children:
        print(child.get_name(), child.get_size())

    # Output:
    # image.png 500
    # Music 100



