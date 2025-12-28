#!/usr/bin/env python3
import os
import re

# Chapter files in proper order (continuous numbering)
chapters = [
    "00_Prologue.md",
    "01_The_Third_Day.md",
    "02_The_Return.md",
    "03_The_Weight_of_Months.md",
    "04_What_Remains.md",
    "05_Old_Enemies_New_Concerns.md",
    "06_A_Day_at_the_Fishery.md",
    "07_The_Sleeping_Mind.md",
    "08_What_The_Wind_Knows.md",
    "09_The_Pruned_Archives.md",
    "10_The_Writing_On_The_Skin.md",
    "11_The_Song_of_Seven_Sorrows.md",
    "12_Devis_Price.md",
    "13_The_Fight.md",
    "14_Interlude_The_Door_That_Stayed_Closed.md",
    "15_The_Maers_Summons.md",
    "16_The_Maers_Court.md",
    "17_The_Dying_Maer.md",
    "18_The_Lackless_Door.md",
    "19_The_Lackless_Box.md",
    "20_The_War_That_Broke_The_World.md",
    "21_Beautiful_Games.md",
    "22_The_True_Story_of_Lanre.md",
    "23_The_Song_That_Heals.md",
    "24_Sim_and_Fela.md",
    "25_Return_to_Imre.md",
    "26_The_Binding.md",
    "27_The_Renegade.md",
    "28_The_Old_Roads.md",
    "29_The_Carving.md",
    "30_The_Songs_Purpose.md",
    "31_The_Cost_of_Doors.md",
    "32_Interlude_The_Truth_About_The_Amyr.md",
    "33_The_Four_Plate_Door.md",
    "34_The_Four_Plate_Door.md",
    "35_The_Last_Night.md",
    "36_The_Road_South.md",
    "37_The_City_of_Doors.md",
    "38_Three_Days.md",
    "39_The_Eve_of_Ending.md",
    "40_Three_Nights_in_Renere.md",
    "41_The_Ball_Begins.md",
    "42_The_Beautiful_Game.md",
    "43_The_Doors_Open.md",
    "44_The_Choice.md",
    "45_The_Confrontation.md",
    "46_Aftermath.md",
    "47_The_Return.md",
    "48_The_Silence_Within.md",
    "49_The_Road_North.md",
    "50_The_Hunt_Begins.md",
    "51_The_Broken_Oath.md",
    "52_The_Mountain_of_Silence.md",
    "53_The_Name_of_Silence.md",
    "54_The_Waystone.md",
    "55_Interlude_The_Weight_of_Confession.md",
    "56_Escape_From_the_Mountain.md",
    "57_The_Oath_Fulfilled.md",
    "58_Three_Things_Breaking.md",
    "59_The_Final_Battle.md",
    "60_The_Ending.md",
    "61_The_Escape.md",
    "62_The_Lock.md",
    "63_The_Thrice_Locked_Chest.md",
    "64_Interlude_The_Only_Door_Left.md",
    "65_The_Name_Spoken.md",
    "66_Walking_Into_War.md",
    "67_Epilogue_A_Silence_Broken.md",
]

def strip_metadata(content):
    """Remove HTML comment metadata blocks"""
    return re.sub(r'<!--\s*METADATA.*?-->\s*', '', content, flags=re.DOTALL)

def compile_manuscript():
    manuscript = []
    
    # Title page
    manuscript.append("# THE SILENCE OF THREE PARTS")
    manuscript.append("")
    manuscript.append("## An Unofficial Conclusion to the Kingkiller Chronicle")
    manuscript.append("")
    manuscript.append("---")
    manuscript.append("")
    manuscript.append("")
    
    total_words = 0
    
    for chapter_file in chapters:
        filepath = os.path.join("book", chapter_file)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Strip metadata
            content = strip_metadata(content)
            
            # Count words
            words = len(content.split())
            total_words += words
            
            # Add chapter content
            manuscript.append(content.strip())
            manuscript.append("")
            manuscript.append("")
            manuscript.append("---")
            manuscript.append("")
            manuscript.append("")
    
    # Write manuscript
    output = '\n'.join(manuscript)
    
    with open("The_Doors_of_Stone_Complete.md", 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Compiled {len(chapters)} chapters")
    print(f"Total word count: {total_words:,}")
    print(f"Output: The_Doors_of_Stone_Complete.md")

if __name__ == "__main__":
    compile_manuscript()
