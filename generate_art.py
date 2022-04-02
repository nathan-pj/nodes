import random

import os
from PIL import Image, ImageDraw

def generate_art():

    run_id =  (len([1 for x in list(os.scandir("./")) if x.is_file()])) +1


    print(f'Processing run_id: {run_id}.png')

    image = Image.new('RGB', (5000, 5000), "WHITE")
    width, height = image.size

    rectangle_width = 1
    rectangle_height = 1

    nodes = []


    number_of_squares = (30)

    draw_nodes = ImageDraw.Draw(image)
    for i in range(number_of_squares):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)
        nodes.append([rectangle_x, rectangle_y])
        
        rectangle_shape = [
            (rectangle_x, rectangle_y),
            (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
        draw_nodes.rounded_rectangle(
            rectangle_shape,
            radius=(50),
            fill=(
                0,0,0
            )
        )
        


    draw_lines = ImageDraw.Draw(image)
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            coords = [nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1]]
            draw_lines.line([(coords[0],coords[1]),(coords[2], coords[3])], "BLACK", joint=("curve"))
            j+=1
        i+=1



    image.save(f'./{run_id}.png')


if __name__ == "__main__":
    generate_art()

