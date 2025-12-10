--all of the necessary queries can be found here!

--SELECT browser_exe FROM browsers WHERE browser_name = "Chromium"
SELECT browser_exe FROM bpos LEFT JOIN browsers ON bpos.browser_ID = browsers.browser_ID WHERE browser_icon = "..\IMG\Firefox.png";