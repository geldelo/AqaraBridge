"""Constants for the Aqara Bridge component."""
DOMAIN = "aqara_bridge"

# Config flow fields
CONF_FIELD_ACCOUNT = "field_account"
CONF_FIELD_COUNTRY_CODE = "field_country_code"
CONF_FIELD_AUTH_CODE = "field_auth_code"
CONF_FIELD_SELECTED_DEVICES = "field_selected_devices"
CONF_FIELD_REFRESH_TOKEN = "field_refresh_token"
CONF_OCCUPANCY_TIMEOUT = 'occupancy_timeout'

# Cloud
SERVER_COUNTRY_CODES = ["CN", "USA", "KR", "RU", "GER"]
SERVER_COUNTRY_CODES_DEFAULT = "CN"

# CONFIG ENTRY
CONF_ENTRY_AUTH_ACCOUNT = "account"
CONF_ENTRY_AUTH_ACCOUNT_TYPE = "account_type"
CONF_ENTRY_AUTH_COUNTRY_CODE = "country_code"
CONF_ENTRY_AUTH_EXPIRES_IN = "expires_in"
CONF_ENTRY_AUTH_EXPIRES_TIME = "expires_datetime"
CONF_ENTRY_AUTH_ACCESS_TOKEN = "access_token"
CONF_ENTRY_AUTH_REFRESH_TOKEN = "refresh_token"
CONF_ENTRY_AUTH_OPENID = "open_id"

# HASS DATA
HASS_DATA_AUTH_ENTRY_ID = "auth_entry_id"
HASS_DATA_AIOTCLOUD = "aiotcloud"
HASS_DATA_AIOT_MANAGER = "aiot_manager"

CONF_DEBUG = "debug"
CONF_STATS = "stats"

OPT_DEBUG = {
    'true': "Basic logs",
    'verbose': "Verbose logs",
    'msg': "msg logs"
}

ATTR_CHIP_TEMPERATURE = "chip_temperature"
ATTR_FW_VER = "fw_ver"
ATTR_LQI = "lqi"
ATTR_VOLTAGE = "voltage"

PROP_TO_ATTR_BASE = {
    "chip_temperature": ATTR_CHIP_TEMPERATURE,
    "fw_ver": ATTR_FW_VER,
    "lqi": ATTR_LQI,
    "voltage": ATTR_VOLTAGE
}
