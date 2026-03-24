
class trianglePyramid:

    def traingle_pyramid(self, num:int)->None:
        for i in range(num+1):
            print(f'{' '*(num-i)}{'*'*i}{'*'*(i-1)}{' '*(num-i)}')

    def triangle_pyramid_v2(self, num:int)->None:
        for i in range(1,num+1):
            stars=2*i-1
            spaces=num-i
            print(f'{' '*spaces}{'*'*stars}{' '*spaces}')

    def traingle_pyramid_center(self, num: int) -> None:
        max_width = 2 * num - 1  # The widest row will have 2*num - 1 stars
        for i in range(1, num + 1):
            stars = 2 * i - 1
            print(('*' * stars).center(max_width))

tp=trianglePyramid()
# tp.traingle_pyramid(7)

class NumberPyramid:

    def number_pyramid_t1(self,num:int)->None:
        for i in range(1,num+1):
            numbers=2*i-1
            spaces=num-i
            print(f'{' '*spaces}{str(i)*numbers}{' '*spaces}')

    def number_pyramid_t2(self,num:int)->None:
        for i in range(1,num+1):
            spaces=num-i
            print(f'{' '*spaces}' ,end='')
            for j in range(1,i+1):
                print(j, end='')
                print(f'{' '}' ,end='')
            print()

    
np=NumberPyramid()
np.number_pyramid_t2(5)


