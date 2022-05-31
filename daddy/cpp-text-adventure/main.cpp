#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <memory>

#include <fmt/format.h>

class Item
{
public:
    std::string id;
};



    // def command(self, command: str, room) -> bool:
    //     if command in ["i", "inv", "inventory"]:
    //         if self._items:
    //             print("You are carrying:")
    //             for k, v in self._items.items():
    //                 print(f"{k} {v}")
    //         else:
    //             print("Your pockets are empty!")
    //         print()

    //         return True

    //     if "drop" in command:
    //         item_name = command.split(" ")[-1]

    //         item = self.remove_item(item_name)
    //         if not item:
    //             print("Sorry, you don't seem to be carrying one of those!")
    //             return True

    //         print(f"You drop your {item_name}")

    //         room.add_item(item)

    //     return False

class Player
{
public:
    bool command(const std::string& text)
    {
        return false;
    }

    std::unique_ptr<Item> remove_item(const std::string& name)
    {
        const auto it = m_items.find(name);

        if (it != m_items.end())
        {
            auto item = std::move(it->second);
            m_items.erase(it);
            return item;
        }

        return {};
    }

    void add_item(std::unique_ptr<Item> item)
    {
        m_items[item->id] = std::move(item);
    }


private:
    std::map<std::string, std::unique_ptr<Item>> m_items = {};
};

class Location
{
public:
    virtual ~Location() = default;
    virtual void intro() = 0;
    virtual std::string command(const std::string& text, Player& player) = 0;
};

std::string get_command()
{
    fmt::print("What is your command?\n");
    fmt::print("# ");
    std::string input;
    std::getline(std::cin, input);
    std::transform(
        input.begin(), input.end(), input.begin(),
        [](auto c){ return std::tolower(c); }
    );
    return input;
}

std::string do_location(Player& player, Location& location)
{
    location.intro();

    const auto command = get_command();

    if (player.command(command))
    {
        return "";
    }

    const std::string new_location = location.command(command, player);

    if (!new_location.empty())
    {
        // fmt::print("I received new location {}\n", new_location);
    }
    else
    {
        fmt::print("I'm afraid that didn't seem to work!\n");
    }

    fmt::print("\n");

    return new_location;
}

namespace locations
{
    class Cheese : public Location
    {
    public:
        static constexpr const char* id = "cheese";
        void intro() override
        {
            fmt::print("You are in a room full of cheese!\n");
        }
        std::string command(const std::string& text, Player& player) override
        {
            if (text == "eat cheese")
            {
                return "haddock"; // TODO: Haddock::id;
            }

            return "";
        }
    };

    class Haddock : public Location
    {
    public:
        static constexpr const char* id = "haddock";
        void intro() override
        {
            fmt::print("You are in a room, featuring a pool containing a huge haddock.\n");
        }
        std::string command(const std::string& text, Player& player) override
        {
            if (text == "fish for haddock")
            {
                return "crossroads"; // TODO: CrossRoads::id
            }

            return "";
        }
    };

    class CrossRoads : public Location
    {
    public:
        static constexpr const char* id = "crossroads";
        void intro() override
        {
            fmt::print("You are at a crossroads.\n");
        }
        std::string command(const std::string& text, Player& player) override
        {
            if (text == "north")
                return "north";
            if (text == "south")
                return "south";
            if (text == "east")
                return "east";
            if (text == "west")
                return "west";
            if (text == "up")
                return "win";
            if (text == "down")
                return "die";
            return "";
        }
    };

    class DeadEnd : public Location
    {
    public:
        // static constexpr const char* id = "crossroads";
        DeadEnd(const std::string& exit)
            :
            m_exit(exit)
        {
        }
        void intro() override
        {
            fmt::print("You are at a dead end.\n");
            fmt::print("There is a single exit to the {}.\n", m_exit);
        }
        std::string command(const std::string& text, Player& player) override
        {
            if (text == m_exit)
                return "crossroads";
            return "";
        }
    private:
        const std::string m_exit;
    };

    class Win : public Location
    {
    public:
        static constexpr const char* id = "win";
        void intro() override
        {
            fmt::print("You win! Did you cheat?!\n");
            exit(0);
        }
        std::string command(const std::string& text, Player& player) override
        {
            return "";
        }
    };

    class Die : public Location
    {
    public:
        static constexpr const char* id = "die";
        void intro() override
        {
            fmt::print("You die! Please leave immediately.\n");
            exit(1);
        }
        std::string command(const std::string& text, Player& player) override
        {
            return "";
        }
    };
}

std::map<std::string, std::unique_ptr<Location>> make_locations()
{
    std::map<std::string, std::unique_ptr<Location>> locations;

    locations[locations::Cheese::id] = std::make_unique<locations::Cheese>();
    locations[locations::Haddock::id] = std::make_unique<locations::Haddock>();
    locations[locations::CrossRoads::id] = std::make_unique<locations::CrossRoads>();
    locations["north"] = std::make_unique<locations::DeadEnd>("south");
    locations["north"] == std::make_unique<locations::Cheese>(); // TODO: want a warning from this!!
    locations["south"] = std::make_unique<locations::DeadEnd>("north");
    locations["east"] = std::make_unique<locations::DeadEnd>("west");
    locations["west"] = std::make_unique<locations::DeadEnd>("east");
    locations[locations::Win::id] = std::make_unique<locations::Win>();

    return locations;
}

// Location& get_location(const std::string& location_id)
// {
// }

// # TODOs
// # "user" commands" (including inventory) - needs to take room as a param (e.g. for drop)
// # factor out moving out of rooms into Room (with a dict of directions -> room names)
// # Make goat into its own class, probably a subclass of Object / Item or something similar?
// # Add "look at" or "describe" commands, to get more detail about things
// # Make items at a location part of Room

int main(int argc, char* argv[])
{
    std::map<std::string, std::unique_ptr<Location>> locations = make_locations();

    auto player = Player();
    std::string current_location_name = "cheese";

    while (true)
    {
        Location& current_location = *locations[current_location_name];
        const std::string new_location_name = do_location(player, current_location);
        if (!new_location_name.empty())
        {
            // fmt::print("I received new location {}\n", new_location_name);
            current_location_name = new_location_name;
        }
    }

    return 0;
}
