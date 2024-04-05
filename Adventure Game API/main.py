from fastapi import FastAPI

app = FastAPI()


game_state = True

player_inventory =[
    
]


game_locations = { 
    locations_name:
            
    
}

@app.get("/inventory/add")


"""
    Adventure Game API
    Adventure Game API
    Objective: Develop a FastAPI application that simulates a simple text-based adventure game. The game will explore locations, manage inventory, and interact with objects or NPCs (Non-Player Characters) through API calls.
    1. Setup and Basic Endpoints
    Initialize a FastAPI app.
    Define global variables for game state, including player inventory (list) and game locations (dictionary).
    2. Player Inventory Management
    Endpoint: /inventory/add 
    Body: Item name (str).
    Function: Add an item to the player's inventory. Use exception handling to manage adding duplicate items.
    Response: Return the updated inventory.
    Endpoint: /inventory/remove ()
    Body: Item name (str).
    Function: Remove an item from the player's inventory. Handle exceptions for removing items not in inventory.
    Response: Return the updated inventory.
    3. Exploring Locations
    Define a dictionary with location names as keys and details (description, items available, etc.) as values.
    Endpoint: /explore/{location_name} 
    Path Parameter: Location name.
    
"""