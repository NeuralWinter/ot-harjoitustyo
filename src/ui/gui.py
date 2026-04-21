#code generated with AI begins here
import tkinter as tk
from tkinter import ttk
from entities.stats import roll_stats
from entities.race import RACES
from entities.character import Character
from entities.character_repository import CharacterRepository
from entities.character_class import CLASSES
from entities.background import BACKGROUNDS
from entities.skills import calculate_skill_value

class CharacterCreatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("D&D 5e Character Creator")
        self.root.geometry("600x500")

        self.current_frame = None
        self.character_data = {}

        self.show_welcome()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root, padx=20, pady=20)
        self.current_frame.pack(fill="both", expand=True)

    def show_welcome(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="D&D 5e Character Creator",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self.current_frame,
            text="Create your character step by step",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(
            self.current_frame,
            text="Create New Character",
            font=("Arial", 12),
            command=self.show_name_input
        ).pack(pady=20)

    def show_name_input(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Enter your character's name:",
            font=("Arial", 14)
        ).pack(pady=20)

        self.name_entry = tk.Entry(self.current_frame, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        if "name" in self.character_data:
            self.name_entry.insert(0, self.character_data["name"])

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_welcome
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_name
        ).pack(side="left", padx=10)

    def save_name(self):
        name = self.name_entry.get().strip()
        if name:
            self.character_data["name"] = name
            self.show_race_selection()
        else:
            tk.Label(
                self.current_frame,
                text="Please enter a name!",
                fg="red"
            ).pack()

    def show_race_selection(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Choose your race:",
            font=("Arial", 14)
        ).pack(pady=20)

        self.race_var = tk.StringVar()

        if "race" in self.character_data:
            self.race_var.set(self.character_data["race"])

        races = ["Human", "Elf", "Dwarf", "Halfling"]
        for race in races:
            tk.Radiobutton(
                self.current_frame,
                text=race,
                variable=self.race_var,
                value=race,
                font=("Arial", 12)
            ).pack(anchor="w", padx=50)

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_name_input
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_race
        ).pack(side="left", padx=10)

    def save_race(self):
        race = self.race_var.get()
        if race:
            self.character_data["race"] = race
            self.show_class_selection()
        else:
            tk.Label(
                self.current_frame,
                text="Please select a race!",
                fg="red"
            ).pack()

    def show_class_selection(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Choose your class:",
            font=("Arial", 14)
        ).pack(pady=20)

        self.class_var = tk.StringVar()

        if "character_class" in self.character_data:
            self.class_var.set(self.character_data["character_class"])

        classes = ["Fighter", "Wizard", "Rogue", "Cleric"]
        for cls in classes:
            tk.Radiobutton(
                self.current_frame,
                text=cls,
                variable=self.class_var,
                value=cls,
                font=("Arial", 12)
            ).pack(anchor="w", padx=50)

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_race_selection
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_class
        ).pack(side="left", padx=10)

    def save_class(self):
        character_class = self.class_var.get()
        if character_class:
            self.character_data["character_class"] = character_class
            self.show_background_selection()
        else:
            tk.Label(
                self.current_frame,
                text="Please select a class!",
                fg="red"
            ).pack()

    def show_background_selection(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Choose your background:",
            font=("Arial", 14)
        ).pack(pady=20)

        self.background_var = tk.StringVar()

        if "background" in self.character_data:
            self.background_var.set(self.character_data["background"])

        backgrounds = {
            "Acolyte": "You have spent your life in service to a temple.",
            "Criminal": "You have a history of breaking the law.",
            "Soldier": "You have fought in wars and know the horrors of battle.",
            "Sage": "You spent years learning the lore of the multiverse.",
            "Folk Hero": "You come from a humble background but are destined for greatness."
        }

        for bg, description in backgrounds.items():
            tk.Radiobutton(
                self.current_frame,
                text=f"{bg} - {description}",
                variable=self.background_var,
                value=bg,
                font=("Arial", 10),
                wraplength=500,
                justify="left"
            ).pack(anchor="w", padx=20, pady=2)

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_class_selection
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_background
        ).pack(side="left", padx=10)

    def save_background(self):
        background = self.background_var.get()
        if background:
            self.character_data["background"] = background
            self.show_stats_method()
        else:
            tk.Label(
                self.current_frame,
                text="Please select a background!",
                fg="red"
            ).pack()

    def show_stats_method(self):
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Choose stat method:",
            font=("Arial", 14)
        ).pack(pady=20)

        tk.Button(
            self.current_frame,
            text="Standard Array [15, 14, 13, 12, 10, 8]",
            font=("Arial", 12),
            command=lambda: self.show_stats_selection([15, 14, 13, 12, 10, 8])
        ).pack(pady=10)

        tk.Button(
            self.current_frame,
            text="Roll 4d6 drop lowest",
            font=("Arial", 12),
            command=self.roll_and_show_stats
        ).pack(pady=10)

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_background_selection
        ).pack(side="left", padx=10)

    def roll_and_show_stats(self):
        from entities.stats import roll_stats
        values = sorted(roll_stats(), reverse=True)
        rolled_text = ", ".join(str(v) for v in values)

        self.clear_frame()
        tk.Label(
            self.current_frame,
            text="You rolled:",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(
            self.current_frame,
            text=rolled_text,
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Re-roll",
            font=("Arial", 12),
            command=self.roll_and_show_stats
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Use these values",
            font=("Arial", 12),
            command=lambda: self.show_stats_selection(values)
        ).pack(side="left", padx=10)

    def show_stats_selection(self, values):
        values = [str(v) for v in values]
        self.current_values = values
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="Assign your stats:",
            font=("Arial", 14)
        ).pack(pady=10)

        values_text = ", ".join(str(v) for v in values)
        tk.Label(
            self.current_frame,
            text=f"Available values: {values_text}",
            font=("Arial", 10)
        ).pack()

        stats = ["strength", "dexterity", "constitution",
                "intelligence", "wisdom", "charisma"]

        self.stat_vars = {}
        stats_frame = tk.Frame(self.current_frame)
        stats_frame.pack(pady=10)

        for stat in stats:
            row = tk.Frame(stats_frame)
            row.pack(pady=3)

            tk.Label(
                row,
                text=f"{stat.capitalize()}:",
                font=("Arial", 12),
                width=15,
                anchor="w"
            ).pack(side="left")

            var = tk.StringVar()
            if "stats" in self.character_data:
                var.set(str(self.character_data["stats"].get(stat, "")))

            self.stat_vars[stat] = var
            ttk.Combobox(
                row,
                textvariable=var,
                values=values,
                width=5,
                state="readonly"
            ).pack(side="left")

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_background_selection
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_stats
        ).pack(side="left", padx=10)

    def save_stats(self):
        stats = {}
        for stat, var in self.stat_vars.items():
            if not var.get():
                tk.Label(
                    self.current_frame,
                    text="Please assign all stats!",
                    fg="red"
                ).pack()
                return
            stats[stat] = int(var.get())

        values_used = sorted(list(stats.values()))
        available = sorted([int(v) for v in self.current_values])
        if values_used != available:
            tk.Label(
                self.current_frame,
                text="Each value must be used exactly once!",
                fg="red"
            ).pack()
            return

        self.character_data["stats"] = stats
        self.show_skills_selection()

    def show_skills_selection(self):
        self.clear_frame()

        character_class = CLASSES[self.character_data["character_class"]]
        background = BACKGROUNDS[self.character_data["background"]]

        bg_skills = background.skill_proficiencies
        available_skills = [
            s for s in character_class.allowed_skills
            if s not in bg_skills
        ]

        tk.Label(
            self.current_frame,
            text="Choose skill proficiencies:",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(
            self.current_frame,
            text=f"Background gives: {', '.join(bg_skills)}",
            font=("Arial", 10),
            fg="green"
        ).pack(pady=5)

        tk.Label(
            self.current_frame,
            text=f"Choose {character_class.skill_count} more from your class skills:",
            font=("Arial", 10)
        ).pack(pady=5)

        self.skill_vars = {}
        skills_frame = tk.Frame(self.current_frame)
        skills_frame.pack(pady=10)

        for skill in available_skills:
            var = tk.BooleanVar()
            self.skill_vars[skill] = var
            tk.Checkbutton(
                skills_frame,
                text=skill.replace("_", " ").capitalize(),
                variable=var,
                font=("Arial", 11)
            ).pack(anchor="w", padx=50)

        self.skill_count_needed = character_class.skill_count
        self.bg_skills = bg_skills

        button_frame = tk.Frame(self.current_frame)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_stats_method
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Next",
            font=("Arial", 12),
            command=self.save_skills
        ).pack(side="left", padx=10)

    def save_skills(self):
        selected = [skill for skill, var in self.skill_vars.items() if var.get()]

        if len(selected) != self.skill_count_needed:
            tk.Label(
                self.current_frame,
                text=f"Please select exactly {self.skill_count_needed} skills!",
                fg="red"
            ).pack()
            return

        self.character_data["skill_proficiencies"] = self.bg_skills + selected
        self.show_character_summary()

    def show_character_summary(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(self.current_frame)
        scrollbar = ttk.Scrollbar(
            self.current_frame,
            orient="vertical",
            command=canvas.yview
        )
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window(
            (canvas.winfo_reqwidth() / 2, 0),
            window=scrollable_frame,
            anchor="n"
        )
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(
                canvas.find_all()[0],
                width=e.width
            )
        )
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        race = RACES[self.character_data["race"]]
        character = Character(self.character_data["name"])
        character.race = self.character_data["race"]
        character.character_class = self.character_data["character_class"]
        character.background = self.character_data["background"]
        character.set_stats(self.character_data["stats"], race)
        character.skill_proficiencies = self.character_data["skill_proficiencies"]

        tk.Label(
            scrollable_frame,
            text="Character Summary",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Label(
            scrollable_frame,
            text=str(character),
            font=("Arial", 12)
        ).pack()

        tk.Label(
            scrollable_frame,
            text=f"Background: {character.background}",
            font=("Arial", 12)
        ).pack()

        tk.Label(
            scrollable_frame,
            text="Stats:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        stat_order = ["strength", "dexterity", "constitution",
                    "wisdom", "intelligence", "charisma"]

        for stat in stat_order:
            value = character.stats[stat]
            modifier = character.get_modifier(stat)
            sign = "+" if modifier >= 0 else ""
            tk.Label(
                scrollable_frame,
                text=f"{stat.capitalize()}: {value} ({sign}{modifier})",
                font=("Arial", 11)
            ).pack()

        tk.Label(
            scrollable_frame,
            text="Skill Proficiencies:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        for skill in sorted(character.skill_proficiencies):
            value = calculate_skill_value(skill, character.stats,
                                        character.skill_proficiencies)
            sign = "+" if value >= 0 else ""
            tk.Label(
                scrollable_frame,
                text=f"{skill.replace('_', ' ').capitalize()}: {sign}{value}",
                font=("Arial", 11)
            ).pack()

        button_frame = tk.Frame(scrollable_frame)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            command=self.show_skills_selection
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Save Character",
            font=("Arial", 12),
            command=lambda: self.save_character(character)
        ).pack(side="left", padx=10)

    def save_character(self, character):
        repository = CharacterRepository()
        filename = repository.save(character)
        self.clear_frame()

        tk.Label(
            self.current_frame,
            text="✓ Character Saved!",
            font=("Arial", 20, "bold"),
            fg="green"
        ).pack(pady=20)

        tk.Label(
            self.current_frame,
            text=f"Saved to: {filename}",
            font=("Arial", 10)
        ).pack(pady=5)

        tk.Button(
            self.current_frame,
            text="Return to Main Menu",
            font=("Arial", 12),
            command=self.return_to_main
        ).pack(pady=20)

    def return_to_main(self):
        self.character_data = {}
        self.show_welcome()

def main():
    root = tk.Tk()
    CharacterCreatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
#code generated with AI ends here, I have never used tkinter and thought this would save the most time
