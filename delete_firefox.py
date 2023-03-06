def deleteBrowserHistory(self):
    import os
    firefox = os.path.join("C:", os.sep, "Users", os.getenv('username'), "AppData", "Roaming", "Mozilla", "Firefox","Profiles")  # get path to firefox
    list_profiles = os.listdir(firefox)  # list directory

    for i in list_profiles:  # for every founded profile
        sqlite_path = "C:\Users\\" + os.getenv('username') + "\AppData\Roaming\Mozilla\Firefox\Profiles\\" + i + "\places.sqlite"  # get path

        try:
            os.remove(sqlite_path)  # try to remove history - places.sqlite file
            return "Success!"
        except WindowsError as e:
            return "Error: " + e.strerror  # File can be used by another process
