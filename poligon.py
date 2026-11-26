import math
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,new_width):
        self.width=new_width
    def set_height(self,new_height):
        self.height=new_height

    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return math.sqrt((self.width*self.width)+(self.height*self.height)) 
    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        else:    
            result=''
            for i in range(self.height):
                for j in range(self.width):
                    result+='*'              
                result+='\n'
            return result
    def get_amount_inside(self,shape):
        
        n=(self.width//shape.width)*(self.height//shape.height)
        return n
          

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'    

class Square(Rectangle):
    def __init__(self,length):
        self.height=length
        self.width=length
    def set_width(self,new_width):
        self.width=new_width
        self.height=new_width
    def set_height(self,new_height):
        self.height=new_height 
        self.width=new_height
    def set_side(self,new_side):
        self.width=new_side
        self.height=new_side
    def __str__(self):
        return f'Square(side={self.height})'       


