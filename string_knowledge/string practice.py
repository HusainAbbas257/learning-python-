email = """
to:{friend_email}
Subject: Thank You for Visiting My Python Repository

Dear {friend_name},

I hope this email finds you well. I wanted to take a moment to thank you for visiting my Python repository on GitHub. Your time and interest mean a lot to me, and I really appreciate the support you've shown.

Your feedback is always welcome, and if you have any suggestions or questions, feel free to reach out. I am constantly working on improving the repository, and your input could be invaluable in that process.

Thank you once again for taking the time to check it out! Looking forward to hearing your thoughts.

Best regards,
Husain Abbas
Date: {date}
"""
fn=input("enter your name :")
fe=input("enter your e-mail:")
dt=input("enter date:")
print(email.format(friend_email=fe,friend_name=fn,date=dt))

#-----------sample output--------------------#
# enter your name :tung tung tung sahurr
# enter your e-mail:tungtungtungsahur@brainrot.com
# enter date:31 fabraury 1234

# to:tungtungtungsahur@brainrot.com
# Subject: Thank You for Visiting My Python Repository

# Dear tung tung tung sahurr,

# I hope this email finds you well. I wanted to take a moment to thank you for visiting my Python repository on GitHub. Your time and interest 
# mean a lot to me, and I really appreciate the support you've shown.

# Your feedback is always welcome, and if you have any suggestions or questions, feel free to reach out. I am constantly working on improving the repository, and your input could be invaluable in that process.

# Thank you once again for taking the time to check it out! Looking forward to hearing your thoughts.

# Best regards,
# Husain Abbas
# Date: 31 fabraury 1234