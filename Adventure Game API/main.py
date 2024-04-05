from fastapi import FastAPI , HTTPException

app = FastAPI()




player_inventory =["gamegear"]

"""
Define a dictionary with location names as keys and details (description, items available, etc.) as values.
Endpoint: /explore/{location_name} 
Path Parameter: Location name


"""



game_location_details = {
  "Whispering Woods": {
    "description": "An ancient forest shrouded in mist. Strange sounds echo through the trees. Watch out for tripwires!",
    "items": ["Herbs", "Mushrooms", "Wooden Staff (Quest Item)"],
    "enemies": ["Wolves", "Giant Spiders"]
  },
  "Abandoned Mine": {
    "description": "A collapsed mine rumored to hold forgotten treasures. Beware of unstable ground!",
    "items": ["Ores", "Gems", "Rusty Pickaxe"],
    "enemies": ["Cave Bats", "Giant Rats"]
  },
  "Sunken City": {
    "description": "The ruins of a once-grand civilization, now submerged underwater. Breathtaking views and lurking dangers await.",
    "items": ["Coral", "Pearls", "Ancient Artifacts"],
    "enemies": ["Giant Eels", "Mermaids (Hostile)"]  # Hostile enemies for variety
  },
  "Forgotten Library": {  # A non-combat location
    "description": "A dusty library filled with ancient tomes. The air is thick with the scent of aged paper and forgotten lore.",
    "items": ["Rare Books", "Scrolls (Lore Items)", "Enchanted Pen (Quest Item)"],
    "enemies": []  # No enemies here, just knowledge (or puzzles)
  }
}

@app.post("/inventory/add")
async def Add_item(item : str):
    """
    Endpoint: /inventory/add 
    
    Body: Item name (str).
    
    Function: Add an item to the player's inventory. Use exception handling to manage adding duplicate items.
    
    Response: Return the updated inventory.
        """
    # add_item = player_inventory.append(item)
    try:  
        if item: 
            player_inventory.append(item)
        else:
            raise HTTPException (status_code=404, detail="no item found")
        return {"inventory": player_inventory,  "message": "item added successfully"}
    except HTTPException and ValueError as e :
        return {"eror": e}

"""
    Endpoint: /inventory/remove ()
    Body: Item name (str).
    Function: Remove an item from the player's inventory. Handle exceptions for removing items not in inventory.
    Response: Return the updated inventory.
"""
@app.delete ("/inventory/remove")
async def remove_item (item: str):
    try:
        
        if item:
            player_inventory.remove(item)
        else:
            raise HTTPException(status_code=404, detail="item not found")
        return {"inventory": player_inventory ,"message " : "Item removed successfully"}
    except HTTPException and ValueError as e :
        return {"eror": e}