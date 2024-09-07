from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import uvicorn

app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

temperature = "0.0"
pH = "0.0"
water_level = "0"

data = {"water_level": water_level,
        "ph": pH,
        "temperature": temperature
        }

@app.post("/update_values")
async def update_values(request: Request):
    result = await request.json()
    values = result.get("result")

    data.update({"ph": values.get("ph"),
                "water_level": values.get("water_level"),
                "temperature": values.get("temperature")
                })

    return "updated"
    

async def stream_updates():                                                                                                                                             
    while True:
        # Simulate an update every 5 seconds                                                                                                
        await asyncio.sleep(3)
        # json_data = json.dumps(data)
        # Yield the JSON data
        # yield f"data: {json_data}\n\n"
        # You can modify the data here dynamically if needed
        yield f"data: {data}\n\n"

@app.get("/stream")
async def stream():
    return StreamingResponse(stream_updates(), media_type="text/event-stream")








# Run the FastAPI server with Uvicorn:
# `uvicorn filename:app --reload`

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7000)








# class_name = ''
# temperature = 0.0
# pH = 0.0
# water_level = 0
# healthy = 0
# unhealthy = 0

# all_values = {"class_name":class_name,
#               "healthy": healthy,
#               "unhealthy": unhealthy,
#               "water_level": water_level,
#               "ph": pH,
#               "temperature": temperature
#              }


# @app.get("/get_updates")
# def get_values():
#     global temperature, pH, water_level, healthy, unhealthy, class_name
#     return {
#         "class_name": class_name,
#         "temp": temperature,
#         "ph": pH,
#         "water_lvl": water_level,
#         "healthy": healthy,
#         "unhealthy": unhealthy
#     }

# @app.post("/post_updates")
# async def update_values(request: Request):
#     global healthy, unhealthy, water_level, pH, temperature, class_name
#     data = await request.json()
#     all_data = data.get('result')  # main request containing all the data
#     healthy = all_data.get('healthy')
#     unhealthy = all_data.get('unhealthy')
#     water_level = all_data.get('water_level')
#     pH = all_data.get('ph')
#     temperature = all_data.get('temperature')
#     class_name = all_data.get('class_name')

#     all_values.update({"class_name": class_name,
#                        "healthy": healthy,
#                        "unhealthy": unhealthy,
#                        "water_level": water_level,
#                        "ph": pH,
#                        "temperature": temperature})

#     return "update received"
    


# @app.get("/healthy")
# def return_healthy():
#     global healthy
#     return healthy


# @app.get("/unhealthy")
# def return_unhealthy():
#     global unhealthy
#     return unhealthy


# @app.get("/temperature")
# def return_temperature():
#     global temperature
#     try:
#         return temperature
#     except Exception:
#         return 'error'


# @app.get("/ph")
# def return_ph():
#     global pH
#     return pH


# @app.get("/level")
# def return_water_level():
#     global water_level
#     return water_level


# def set_healthy(good):
#     global healthy
#     try:
#         healthy = good
#         return 'success'
#     except Exception:
#         return 'error'


# @app.put("/update_healthy/{healthy_status}")
# def update_healthy(healthy_status: int):
#     set_healthy(healthy_status)
#     return 'healthy updated'


# @app.put("/update_unhealthy/{unhealthy_status}")
# def update_unhealthy(unhealthy_status: int):
#     set_unhealthy(unhealthy_status)
#     return 'unhealthy updated'


# @app.put("/update_temperature/{temperature_value}")
# def update_temperature(temperature_value: float):
#     set_temperature(temperature_value)
#     return 'temperature updated'


# @app.put("/update_ph/{ph_value}")
# def update_ph(ph_value: float):
#     set_ph(ph_value)
#     return 'ph updated'


# @app.put("/update_water_level/{level}")
# def update_water_level(level: int):
#     set_water_level(level)
#     return 'level updated'


# def set_unhealthy(bad):
#     global unhealthy
#     try:
#         unhealthy = bad
#         return 'success'
#     except Exception:
#         return 'error'


# def set_temperature(temp):
#     global temperature
#     temperature = temp


# def set_ph(p):
#     global pH
#     pH = p


# def set_water_level(level):
#     global water_level
#     water_level = level


# def get_temperature():
#     global temperature
#     return temperature


# def get_ph():
#     global pH
#     return pH


# def get_water_level():
#     global water_level
#     return water_level


# def start_server():
#     uvicorn.run(app, host="0.0.0.0", port=8080)


# def get_healthy():
#     global healthy
#     return healthy


# def get_unhealthy():
#     global unhealthy
#     return unhealthy
