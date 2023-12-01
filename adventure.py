import sys
import json

class Game:
    def __init__(self, map_filename):
        self.load_map(map_filename)
        self.current_room = 0
        self.inventory = []
        self.display_room()

    def load_map(self, map_filename):
        try:
            with open(map_filename, 'r') as file:
                self.map = json.load(file)
        except FileNotFoundError:
            print(f"Error: Map file '{map_filename}' not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in map file '{map_filename}'.")
            sys.exit(1)

    def display_room(self):
        room_info = self.map[self.current_room]
        print(f"> {room_info['name']}\n\n{room_info['desc']}\n")

        if 'items' in room_info:
            print(f"Items: {', '.join(room_info['items'])}")

        print(f"Exits: {', '.join(room_info['exits'])}\n")

    def go(self, direction):
        if not direction:
            print("Error: You need to enter a direction.")
            return

        room_info = self.map[self.current_room]
        matching_exits = [exit for exit in room_info['exits'] if exit.startswith(direction)]
        if len(matching_exits) == 1:
            self.current_room = room_info['exits'][matching_exits[0]]
            self.display_room()
        elif len(matching_exits) > 1:
            print(f"Error: Did you want to go {', '.join(matching_exits)}?")
        else:
            print(f"Error: There's no way to go {direction}.")

    def look(self):
        self.display_room()

    def get(self, item):
        if not item:
            print("Error: You need to enter an item.")
            return

        room_info = self.map[self.current_room]
        matching_items = [i for i in room_info.get('items', []) if i.startswith(item)]
        if len(matching_items) == 1:
            self.inventory.append(matching_items[0])
            room_info['items'].remove(matching_items[0])
            print(f"You pick up the {matching_items[0]}.")
        elif len(matching_items) > 1:
            print(f"Error: Did you want to get {', '.join(matching_items)}?")
        else:
            print(f"Error: There's no {item} anywhere.")

    def drop(self, item):
        if not item:
            print("Error: You need to enter an item.")
            return

        if item in self.inventory:
            self.inventory.remove(item)
            self.map[self.current_room].setdefault('items', []).append(item)
            print(f"You drop the {item}.")
        else:
            print(f"Error: You don't have {item} in your inventory.")

    def inventory_command(self):
        if not self.inventory:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"  {item}")

    def help_command(self):
        print("You can run the following commands:")
        print("  go ...")
        print("  get ...")
        print("  look")
        print("  inventory")
        print("  drop ...")
        print("  quit")
        print("  help")

    def quit(self):
        print("Goodbye!")
        sys.exit(0)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    game = Game(sys.argv[1])

    while True:
        user_input = input("What would you like to do? ").strip().lower().split()
        if not user_input:
            print("Error: You need to enter a command.")
            continue

        verb = user_input[0]
        if verb == 'go':
            game.go(user_input[1] if len(user_input) > 1 else None)
        elif verb == 'look':
            game.look()
        elif verb == 'get':
            game.get(user_input[1] if len(user_input) > 1 else None)
        elif verb == 'drop':
            game.drop(user_input[1] if len(user_input) > 1 else None)
        elif verb == 'inventory' or verb == 'inv':
            game.inventory_command()
        elif verb == 'help':
            game.help_command()
        elif verb == 'quit':
            game.quit()
        else:
            print(f"Error: Unknown command - {verb}")

if __name__ == "__main__":
    main()
