# STORY DIRECTOR BY HARSHA VALLAMKONDA

import random
when = ['A few years ago', 'Yesterday', 'Last night',
        'A long time ago', 'On 25th April 2021']
who = ['Harsha', 'Phani', 'Charan', 'Lekhaj', 'Lokesh']
name = ['Devesh', 'Vasudev', 'HarshKumar', 'Siddarth', 'Dheerajchukkala']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'Project meeting', 'school', 'laundry']
happened = ['made a lot of friends', 'Eats a burger',
            'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(
    residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
