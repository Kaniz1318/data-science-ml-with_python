# a ="Good Morning, Rahim. How are you?" ---nam ta dynamic korbo user input niye


user_input = input("What's your name?")
a ="Good Morning, {}. How are you? {}".format(user_input,'hi')
print(user_input)
print(a)



age = 25
f_name = "Kaniz"
l_name = "Fatema"

txt = "I am {f_name} {l_name}. I am {age} years old.".format(f_name=f_name,l_name=l_name,age=age)
print(txt)


#Shortcut method
txt2 = f"I am {f_name} {l_name}. I am {age} years old."
print(txt2)