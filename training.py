class Body():
    def __init__(self, content):
        self.content = content


practics= {
    'left_angle_bracket' : '<',
    'right_angle_bracket' : '>',
    'tag_name' : '',
    'close_tag_slash': '/',
    'children_elements': []
}

animal = '표범'
content = '고양이과'

result = practics['left_angle_bracket'] + animal + practics['right_angle_bracket'] \
+ content \
+ practics['left_angle_bracket'] + practics['close_tag_slash'] + animal + practics['right_angle_bracket'] 

a = Body('치타')
print(result)