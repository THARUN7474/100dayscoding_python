age: int
name: str
height: float
is_human: bool

#we can specify the data type of variable
# we can decide what type dadta needed and what it can give out        typehints these are usefull
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(122):
    print("You may pass")
else:
    print("Pay a fine.")







