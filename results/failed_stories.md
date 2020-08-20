## happy path 1 (C:\Users\sushr\AppData\Local\Temp\tmpff57pezy\50747a89dbeb4fa78fb9dcf89ee869ec_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_ask_email -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->


## happy path 2 (C:\Users\sushr\AppData\Local\Temp\tmpff57pezy\50747a89dbeb4fa78fb9dcf89ee869ec_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_ask_email -->
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\sushr\AppData\Local\Temp\tmpff57pezy\50747a89dbeb4fa78fb9dcf89ee869ec_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_ask_email -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_goodbye -->


## sad path 2 (C:\Users\sushr\AppData\Local\Temp\tmpff57pezy\50747a89dbeb4fa78fb9dcf89ee869ec_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_ask_email -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye


## sad path 3 (C:\Users\sushr\AppData\Local\Temp\tmpff57pezy\50747a89dbeb4fa78fb9dcf89ee869ec_conversation_tests.md)
* greet: hi
    - utter_greet
    - action_listen   <!-- predicted: utter_ask_email -->
* mood_unhappy: very terrible   <!-- predicted: deny: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye


