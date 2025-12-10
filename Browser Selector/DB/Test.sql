--all of the necessary queries can be found here!

--SELECT browser_exe FROM browsers WHERE browser_name = "Chromium"
SELECT browser_icon FROM bpos LEFT JOIN browsers ON bpos.browser_ID = browsers.browser_ID WHERE xpos = 1 and ypos = 0;