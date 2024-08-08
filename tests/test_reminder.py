from lib.reminder import *

def test_reminds_user_to_do_a_task():
    reminder = Reminder("Andy")
    reminder.remind_me_too("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Andy"