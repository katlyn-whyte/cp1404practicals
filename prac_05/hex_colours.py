COLOUR_CODES = {'AbsoluteZero': '#0048ba', 'BrightGreen': '#66ff00', 'CarminePink': '#ffa6c9',
                'CastletonGreen': '#00563f', 'Celeste': '#b2ffff', 'DarkLavendar': '#734f96',
                'DeepFunchsia': '#c54c1', 'Electriclime': '#ccff00', 'FloralWhite': '#fffaf0'}
colour_name = input("What is the colour you are looking for? ")
is_colour = False
while colour_name != "":
    while not is_colour:
        try:
            print(f"the code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
            is_colour = True
        except ValueError:
            print("invalid colour choice")
    colour_name = input("What is the colour you are looking for? ")


