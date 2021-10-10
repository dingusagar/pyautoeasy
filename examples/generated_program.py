from pyautoeasy.screen_point import ScreenPoint


minimise = ScreenPoint(pos=(1835, 47))
minimise.click_here()


searchbar = ScreenPoint(pos=(220, 151))
searchbar.click_here()
searchbar.type_here("iron man photos")


images = ScreenPoint(pos=(277, 207))
images.click_here()


firstphoto = ScreenPoint(pos=(82, 393))
firstphoto.right_click_here()


save_image = ScreenPoint(pos=(218, 637))
save_image.click_here()


save_button = ScreenPoint(pos=(1530, 105))
save_button.click_here()

