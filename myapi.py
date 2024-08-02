from fastapi import FastAPI
import uvicorn

app = FastAPI()

temperature = 0
pH = 0
water_level = 0
healthy = 0
unhealthy = 0


@app.get("/updates")
def get_values():
    global temperature, pH, water_level, healthy, unhealthy
    return {
        "temp": temperature,
        "ph": pH,
        "water_lvl": water_level,
        "healthy": healthy,
        "unhealthy": unhealthy
    }


@app.get("/healthy")
def return_healthy():
    global healthy
    return healthy


@app.get("/unhealthy")
def return_unhealthy():
    global unhealthy
    return unhealthy


@app.get("/temperature")
def return_temperature():
    global temperature
    try:
        return temperature
    except Exception:
        return 'error'


@app.get("/ph")
def return_ph():
    global pH
    return pH


@app.get("/level")
def return_water_level():
    global water_level
    return water_level


def set_healthy(good):
    global healthy
    try:
        healthy = good
        return 'success'
    except Exception:
        return 'error'


def set_unhealthy(bad):
    global unhealthy
    try:
        unhealthy = bad
        return 'success'
    except Exception:
        return 'error'


def set_temperature(temp):
    global temperature
    temperature = temp


def set_ph(p):
    global pH
    pH = p


def set_water_level(level):
    global water_level
    water_level = level


def get_temperature():
    global temperature
    return temperature


def get_ph():
    global pH
    return pH


def get_water_level():
    global water_level
    return water_level


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8080)


def get_healthy():
    global healthy
    return healthy


def get_unhealthy():
    global unhealthy
    return unhealthy