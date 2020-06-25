def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('ramon', 'betances',
                             heigth="5'8", location='puerto rico',
                             birth='1965',)

print(user_profile)
