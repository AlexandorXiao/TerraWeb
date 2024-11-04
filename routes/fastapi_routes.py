from libs.WebServer import fastapi_app

from fastapi import HTTPException
from fastapi.responses import Response
import httpx
from PIL import Image
from io import BytesIO

MINECRAFT_SKIN_URL = "https://crafatar.com/skins/{}"
HEAD_SIZE = 64

@fastapi_app.get("/api/get_head/{username}")
async def get_player_head(username: str):
    async with httpx.AsyncClient() as client:
        uuid_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        response = await client.get(uuid_url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Player not found")
        player_data = response.json()
        uuid = player_data.get("id")
        
        skin_url = MINECRAFT_SKIN_URL.format(uuid)
        response = await client.get(skin_url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Skin not found")
        
        skin_image = Image.open(BytesIO(response.content))
    
    head_box = (8, 8, 16, 16)
    head_layer_2_box = (40, 8, 48, 16)
    
    head_image = skin_image.crop(head_box).resize((HEAD_SIZE, HEAD_SIZE), Image.NEAREST)
    
    head_layer_2_image = skin_image.crop(head_layer_2_box).resize((HEAD_SIZE, HEAD_SIZE), Image.NEAREST)

    final_head = Image.new('RGBA', (HEAD_SIZE, HEAD_SIZE))
    final_head.paste(head_image, (0, 0))
    final_head.paste(head_layer_2_image, (0, 0), head_layer_2_image)
    
    img_byte_arr = BytesIO()
    final_head.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return Response(content=img_byte_arr, media_type="image/png")