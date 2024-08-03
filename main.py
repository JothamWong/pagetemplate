import argparse
from PIL import Image, ImageDraw

COLOURS = {
    "black": (0,0,0),
    "light_black": (64,64,64),
    "blue": (0,0,255),
    "white": (255,255,255),
}

def create_template(width, height, margin, line_spacing, line_color, background_color):
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    # Left margin
    draw.line([(margin, 0), (margin, height)], fill=line_color)
    # Horizontal lines
    for y in range(0, height, line_spacing):
        draw.line([(0, y), (width, y)], fill=line_color)
    
    return image


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--width", type=int, default=1000, help="Width of page")
    args.add_argument("--height", type=int, default=1414, help="Height of page")
    args.add_argument("--margin", type=int, default=100, help="Left margin loc")
    args.add_argument("--ls", type=int, default=50, help="Line spacing")
    args.add_argument("--lc", choices=COLOURS.keys(), default="blue", help="Line color")
    args.add_argument("--bc", choices=COLOURS.keys(), default="white",help="Background color")
    args.add_argument("--to", type=str, default="template.jpg", help="Filename")
    opts = args.parse_args()
    
    template = create_template(
        opts.width,
        opts.height,
        opts.margin,
        opts.ls,
        COLOURS[opts.lc],
        COLOURS[opts.bc],
    )
    
    template.save(opts.to, 'JPEG')
    