names = ["gabo","gabinete", "gabito", "gabrielo", "gabilichus"]

message = "Aveces me dicen "
message_2 = "Otras veces "
print (message + names[0] + ".")
print (message_2 + names[2] + ".")

# Aqui comienzan los ejercicios 3.4 al 3.6

# 3.4

dinner_invitations = ["Jackie Chan","Bruce Lee","Ramon"]

invitation_message_1 = "Saludos "
invitation_message_2 = "quieres ir a Pizza Hut?"

print (invitation_message_1 + dinner_invitations[0] + ", " + invitation_message_2)
print (invitation_message_1 + dinner_invitations[2] + ", " + invitation_message_2)
print (invitation_message_1 + dinner_invitations[1] + ", " + invitation_message_2)

# uno tiro bomba (3.5)

denied_invitation = dinner_invitations.pop(2)
invitation_message_3 = " tiro bomba."

print (denied_invitation + invitation_message_3)

dinner_invitations.append("Tony Yaa")

print (dinner_invitations)
print (invitation_message_1 + dinner_invitations[2] + "," + invitation_message_2)

# 3.6

dinner_invitations.insert(0, "Denzel")
dinner_invitations.insert(2, "Jet Lee")
dinner_invitations.append("Wesley")

print (dinner_invitations)

# 3.7

invitation_message_4 = "Sorry guys, I'll be able to invite just two guest."
print (invitation_message_4)

del dinner_invitations[0]
len(dinner_invitations)

print (len(dinner_invitations))