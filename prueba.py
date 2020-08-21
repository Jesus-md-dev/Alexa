
import dropbox
import hashlib

accessToken = 'sl.AgOGDMe1Va54wk37OzuQCndtndRjUtzeiRSzckFAJZ_LMMfse0TsZB8ZcsLHK_-2faqjdAW-Unrie2qNwdEhaZq7-JLaSQkk9Qt0tcvPoIuM-Tdssz6CU8JwzuC1WNaPFzYSZec'
folder = "/Amazon Alexa"
dbx = dropbox.Dropbox(accessToken)
response = dbx.files_list_folder(path=folder)





#for f in response.entries:
path = folder+"/"+response.entries[0].name
md,res = dbx.files_download(path)
dbx.files_delete_v2(path)
