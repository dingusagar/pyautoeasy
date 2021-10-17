
"""
_________________________________________________________________________________________
ScreenPoint refers to a point in the screen. All the recorded points are generated here.
You may use these objects and its methods to quickly create an automation script.
_________________________________________________________________________________________
"""

from pyautoeasy import ScreenPoint

searchmenu = ScreenPoint(pos=(95, 1046))
searchmenu.click_here()


searchbox = ScreenPoint(pos=(142, 165))
searchbox.click_here()
searchbox.type_here("chrome")


searchresult = ScreenPoint(pos=(122, 367))
searchresult.click_here()


addressbar = ScreenPoint(pos=(220, 67))
addressbar.click_here()
addressbar.type_here("car")


imagetab = ScreenPoint(pos=(343, 265))
imagetab.click_here(after_sleeping_for=1.5)


pic1 = ScreenPoint(pos=(163, 502))
pic1.click_here(after_sleeping_for=1.5)


picmenu = ScreenPoint(pos=(1510, 397))
picmenu.right_click_here(after_sleeping_for=1.5)


saveimageopt = ScreenPoint(pos=(1602, 694))
saveimageopt.click_here(after_sleeping_for=1.5)


savebtn = ScreenPoint(pos=(735, 555))
savebtn.click_here(after_sleeping_for=1.5)


nextbtn = ScreenPoint(pos=(1815, 254))
nextbtn.click_here()

picmenu = ScreenPoint(pos=(1510, 397))
picmenu.right_click_here(after_sleeping_for=1.5)


saveimageopt = ScreenPoint(pos=(1602, 694))
saveimageopt.click_here(after_sleeping_for=1.8)


savebtn = ScreenPoint(pos=(735, 555))
savebtn.click_here(after_sleeping_for=1.8)