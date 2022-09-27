import requests
import win32com.client as client
import os


try:
    # Login to modjoul dashboard using username/password
    db_user = os.getenv('ModDB_User')
    db_pass = os.getenv('ModDB_Pass')
    #print(db_user)
    #print(db_pass)
    payload = {"email": db_user, "password": db_pass}
    response = requests.post("https://api.modjoul.com/v1/login", data=payload)
    print(response.status_code)
    print(response.json())

    # Logout from modjoul dashboard
    access_token = response.json()['token']
    #access_token = 'xyz'
    authtoken = {'Authorization': f'Bearer {access_token}'}
    print(authtoken)
    logout_response = requests.post("https://api.modjoul.com/v1/logout", headers=authtoken)
    print(logout_response.status_code)
    if logout_response.status_code != 204:
        raise Exception("logout failed")
except:
    print("Login/Logout Failed")
    # Send email via outlook
    outlook = client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0)
    message.To = 'shridhar@modjoul.com'
    message.Subject = 'Modjoul Dashboard Login/Logout Failed'
    message.Body = 'Login/Logout Failed. Please check.'
    message.Save()
    message.Send()
