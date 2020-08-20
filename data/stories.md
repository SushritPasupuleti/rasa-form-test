## happy path
* greet
  - utter_greet
  - utter_ask_email
* inform_email
  - send_OTP
  - utter_ask_otp
* inform_otp
  - verify_OTP
  - slot{"authenticated" : true}
  - utter_authenticated

## sad path 1
* greet
  - utter_greet
  - utter_ask_email
* inform_email
  - send_OTP
  - utter_ask_otp
* inform_otp
  - verify_OTP
  - slot{"authenticated" : true}

## sad path 2
* greet
  - utter_greet
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
