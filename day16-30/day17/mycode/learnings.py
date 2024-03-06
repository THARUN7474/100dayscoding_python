class NewLearningPurpose:
    pass

class Practice:
    var = "i am class delcared out of init fun variable"
    def __init__(self,id_no,name):
        print("i am init fun(constructer) i will always run,and self is me name of practice i will be you when used"
              "i can have variables and i will be passed to parameters when object is initialized as aruguments"
              "i will be having atrributes (variables) class  variables i can defiend here as basic")
        self.id = id_no
        self.name_of = name
        self.money = 0
        self.following = 0
        self.follower = 0
        print(f"i  will print 1st and when ever obeject is initiated with this class {self.money}")
        print("here the no of arguments from object initailization should match no of parameters other than self even "
              "it is declared to somevalue in main class")
        print("---------------------------------------------------------------------------------------------------")
    def method_wecan_make(self):
        print(f"i cna use the class attributes declared in init or normal---{self.id}")
        print(f"i cant use local declared vairables out of class even through resp object")
        print(f"I AM VAriable declared out of init fun and here i am in method----{self.var}")
        self.var= ("in method we can change the vairbales(declared either in init fun or out of it) too but changes "
                   "applied to that obejct itself but not others")
        print("we can pass the obejct name also as argument to parameter of funtion in class(method) and use ")
        print("\n")
        print(f"\n{self.var}\n")
        self.id=23
        print(f"\n{self.id}\n")
        print("====================================================================================================")
    def follow(self,user):
        user.follower += 1
        self.following +=1


tharun = Practice(1,"tharu")
print(tharun.id)
print(tharun.name_of)
print(tharun.money)
print(tharun.method_wecan_make())
# tharun.follow(user2)#here user2 is not yer declared so to use like this we need to use at last of all declarations



user2 = Practice(2,"noone")
user2.why = ("i can create insatance variables to keep for this object only and i use\n here class is main blueprint "
             "and object is insatance or form of it")
print(user2.name_of)
print(user2.why)
print("if tharun.why is prineted it throws error coz it is not defined in global(here in class)")
# print(tharun.why)
print(user2.method_wecan_make())
print(tharun.id)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
tharun.follow(user2)
print(tharun.follower)
print(tharun.following)
print(user2.following)
print(user2.follower)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")