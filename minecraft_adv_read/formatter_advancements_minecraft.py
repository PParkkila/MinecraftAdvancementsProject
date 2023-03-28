import copy
import dictionary_advancements
import advancement_checkers as ac
#______List of Advancements_______
#
#
#
#
#
#
#
# Minecraft: story/root
# Stone Age: story/mine_stone
# Getting an Upgrade: story/upgrade_tools
# Acquire Hardware: story/smelt_iron
# Suit Up: story/obtain_armor
# Hot Stuff: story/lava_bucket
# Isn't It Iron Pick: story/iron_tools
# Not Today, Thank You: story/deflect_arrow
# Ice Bucket Challenge: story/form_obsidian
# Diamonds!: story/mine_diamond
# We Need to Go Deeper: story/enter_the_nether
# Cover Me With Diamonds: story/shiny_gear
# Enchanter: story/enchant_item
# Zombie Doctor: story/cure_zombie_villager
# Eye Spy: story/follow_ender_eye
# The End?: story/enter_the_end

def main():
 
    print('Completed "Minecraft": ' + str(ac.minecraft()))
    print('Completed "Stone Age": ' + str(ac.stone_age()))
    print('Completed "Getting an Upgrade": ' + str(ac.getting_an_upgrade()))
    print('Completed "Acquire Hardware": ' + str(ac.acquire_hardware()))
    print('Completed "Suit Up": ' + str(ac.suit_up()))
    print('Completed "Hot Stuff": ' + str(ac.hot_stuff()))
    print('Completed "Isn\'t It Iron Pick": ' + str(ac.isnt_it_iron_pick()))
    print('Completed "Not Today, Thank You": ' + str(ac.not_today_thank_you()))
    print('Completed "Ice Bucket Challenge": ' + str(ac.ice_bucket_challenge()))
    print('Completed "Diamonds!": ' + str(ac.diamonds()))
    print('Completed "We Need to Go Deeper": ' + str(ac.we_need_to_go_deeper()))
    print('Completed "Cover Me With Diamonds": ' + str(ac.cover_me_with_diamonds()))
    print('Completed "Enchanter": ' + str(ac.enchanter()))
    print('Completed "Zombie Doctor": ' + str(ac.zombie_doctor()))
    print('Completed "Eye Spy": ' + str(ac.eye_spy()))
    print('Completed "The End?": ' + str(ac.the_end_q()))
    

    




if __name__ == "__main__":
    main()
    
