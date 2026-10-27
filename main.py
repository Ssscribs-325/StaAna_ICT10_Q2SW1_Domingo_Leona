from pyscript import document

def candidate_checker(e):
    club_members = [
        'yatora yaguchi', 
        'masako saeki',
        'shirota',
        'shiraii',
        'yamamoto',
        'maru mori',
        'ryuji ayukawa',
        'yotasuke takahashi',
        'haruka hashida'
    ]

    f_name = document.getElementById('first-name').value
    l_name = document.getElementById('last-name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'"I would rather choose a safer and more ordinary path." Sorry, {f_name} is not a current member of the JHS Arts Club.', f'"People who are true to themselves make great art." Congrats {f_name}, you now are a member of the JHS Arts Club!')

    document.getElementById('message').innerHTML = messages[member_checker]