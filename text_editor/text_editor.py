import stackDeque


class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = stackDeque.Stack()
        self.redo_stack = stackDeque.Stack()


    def typing(self, value):
        if self.undo_stack.isEmpty():
            self.undo_stack.push("")
        self.text += " " + value
        self.undo_stack.push(self.text)
        self.displayText()



    def undo(self):
        # if self.undo_stack.isEmpty:
        #     self.redo_stack.clear_stack()
        self.redo_stack.push(self.undo_stack.pop())
        self.text = self.undo_stack.top()
        self.displayText()


    def redo(self):
        self.text = self.redo_stack.top()
        self.displayText()
        self.undo_stack.push(self.redo_stack.pop())

        
    def displayText(self):
        print(self.text)

myTexteditor = TextEditor()

myTexteditor.typing("Barev")
myTexteditor.typing("dzez")
myTexteditor.typing("inchpes eq")
myTexteditor.typing("inch eq anum")


print('\n')
print('\n')



myTexteditor.undo()
myTexteditor.undo()
myTexteditor.undo()
myTexteditor.undo()

# myTexteditor.undo()



print('\n')
print('\n')


myTexteditor.redo()
myTexteditor.redo()
myTexteditor.redo()
myTexteditor.redo()













