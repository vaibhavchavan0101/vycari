from social_core.pipeline.user import create_user as social_create_user
USER_FIELDS = ["username", "email"]

def custom_user_details(strategy, details, backend, user=None, *args, **kwargs):
    print('pipeline 5.1:--->', user)
    print('backend:--->', backend.name)
    print('details:--->', details)
    print('strategy:--->', strategy)
    print('user:--->', user)
    print('kwargs:--->', kwargs)
    """
    Set user details from the authentication provider's response.
    """
    if user:
        return {"is_new": False}

    fields = {
        name: kwargs.get(name, details.get(name))
        for name in backend.setting("USER_FIELDS", USER_FIELDS)
    }
    # if not fields.phone:
    #     return statucode(302)
    fields['phone'] = '9898981112'
    fields['bio'] = 'asbashdd'
    fields['country'] = 'india'
    fields['gender'] = 'M'
    print('fields12:--->', fields)
    if not fields:
        return

    return {"is_new": True, "user": strategy.create_user(**fields)}

social_create_user=custom_user_details