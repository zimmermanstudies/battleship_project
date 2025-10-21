# establishes ships and corresponding length
def get_available_ships():
    return {
        "Destroyer": 2,
        "Submarine": 3,
        "Cruiser": 3,
        "Battleship": 4,
        "Carrier": 5
    }

# initial empty grid (TO BE CHANGED FOR OFFICIAL INTERFACE)
def create_empty_grid():
    return [["≈" for _ in range(11)] for _ in range(11)]

# defines how our coordinates function
def coord_to_index(coord):
    letters = "ABCDEFGHIJK"
    row = letters.index(coord[0].upper())
    col = int(coord[1:]) - 1
    return row, col # sections off two parts of coordinate

# Boolean verifies placement is valid
def place_ship(grid, coord, direction, length):
    row, col = coord_to_index(coord)
    max_index = len(grid) - 1

    # Check if placement is valid and doesn't overlap
    if direction == "up":
        if row - length + 1 < 0:
            print("\nNot enough space upward from that position.")
            return False
    elif direction == "down":
        if row + length - 1 > max_index:
            print("\nNot enough space downward from that position.")
            return False
    elif direction == "left":
        if col - length + 1 < 0:
            print("\nNot enough space to the left from that position.")
            return False
    elif direction == "right":
        if col + length - 1 > max_index:
            print("\nNot enough space to the right from that position.")
            return False
    else:
        print("\nInvalid direction. Choose up, down, left, or right.")
        return False

    # Check for overlap
    # Consider changing variables from letters??
    for i in range(length): # i = each section of the ship through it's length
        r, c = row, col
        if direction == "up":
            r -= i
        elif direction == "down":
            r += i
        elif direction == "left":
            c -= i
        elif direction == "right":
            c += i

        if grid[r][c] != "≈": # Will replace ≈ with whatever 
                                  # symbolizes open space
            print("\nOverlap detected — there's already a ship at that location.\n")
            return False 

    # Place the ship
    for i in range(length):
        r, c = row, col
        if direction == "up":
            r -= i
        elif direction == "down":
            r += i
        elif direction == "left":
            c -= i
        elif direction == "right":
            c += i

        grid[r][c] = "S" # Will replace with whatever symbolizes
                         # occupying ship

    return True # If all verification passes, clear to place!
    
# Scaffolding for updating menu after every choice
def print_ship_menu(ships):
    print("+------------+--------+")
    print("| Ship Name  | Length |")
    print("+------------+--------+")
    for i, (name, length) in enumerate(ships.items(), start=1):
        print(f"| {name.ljust(10)} | {str(length).center(6)} |")
    print("+------------+--------+")

# Prompts user to choose a ship
def get_ship_choice(ships):
    while True:
        ship_name = input("Choose a ship to place by name: ").strip().title()
        if ship_name in ships:
            return ship_name
        print("\nInvalid ship name. Try again.\n")

# Prompts user to choose a coordinate
def get_placement_details(ship_name):
    coord = input(f"Enter starting coordinate for {ship_name} (e.g., B5): ").strip().upper()
    # Prompts user for direction of ship FROM coordinate
    direction = input("Enter direction (up, down, left, right): ").strip().lower()
    return coord, direction


def run_ship_placement():
    # Simplifies our known information
    ships = get_available_ships()
    grid = create_empty_grid()

    print_grid(grid)
    # Loops updating menu and user choices
    while ships:
        print_ship_menu(ships)
        ship = get_ship_choice(ships)
        coord, direction = get_placement_details(ship)

        # Continues verifying as we receive prompts
        success = place_ship(grid, coord, direction, ships[ship])
        if success:
            del ships[ship]
            print(f"{ship} placed.")
            print_grid(grid)
        else:
            print("\nInvalid placement. Try again.\n")

    return grid

# Enters info into updated grid
def print_grid(grid):
    letters = "ABCDEFGHIJK"
    
    # Print column headers
    print(" " + " ".join([str(i).rjust(3) for i in range(1, 12)]))
    
    # Print each row (consider changing i variable)
    for i, row in enumerate(grid):
        row_label = letters[i]
        row_content = []
        for cell in row:
            row_content.append(cell.center(3))  
        print(row_label + " " + " ".join(row_content))

# Final output after all ships chosen, all choices made       
player_grid = run_ship_placement()
print("Final player grid:")
print_grid(player_grid)
