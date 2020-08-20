## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_ask_email
* inform_email
  - send_OTP
  - utter_ask_otp
* inform_otp
  - verify_OTP

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_ask_email
* inform_email
  - send_OTP
  - utter_ask_otp
* inform_otp
  - verify_OTP

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
