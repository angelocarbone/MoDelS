import ctypes
from sys import platform

if platform == "linux" or platform == "linux2":
    se = ctypes.CDLL("./libesminiLib.so")
elif platform == "darwin":
    se = ctypes.CDLL("./libesminiLib.dylib")
elif platform == "win32":
    se = ctypes.CDLL("./esminiLib.dll")
else:
    print("Unsupported platform: {}".format(platform))
    quit()


# Definition of SE_ScenarioObjectState struct
class SEScenarioObjectState(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_int),
        ("model_id", ctypes.c_int),
        ("control", ctypes.c_int),
        ("timestamp", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("h", ctypes.c_float),
        ("p", ctypes.c_float),
        ("r", ctypes.c_float),
        ("roadId", ctypes.c_int),
        ("t", ctypes.c_float),
        ("laneId", ctypes.c_int),
        ("laneOffset", ctypes.c_float),
        ("s", ctypes.c_float),
        ("speed", ctypes.c_float),
        ("centerOffsetX", ctypes.c_float),
        ("centerOffsetY", ctypes.c_float),
        ("centerOffsetZ", ctypes.c_float),
        ("width", ctypes.c_float),
        ("length", ctypes.c_float),
        ("height", ctypes.c_float),
    ]


# Define callback for scenario object enabling manipulating the state AFTER scenario step but BEFORE OSI output
# Use in combination with ExternalController in mode=additive in order for scenario actions to be applied first
def callback(state_ptr, b):
    state = state_ptr.contents
    print("callback for obj {}: x={} y={}".format(state.id, state.x, state.y))
    se.SE_ReportObjectPos(ctypes.c_int(state.id), ctypes.c_float(state.timestamp),
                          # position
                          ctypes.c_float(state.x + 1.0), ctypes.c_float(state.y + 20.0), ctypes.c_float(0.0),
                          # rotation
                          ctypes.c_float(state.h + 0.5), ctypes.c_float(state.p), ctypes.c_float(state.r),
                          # speed
                          ctypes.c_float(state.speed))


callback_type = ctypes.CFUNCTYPE(None, ctypes.POINTER(SEScenarioObjectState), ctypes.c_void_p)
callback_func = callback_type(callback)

# Intitialize esmini before register the callback
se.SE_Init(b"xosc/my_scenario.xosc", 0, 1, 0, 1)

# register callback for first object (id=0)
se.SE_RegisterObjectCallback(0, callback_func, 0)