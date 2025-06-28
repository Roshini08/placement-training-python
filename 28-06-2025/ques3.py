preferences = {'Action': ['The Dark Knight', 'Inception'], 'Comedy': ['The Hangover', 'Superbad']}
user_preference = 'Action'
recommendations = preferences.get(user_preference, [])
print("Recommendations:", recommendations)
