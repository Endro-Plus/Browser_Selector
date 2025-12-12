--all of the necessary queries can be found here!

--SELECT browser_exe FROM browsers WHERE browser_name = "Chromium"
UPDATE browsers SET browser_exe = NULL WHERE  browser_ID = 10

DELETE FROM bpos WHERE browser_id = 23