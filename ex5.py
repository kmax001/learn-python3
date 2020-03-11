my_name="金云杰"
my_age=35     #not a lie
my_height=74    #inches
my_weight=180   #lbs
my_eyes="Blue"
my_teeth="White"
my_hair='Brown'
#三种常用打印方式，可用end=''代替换行
print(f"Let's talk about {my_name}.")      
print("He's %s inches tall." %my_height)
print("He's {} pounds heavy.".format(my_weight))
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#this line is tricky,try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height},and {my_weight} I get {total}.")
#print("If I add %s,%s,and %s I get %s." %my_age %my_height %my_weight %total)
print("If I add {},{},and{} I get {}".format(my_age,my_height,my_weight,total))