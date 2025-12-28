#!/usr/bin/env python3
import os
import shutil

# Current files in order
current_files = [
    "00_Prologue.md",
    "01_The_Third_Day.md",
    "02_The_Return.md",
    "03_The_Weight_of_Months.md",
    "04_What_Remains.md",
    "05_Old_Enemies_New_Concerns.md",
    "05b_A_Day_at_the_Fishery.md",
    "06_The_Sleeping_Mind.md",
    "07_What_The_Wind_Knows.md",
    "08_The_Pruned_Archives.md",
    "09_The_Writing_On_The_Skin.md",
    "10_The_Song_of_Seven_Sorrows.md",
    "10b_Devis_Price.md",
    "11_The_Fight.md",
    "12_Interlude_The_Door_That_Stayed_Closed.md",
    "13_The_Maers_Summons.md",
    "13b_The_Maers_Court.md",
    "14_The_Dying_Maer.md",
    "15_The_Lackless_Door.md",
    "16_The_Lackless_Box.md",
    "17_The_War_That_Broke_The_World.md",
    "18_Beautiful_Games.md",
    "19_The_True_Story_of_Lanre.md",
    "20_The_Song_That_Heals.md",
    "20b_Sim_and_Fela.md",
    "21_Return_to_Imre.md",
    "22_The_Binding.md",
    "23_The_Renegade.md",
    "24_The_Old_Roads.md",
    "25_The_Carving.md",
    "26_The_Songs_Purpose.md",
    "27_The_Cost_of_Doors.md",
    "28_Interlude_The_Truth_About_The_Amyr.md",
    "29_The_Four_Plate_Door.md",
    "29b_The_Four_Plate_Door.md",
    "30_The_Last_Night.md",
    "31_The_Road_South.md",
    "32_The_City_of_Doors.md",
    "33_Three_Days.md",
    "34_The_Eve_of_Ending.md",
    "34b_Three_Nights_in_Renere.md",
    "35_The_Ball_Begins.md",
    "36_The_Beautiful_Game.md",
    "36_The_Doors_Open.md",
    "37_The_Choice.md",
    "37_The_Confrontation.md",
    "38_Aftermath.md",
    "39_The_Return.md",
    "40_The_Silence_Within.md",
    "40b_The_Road_North.md",
    "41_The_Hunt_Begins.md",
    "42_The_Broken_Oath.md",
    "42_The_Mountain_of_Silence.md",
    "43_The_Name_of_Silence.md",
    "43_The_Waystone.md",
    "44_Interlude_The_Weight_of_Confession.md",
    "45_Escape_From_the_Mountain.md",
    "46_The_Oath_Fulfilled.md",
    "47_Three_Things_Breaking.md",
    "48_The_Final_Battle.md",
    "49_The_Ending.md",
    "50_The_Escape.md",
    "51_The_Lock.md",
    "52_The_Thrice_Locked_Chest.md",
    "53_Interlude_The_Only_Door_Left.md",
    "54_The_Name_Spoken.md",
    "55_Walking_Into_War.md",
    "56_Epilogue_A_Silence_Broken.md",
]

def get_chapter_name(filename):
    """Extract the chapter name without the number prefix"""
    # Remove .md extension
    name = filename[:-3]
    # Find the first underscore after the number
    parts = name.split('_', 1)
    if len(parts) > 1:
        return parts[1]
    return name

def renumber_chapters():
    book_dir = "book"
    
    # First pass: rename to temp names to avoid conflicts
    temp_names = []
    for i, old_file in enumerate(current_files):
        old_path = os.path.join(book_dir, old_file)
        if os.path.exists(old_path):
            temp_name = f"TEMP_{i:02d}.md"
            temp_path = os.path.join(book_dir, temp_name)
            shutil.move(old_path, temp_path)
            temp_names.append((temp_path, old_file))
            print(f"Temp: {old_file} -> {temp_name}")
    
    # Second pass: rename to final names
    new_files = []
    for i, (temp_path, old_file) in enumerate(temp_names):
        chapter_name = get_chapter_name(old_file)
        new_name = f"{i:02d}_{chapter_name}.md"
        new_path = os.path.join(book_dir, new_name)
        shutil.move(temp_path, new_path)
        new_files.append(new_name)
        print(f"Final: {old_file} -> {new_name}")
    
    print(f"\nRenamed {len(new_files)} chapters")
    return new_files

if __name__ == "__main__":
    new_files = renumber_chapters()
    
    # Print new file list for compile script
    print("\n# New chapter list for compile_manuscript.py:")
    for f in new_files:
        print(f'    "{f}",')
