# EXAMPLE STATE
# state = {
#   "rooms": {
#     "1000": {
#       "phone-numbers;": ["07123456789", "07123456782"],
#       "access_token": "1234"
#     },
#     "1001": {
#       "phone-numbers": ["07123456789", "07123456782"],
#       "access_token": "1234"
#     }
#   }
# }

state = {}

def update_state(new_state):
  state = new_state

def get_state():
  return state

