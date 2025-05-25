from PIL import Image, ImageDraw


def generate_rectangle(width, height, color, output_path, outline=False):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color="#2D8BBF")
    
    # Create a drawing context
    draw = ImageDraw.Draw(img)
    
    if not outline:
        output_path += filled_rectangle_name
        # Draw filled rectangle
        draw.rectangle([(0, 0), (width-1, height-1)], fill=color)
    else:
        output_path += outlined_rectangle_name
        draw.rectangle([(0, 0), (width-1, height-1)], outline=color, fill=False)

    # Save the image
    img.save(output_path)


rectangle_path = "/home/matous/Downloads/Conky/Shapes/"
filled_rectangle_name = "filled_rectangle.png"
outlined_rectangle_name = "outline_rectangle.png"

width = 10
height = 20
color = "#2D8BBF"  # Bright blue color
generate_rectangle(width, height, color, rectangle_path)
generate_rectangle(width, height, color, rectangle_path, True)
