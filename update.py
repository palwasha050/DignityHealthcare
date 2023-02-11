import impira
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


impira_api = impira.Impira(
    org_name="student.uet.edu.pk-7cbbad74",
    api_token="ITsSKGLZkPK-EE96ii5goWu4~wMZI8Sj2HmpX9Knvd5wL8uDMMwDKTs-liagPVMaX",
)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

string_list = filename.split("/")
print(string_list[-1])


files = [
    {
      "path": string_list[-1],
      "name": string_list[-1],
    },
  ]

uids = impira_api.upload_files("dd303dd5c3118d71", files)


# uids is a list of uids returned from the upload request
impira_api.poll_for_results("dd303dd5c3118d71", uids)
