"""Constants for the mega integration."""
import re

DOMAIN = "mega"
CONF_MEGA_ID = "mega_id"
CONF_DIMMER = "dimmer"
CONF_SWITCH = "switch"
CONF_KEY = 'key'
TEMP = 'temp'
HUM = 'hum'
W1 = 'w1'
W1BUS = 'w1bus'
CONF_PORT_TO_SCAN = 'port_to_scan'
CONF_RELOAD = 'reload'
CONF_INVERT = 'invert'
CONF_PORTS = 'ports'
CONF_CUSTOM = '__custom'
CONF_HTTP = '__http'
CONF_ALL = '__all'
CONF_SKIP = 'skip'
CONF_MQTT_INPUTS = 'mqtt_inputs'
CONF_NPORTS = 'nports'
CONF_RESPONSE_TEMPLATE = 'response_template'
CONF_ACTION = 'action'
CONF_UPDATE_ALL = 'update_all'
CONF_GET_VALUE = 'get_value'
CONF_ALLOW_HOSTS = 'allow_hosts'
CONF_CONV_TEMPLATE = 'conv_template'
CONF_POLL_OUTS = 'poll_outs'
PLATFORMS = [
    "light",
    "switch",
    "binary_sensor",
    "sensor",
]
EVENT_BINARY_SENSOR = f'{DOMAIN}.sensor'
EVENT_BINARY = f'{DOMAIN}.binary'

PATT_SPLIT = re.compile('[;/]')

LONG = 'long'
RELEASE = 'release'
LONG_RELEASE = 'long_release'
PRESS = 'press'
SINGLE_CLICK = 'single'
DOUBLE_CLICK = 'double'
